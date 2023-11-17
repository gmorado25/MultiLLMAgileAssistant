import json

from django.test import TestCase
from django.urls import reverse

from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from rest_framework import status

from multi_llm.views.llm_query import LLMQuery
from multi_llm.views.function_based_views import models
from multi_llm.util import llm_manager
from multi_llm.models.test_model import MockInputModel

class TestMultiLLMViews(TestCase):

    factory = APIRequestFactory()
    client = APIClient()

    # ----- TEST URLS ARE REACHABLE WITH STATED HTTP METHODS -----
        
    def test_models_url_reachable_onGET(self):
        url = reverse('models')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_models_url_not_reachable_on_POST_PUT_DELETE(self):
        url = reverse('models')
        response = self.client.post(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        response = self.client.put(url)

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_generate_url_reachable_onPOST(self):
        url = reverse('generate') 
        response = self.client.post(url)
        assert response.status_code == status.HTTP_200_OK

    def test_generate_url_not_reachable_onGET_PUT_DELETE(self):
        url = reverse('generate')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        url = reverse('generate')
        response = self.client.put(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        url = reverse('generate')
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_formats_url_reachable_onGET(self):
        url = reverse('formats')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_formats_url_not_reachable_on_POST_PUT_DELETE(self):
        url = reverse('formats')
        response = self.client.post(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        response = self.client.put(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED    

    def test_format_search_url_reachable_onGET(self):
        url = reverse('format_search') + "?format=CSV_FORMAT"
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_format_search_url_not_reachable_on_POST_PUT_DELETE(self):
        url = reverse('format_search')
        response = self.client.post(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        response = self.client.put(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED    

    # ----- TEST VIEW FUNCTIONAILITY ITSELF -----

    def test_models_view(self):
        """
        Test that /models returns a list of models in JSON format
        from the models registered with the llm manager.
        """
        llm_manager.clearModels()
        args = {
            "model_name": "test-model",
            "response": "Hello!"
        }
        llm_manager.registerModel(id="Generate Test", model=MockInputModel, model_kwargs=args)

        url = reverse('models')
        request = self.factory.get(url)
        response = models(request)

        expected = json.loads('["Generate Test"]')
        assert response.data == expected

    def test_generate_view(self):
        generate_url = reverse('generate')
        generate_request = self.factory.post(
            path=generate_url,
            data=json.dumps({
                "models": ["Model_1"],
                "prompt": "Put the system prompt here",
                "data": "Put the user input here"
            }),
            content_type='application/json'
        )
        force_authenticate(generate_request)
        converted_request = Request(generate_request, parsers=[JSONParser()])
        response = LLMQuery().post(request=converted_request)

        expected = json.loads('[{"model": "Model_1", "response": "An error has occurred."}]')
        assert response.data == expected

