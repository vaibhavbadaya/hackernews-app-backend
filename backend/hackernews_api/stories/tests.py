from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
import json

class APITests(TestCase):
    
    @patch('stories.views.requests.get')
    def test_successful_api_response(self, mock_get):
        top_stories_mock = mock_get.return_value
        top_stories_mock.status_code = 200
        top_stories_mock.json.return_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                
        story_mock = mock_get.return_value
        story_mock.status_code = 200
        story_mock.json.return_value = {
            'title': 'Test Story',
            'by': 'testuser',
            'url': 'https://example.com',
            'score': 100,
            'time': 1617211200  
        }      
       
        response = self.client.get(reverse('top_stories'))                
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn('stories', data)
        self.assertEqual(len(data['stories']), 10)
        
    @patch('stories.views.requests.get')
    def test_hackernews_api_down(self, mock_get):
        
        mock_get.return_value.status_code = 500
        response = self.client.get(reverse('top_stories'))            
        self.assertEqual(response.status_code, 500)
        data = json.loads(response.content)
        self.assertIn('error', data)
