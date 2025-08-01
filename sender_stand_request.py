import configuration
import requests
import data
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
response = post_new_user(data.user_body)
print(response.status_code)
def get_token():
    user_body = data.user_body.copy()
    user_response = post_new_user(user_body)
    assert user_response.status_code == 201
    return user_response.json()["authToken"]
def post_new_client_kit(body, token):
    auth_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
        json=body,
        headers=auth_headers
    )
