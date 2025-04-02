from django.http import JsonResponse
import requests
from datetime import datetime

def get_top_news_stories(request):
    try:        
        top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        response = requests.get(top_stories_url, timeout=10)
        
        if response.status_code != 200:
            return JsonResponse(
                {"error": "Failed to fetch top stories. Status code: {}".format(response.status_code)}, 
                status=500
            )
                
        top_story_id = response.json()[:10]
                
        stories = []
        for story_id in top_story_id:
            story_url = "https://hacker-news.firebaseio.com/v0/item/{}.json".format(story_id)
            story_response = requests.get(story_url, timeout=10)
            
            if story_response.status_code == 200:
                story_data = story_response.json()
                       
                timestamp = story_data.get('time', 0)
                readable_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                
                story = {
                    'title': story_data.get('title', 'No Title'),
                    'author': story_data.get('by', 'Unknown'),                    
                    'score': story_data.get('score', 0),
                    'time': readable_time,
                    'url': story_data.get('url', '#'),
                }
                stories.append(story)
        
        return JsonResponse({"stories": stories})
       
    except Exception as e:
        return JsonResponse({"error": "An unexpected error occurred: {}".format(str(e))}, status=500)