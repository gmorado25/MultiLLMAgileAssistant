from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from rest_framework import status


class TestAppViews(TestCase):

    factory = APIRequestFactory()
    client = APIClient()

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
        homepage = "127.0.0.1:3000/"
        self.client.get(homepage)      

        sync_url = reverse('homepage') #should map to <host>:<port> that NextJS is running on
        response = self.client.get(sync_url)
        assert response.status_code == status.HTTP_200_OK

        dashboard_url = reverse('dashboard')
        response = self.client.get(dashboard_url)
        assert response.status_code == status.HTTP_200_OK

    def test_adminPanel_url_reachable(self):
        url = reverse('admin:index')
        response = self.client.get(url)
        assert response.status_code < 400 # will likely redirect, but this is ok since we're just checking reachability
    
