import requests

# Define the base URL of your API
base_url = 'http://localhost:5000/api'

# Test adding a person
def test_add_person():
    response = requests.post(base_url, json={'name': 'John Doe'})
    assert response.status_code == 201

# Test getting a person by ID
def test_get_person():
    response = requests.get(f'{base_url}/1')
    assert response.status_code == 200

# ... other tests for updating, deleting, and dynamic parameter handling ...

# Run the tests
if __name__ == '__main__':
    test_add_person()
    test_get_person()
    # ... call other test functions ...
