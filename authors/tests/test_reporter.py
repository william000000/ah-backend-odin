from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from .base_test import BaseTest

from ..apps.authentication.models import User

class TestReporter(BaseTest):

    def test_if_an_article_can_be_reported(self):
        
        response = self.client.post("/api/articles/{}/report/".format(self.slug), self.report_data, **self.headers)
        self.assertEqual(response.status_code, 201)

    # def test_if_report_data_is_returned(self):
        
    #     response = self.client.post("/api/articles/{}/report/".format(self.slug), self.report_data3, **self.headers)
    #     self.assertIsInstance('report', response.data)

    def test_if_blank_report_is_refused(self):

        response = self.client.post("/api/articles/{}/report/".format(self.slug), self.report_data2, **self.headers)
        self.assertEqual(response.status_code, 400)

    def wrong_object_request(self):
            response = self.client.post("/api/articles/{}/report/".format(self.slug), self.report_data3, **self.headers)
            
    def test_if_wrong_object_is_refused(self):
        self.assertRaises(KeyError, self.wrong_object_request)