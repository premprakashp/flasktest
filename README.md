# Flask Test app with JWT

Basic Flask python app with JWT enabled and mysql connection to retrieve data from db.

## Setup

### Setup virtual env and install flask

Install pip3 and virtual env in Ubuntu

```bash
sudo apt-get install python3-virtualenv
```

Set up virtual env and install deps

```bash
python3 -m venv venv
. venv/bin/activate
pip3 install Flask
pip3 install Flask-JWT
pip3 install flask-mysql
```

## Run app

```bash
export FLASK_ENV=development
export FLASK_APP=app.py
flask run --host=0.0.0.0
```

## Test app

### Getting new JWT Token
First get JWT Token for accessing protected endpoints using

```bash
curl --request POST \
  --url http://localhost:5000/auth \
  --header 'content-type: application/json' \
  --data '{
    "username": "user1",
    "password": "abcxyz"
}'
```

Sample response

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODkyNjAwNjMsImlhdCI6MTU4OTI1OTc2MywibmJmIjoxNTg5MjU5NzYzLCJpZGVudGl0eSI6MX0.XSQVyyoM2pwRy3urvGBpgxbUtzO4u7FH_weqYkNH9dw"
}
```

### Executing protected endpoint

```bash
curl --request GET \
  --url http://localhost:5000/users \
  --header 'authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1ODkxMzg2MTcsImlhdCI6MTU4OTEzODMxNywibmJmIjoxNTg5MTM4MzE3LCJpZGVudGl0eSI6MX0.0jnD3JSee8jHocB3C5ajGfAb8t7oNd9RbBdePJYrnWo'
```

Sample response

```json
{
  "users": [
    {
      "loginid": "admin",
      "name": "admin",
      "role": "A",
      "userid": 1
    },
    {
      "loginid": "test",
      "name": "test",
      "role": "A",
      "userid": 2
    }
  ]
}
```