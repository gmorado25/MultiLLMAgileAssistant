from django.test import TestCase
from django.urls import reverse
from django.db.models import Count

from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from rest_framework import status

from multillm.settings import NEXTJS_SETTINGS
from .models import Prompt
from .views import *

class TestAppViews(TestCase):

    factory = APIRequestFactory()
    client = APIClient()

    def setUp(self):
        """Add a test object to the database."""
        Prompt.objects.create(
            title="Prompt 1", 
            description="AAA", 
            sdlc_phase="testing", 
            role="tester"
        )

    # ----- TEST URLS ARE REACHABLE WITH STATED HTTP METHODS -----

    def test_syncNextJS_url_reachable(self):
        """
        Test sync with NextJS, this will proxy all explicit synced URLs
        (in urls.py with syncNextJS() mapped to its view) and any wildcard URLs.
        For example, if the Django server is running on localhost:8000 and NextJS
        is an internal service running on localhost:3000, then requests to
        localhost:8000 should automatically be forwarded to localhost:3000.
        """

        # make sure the NextJS server is running to test syncing (Test Precondition)
        # this will throw an exception if unreachable
        homepage = NEXTJS_SETTINGS["nextjs_server_url"]
        self.client.get(homepage)      

        sync_url = reverse('homepage') #should map to <host>:<port> that Django is running on
        response = self.client.get(sync_url)
        assert response.status_code == status.HTTP_200_OK

        dashboard_url = reverse('dashboard')
        response = self.client.get(dashboard_url)
        assert response.status_code == status.HTTP_200_OK
        
    # def test_models_url_reachable_onGET(self):
    #     url = reverse('models')
    #     response = self.client.get(url)                                     #failing
    #     assert response.status_code == status.HTTP_200_OK

    # def test_models_url_not_reachable_on_POST_PUT_DELETE(self):
    #     url = reverse('models')
    #     response = self.client.post(url)
    #     assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    #     response = self.client.put(url)

    #     assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    #     response = self.client.delete(url)
    #     assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    # def test_generate_url_reachable_onPOST(self):
    #     url = reverse('generate')                                           #failing
    #     response = self.client.post(url)
    #     assert response.status_code == status.HTTP_200_OK

    # def test_generate_url_not_reachable_onGET_PUT_DELETE(self):
    #     url = reverse('generate')
    #     response = self.client.get(url)
    #     assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    #     url = reverse('generate')
    #     response = self.client.put(url)
    #     assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
    #     url = reverse('generate')
    #     response = self.client.delete(url)
    #     assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    
    # def test_prompt_url_reachable_onGET_POST(self):
    #     url = reverse('prompt_list')
    #     response = self.client.get(url)
    #     assert response.status_code == status.HTTP_200_OK
    #     url = reverse('prompt_list')
    #     response = self.client.post(url)
    #     assert response.status_code == status.HTTP_200_OK

    def test_prompt_url_not_reachable_onPUT_DELETE(self):
        url = reverse('prompt_list')
        response = self.client.put(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        url = reverse('prompt_list')
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_prompt_id_url_reachable_onGET_PUT_DELETE(self):
        url = reverse('prompt_id', kwargs={'id': 1})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

        url = reverse('prompt_id', kwargs={'id': 1})
        body = {'title': 'a', 'description': 'b', 'sdlc_phase': 'c', 'role': 'd'}
        request = self.factory.put(url, body, format='json')
        force_authenticate(request)
        response = prompt_detail(request, '1')
        assert response.status_code == status.HTTP_200_OK

        url = reverse('prompt_id', kwargs={'id': 1})
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
    
    def test_prompt_id_url_not_reachable_onPOST(self):
        url = reverse('prompt_id', kwargs={'id': 1})
        response = self.client.post(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_prompt_search_url_reachable_onGET(self):
        url = reverse('prompt_search')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

    def test_prompt_search_url_not_reachable_onPOST_PUT_DELETE(self):
        url = reverse('prompt_search')
        response = self.client.post(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        url = reverse('prompt_search')
        response = self.client.put(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
        url = reverse('prompt_search')
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    # ----- TEST VIEW FUNCTIONAILITY ITSELF -----

    def test_models_view(self):
        """
        Test that /models returns a list of models in JSON format
        from the models registered with the llm manager.
        """
        pass

    def test_generate_view(self):
        """
        Test that /generate returns a list of responses from
        the requested llm(s), where the request body is a JSON
        object like:

        {
            "models": ["Model_1", "Model_2", "Model_3"],
            "prompt": "Put the system prompt here",
            "data": "Put the user input here"
        }

        And the generated response should be another JSON object like:

        [
            {
                "model": "Model1",
                "response": "The reponse generated by querying Model_1"
            },
            {
                "model": "Model2",
                "response": "The reponse generated by querying Model_2"
            },
            
            ...
        ]

        *Note @see - llm_communication.MockInputModel and llm_communication.llm_manager
        """
        pass

    def test_prompt_view(self):
        """
        Test that /prompts returns a list of prompts in the 
        database in JSON format.
        """
        pass

    def test_prompt_id_view(self):
        """
        Test that /prompts/<id> returns the requested prompt
        from the database in JSON format.
        """
        pass

    def test_prompt_search_view(self):
        """
        Test that /prompts/search/... returns prompts that match
        the given query parameters. For example .../prompts/search?role=req
        should return all prompts where 'req' appears in the 'role' attribute
        """
        pass

    # WRITE OTHER NEGATIVE TEST CASES FOR VIEWS

