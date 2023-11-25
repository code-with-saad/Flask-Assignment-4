import sys
sys.path.append(".")
from app import app

def test_create_customer_api():
    response = app.test_client().post("/register-customer", json={
        "email": "hello@gmail.com",
        "password": "123456"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["data"] is not None
    assert data["data"]["id"] > 0

def test_create_customer_api_without_email():
    response = app.test_client().post("/register-customer", json={
        "password": "123456"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]["message"] == "email field is required"

def test_create_customer_api_without_password():
    response = app.test_client().post("/register-customer", json={
        "email": "hello2@gmail.com"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]["message"] == "password field is required"

def test_create_admin_api():
    response = app.test_client().post("/register-admin", json={
        "email": "saad@gmail.com",
        "password": "123456"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["data"] is not None
    assert data["data"]["id"] > 0

def test_create_admin_api_without_email():
    response = app.test_client().post("/register-admin", json={
        "password": "123456"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]["message"] == "email field is required"

def test_create_admin_api_without_password():
    response = app.test_client().post("/register-admin", json={
        "email": "hello2@gmail.com"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]["message"] == "password field is required"

def test_login_user_api_for_admin():
    response = app.test_client().post("/login", json={
        "email": "saad@gmail.com",
        "password": "123456",
        "user_type": "Admin"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["message"] == "user login successfully"
    assert data["token"] is not None

def test_login_user_api_for_customer():
    response = app.test_client().post("/login", json={
        "email": "hello@gmail.com",
        "password": "123456",
        "user_type": "Customer"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["message"] == "user login successfully"
    assert data["token"] is not None

def test_login_user_api_without_email():
    response = app.test_client().post("/login", json={
        "password": "123456",
        "user_type": "Customer"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]["message"] == "email field is required"

def test_login_user_api_without_password():
    response = app.test_client().post("/login", json={
        "email": "hello@gmail.com",
        "user_type": "Customer"
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]["message"] == "password field is required"

def test_login_user_api_without_user_type():
    response = app.test_client().post("/login", json={
        "email": "hello@gmail.com",
        "password": "123456",
    })
    data = response.json
    assert data is not None
    assert type(data) is dict
    assert data["error"] is not None
    assert data["error"]["message"] == "user_type field is required"