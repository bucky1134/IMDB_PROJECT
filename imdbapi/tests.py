import json 
from django.urls import reverse
from  django.contrib.auth.models import User
from rest_framework  import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

#written the testcase for testing SOME Endpoints...
class imdbpapitest(APITestCase):
    def setUp(self):
        self.user=User.objects.create(username='vishal',password='Hyperlink@1234',is_staff=True,is_superuser=True)
        self.token=Token.objects.create(user=self.user)
        self.api_authentication()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token "+self.token.key)

    def testlistmovie(self):
        response=self.client.get('/api/movies')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def testcreatemovie_authentication(self):
        data={
        "name": "plan",
        "popularity": "78",
        "imdbscore": "6",
        "director": "mark snow",
        "date_added": "2021-07-05T07:47:10.317250Z",
        "writer": "gerorge lucas",
        "language": "english",
        "country": "united states",
        "awards": "gsgs",
        "description": "sg"
    }
        response=self.client.post('/api/movies/create',data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    
    def testcreatemovie_un_authentication(self):
        self.client.force_authenticate(user=None)
        data={
        "name": "plan",
        "popularity": "78",
        "imdbscore": "6",
        "director": "mark snow",
        "date_added": "2021-07-05T07:47:10.317250Z",
        "writer": "gerorge lucas",
        "language": "english",
        "country": "united states",
        "awards": "gsgs",
        "description": "sg"
    }
        response=self.client.post('/api/movies/create',data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)