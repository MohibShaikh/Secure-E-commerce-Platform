import requests
import json

BASE_URL = 'http://localhost:8000'
USERNAME = 'testuser2'
EMAIL = 'test2@example.com'
PASSWORD = 'testpass123'

def test_registration():
    print("\nTesting Registration...")
    url = f"{BASE_URL}/api/users/api/register/"
    data = {
        "username": USERNAME,
        "email": EMAIL,
        "password": PASSWORD
    }
    
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return response.json() if response.ok else None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def test_login():
    print("\nTesting Login...")
    url = f"{BASE_URL}/api/users/api/login/"
    data = {
        "username": USERNAME,
        "password": PASSWORD
    }
    
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return response.json() if response.ok else None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def test_profile(access_token):
    print("\nTesting Profile...")
    url = f"{BASE_URL}/api/users/api/profile/"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    
    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return response.json() if response.ok else None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def test_edit_profile(access_token):
    print("\nTesting Edit Profile...")
    url = f"{BASE_URL}/api/users/api/profile/"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    data = {
        "username": USERNAME,
        "email": "updated2@example.com",
        "phone_number": "1234567890",
        "address": "123 Test St"
    }
    
    try:
        response = requests.put(url, headers=headers, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        return response.json() if response.ok else None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def test_logout():
    print("\nTesting Logout (client-side simulation)...")
    print("Tokens would be removed from local storage in a real client.")
    print("Logout successful.")

if __name__ == "__main__":
    # Test registration
    reg_response = test_registration()
    
    # Test login
    login_response = test_login()
    if login_response and 'access' in login_response:
        access_token = login_response['access']
        
        # Test profile
        profile_response = test_profile(access_token)
        
        # Test edit profile
        edit_response = test_edit_profile(access_token)
        
        # Test logout
        test_logout() 