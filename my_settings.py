#my_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'rasberry', #2
        'USER': 'root', #3                      
        'PASSWORD': 'root',  #4              
        'HOST': '192.168.0.9',   #5                
        'PORT': '3306', #6
    }
}
SECRET_KEY = 'jq5kc&f21tj@n=3estca=^!!drfs5b&2-41op_zxe93ujp9r7k'