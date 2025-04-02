Overview  :
   The application is built on **Django** Framework. The service will fetch the **TOP 10 Stories From HackerNews** using their **public API** and in returns give me data in JSON Format. 

   
   Working  :
   
      Public API will fetch the list of top stories ids.  
      then will request first 10 stories ids and their details as follows.
      
              Title (story headline)
              Author (who posted it)
              Score (amount of upvotes it has)
              Time ( a readable date)
              URL (link to the story)

      Now We will have our JSON Data 

EndPoints : 

            Endpoint: **api/top-news/**
            
            method - **GET**

Error Handling   : All the Potential Error Handling cases,scenario had been look after in the project
          Example:  If the Public API is down or not working it will show
          {
            "error": "Failed to fetch top stories. Status code: 500"
        }

        
Application Setup  :  

            Install the latest Django version in your code editor. 
                                       Use Command--- **pip install django**
            Now django is installed.Also Install some basic requirements like (requirements.txt), (corsheaders),(restframework),
            Create Your Django Project:
                                         **django-admin startproject hackernews_api(project_name)**
                                                      hackernews_api/
                                                      │── hackernews_api/
                                                      │   ├── __init__.py
                                                      │   ├── settings.py
                                                      │   ├── urls.py
                                                      │   ├── asgi.py
                                                      │   ├── wsgi.py
                                                      │── manage.py
                                                      
          Create your app:  **python manage.py startapp stories(app_name)**
                                                      stories/
                                                      │── __init__.py
                                                      │── admin.py
                                                      │── apps.py
                                                      │── models.py
                                                      │── views.py
                                                      │── tests.py
                                                      │── urls.py (This should be created manually)

         
           Your are in your django application
           
           Register stories(your_app_name) in Installed Apps in your setting.py (hackernews_api),Also add (corsheaders,rest-framework)
           
                     **INSTALLED_APPS [  'stories',
                                       'rest_framework', 
                                      'corsheaders', 
                                  ]**
                                  
           Run your Server  using **Python manage.py runserver..  **
           
        ** Visit url in your Browser : **http://127.0.0.1:8000/api/top-news/**  **


      
