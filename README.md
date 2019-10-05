# StockChat
Made with Python3, Redis, Django 2.2.6, SQLite (recommended to change if some actual database work is going to happen).

### To run the app
1. Navigate in the console to the root project directory
2. [Get Redis](https://redis.io/topics/quickstart) up in your local machine (using default port)
3. Install the project requirements contained in requirements.txt (If you are using a virtualenv, activate it before installing)

`pip3 install -r requirements.txt`

4. Execute the command

`python3 manage.py runserver`
5. Application should be running in http://localhost:8000/chat

### To run the test suite:
1. Navigate in the console to the project directory
2. Execute the command

`python3 -m unittest discover`


## Project components

### Chat
App mainly based in [django-channels](https://channels.readthedocs.io/en/latest/) to communicate with Redis.

### Stock-API (in package chatbot, for the future evolution)
Wrapper for requests made to the external API that provides the stocks values. 

## Limitations
- User management is non existent (and security that comes with it)
- Chat doesn't load all messages (so they are all lost if browser is refreshed)
- No index page is defined (404 returned in that case)
- The chatbot functionality is not actually decoupled, what is decoupled is the API that serves it
- Site base url hardcoded in the code (as localhost:8000)
- Redis URL is on settings, not allowing multi-environment right now
