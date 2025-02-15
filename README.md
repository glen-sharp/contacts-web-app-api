# Contacts Hub API
Repository storing API code that allows basic HTTP requests, interacting with contact data stored locally in the repository. Written in Python using the 

## Features
The following endpoints are available to use.
### GET /contact_details
### POST /add_contact
Request payload:
```json
{
    "forename": "Ted",
    "surname": "Lasso",
    "address": "Richmond",
    "phone_number": 462946593
}
```

### DELETE /delete_contact
Query param:
```
/delete_contact?id=1
```

## Deploying API locally

```bash
# Install required python libraries
pip install -r requirements.txt

# Migrate DB queries to a local SQLite file
python contacts_web_app/manage.py migrate

# Run API server locally
python contacts_web_app/manage.py runserver
```

## Deploying API via Docker Image

```bash
docker build . -t contacts-api

docker run -p 8000:10 contacts-api:latest
```