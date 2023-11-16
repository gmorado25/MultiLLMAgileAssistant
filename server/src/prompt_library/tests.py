from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from rest_framework import status

from prompt_library.models import Prompt
from prompt_library.views.function_based_views import prompt_list, prompt_detail

class TestPromptLibViews(TestCase):

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

    def test_prompt_url_reachable_onGET_POST(self):
        url = reverse('prompts')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

        body = {'title': 'a', 'description': 'b', 'sdlc_phase': 'c', 'role': 'd'}
        request = self.factory.post(url, body, format='json')
        force_authenticate(request)
        response = prompt_list(request)
        assert response.status_code == status.HTTP_201_CREATED

    def test_prompt_url_not_reachable_onPUT_DELETE(self):
        url = reverse('prompts')
        response = self.client.put(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

        response = self.client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_prompt_id_url_reachable_onGET_PUT_DELETE(self):
        url = reverse('prompt_id', kwargs={'id': 1})
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK

        body = {'title': 'a', 'description': 'b', 'sdlc_phase': 'c', 'role': 'd'}
        request = self.factory.put(url, body, format='json')
        force_authenticate(request)
        response = prompt_detail(request, '1')
        assert response.status_code == status.HTTP_200_OK

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

        response = self.client.put(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

        response = self.client.delete(url)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    # ----- TEST VIEW FUNCTIONAILITY ITSELF -----

    def test_prompt_view(self):
        """
        Test that /prompts returns a list of prompts in the 
        database in JSON format.
        """
        url = reverse('prompts')
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK


    def test_prompt_id_view(self):
    #Test that /prompts/<id> returns the requested prompt
    #from the database in JSON format. """
    # Add a prompt to the database
        prompt = Prompt.objects.create(
            title="Test Prompt", 
            description="Test description", 
            sdlc_phase="testing", 
            role="tester"
        )

        url = reverse('prompt_id', kwargs={'id': prompt.id})

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()

        self.assertEqual(data['id'], prompt.id)
        self.assertEqual(data['title'], prompt.title)
        self.assertEqual(data['description'], prompt.description)
        self.assertEqual(data['sdlc_phase'], prompt.sdlc_phase)
        self.assertEqual(data['role'], prompt.role)

    def test_prompt_search_view(self):
        """
        Test that /prompts/search/... returns prompts that match
        the given query parameters. For example .../prompts/search?role=req
        should return all prompts where 'req' appears in the 'role' attribute
        """
        pass

    # WRITE OTHER NEGATIVE TEST CASES FOR VIEWS

