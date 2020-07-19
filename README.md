# Djangostagram
Djangostagram imitating the famous social network service, Instagram, using Django engine

NOTE) SECRET_KEY in settings.py was saved in separate file that wasn't uploaded here.


After git clone, follow these:
  1) Enter the "Djangostagram" directory.
  2) Make virtual environment:
    - virtualenv venv  
    - venv\Scripts\activate (Or "source venv/bin/activate" in Mac)  
    - pip install -r requirements.txt  
  3) python manage.py migrate  
  4) python manage.py createsuperuser  
    - Fill in username, email address, password, password(again).  
  5) python manage.py runserver  
    - Go to 127.0.0.1:8000/admin  
    - Login with superuser account made above.  
    - You can now control the admin site.  
  6) Go to 127.0.0.1:8000  

It's the "Djangostagram" website, which is intended to show you.
