## SoftServv API

### Notes

This is a very small API, built using the app factory schema in the Flask framework.
Many of the settings are easily changed, and you can add/takeaway if you choose to clone this repo.

This is the *public* version of the repo, meaning you will have to put your own api url, api key, and email information to use it.

API key
- This is a manually generated API key found in the .env file
- You can use Flask_SQLAlchemy as an ORM to set up a database to store more than one
- You should keep your API key secret

CORS
- This uses Flask_CORS, and has some code thrown in to ensure it is used only by a specific domain

Email
- This uses Flask_Mail to send messages to whoever is specified, by default it sends the message from the SoftServv website