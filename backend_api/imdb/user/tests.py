import json 
from django.urls import reverse
from rest_framework  import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

#Test cases for teting registration API.

class RegisterTestCase(APITestCase):
    def testregistrationwithdata(self):
        #Test data
        data={"username" : "vishu",
            "password" : "buckybaz",
            "email" : "vishalubercool@gmail.com",
            "is_superuser":"True",
            "is_staff":"True"
            }
        response=self.client.post('/user/register/',data) #sending request
        self.assertEqual(response.status_code,status.HTTP_201_CREATED) #comparing status code from reponse and stander one
    
    def testregistrationwithoutdata(self):
        response=self.client.post('/user/register/')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)