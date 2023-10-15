import random
import requests
import json
from utility.demo_qa_utils import *


@allure.title("REST Apis")
class TestRestApis:

    def test_create_login_delete_user(self):

        user_name = "TestUser" + str(random.randint(0, 1000))
        pass_word = "TestPass#" + str(random.randint(0, 1000))

        # Create a user
        user_res = requests.post(user, data={"userName": user_name, "password": pass_word})
        print(user_res.text)
        assert user_res.status_code == 201, f"User not created successfully"
        user_data = json.loads(user_res.text)
        assert user_data.get("username") == user_name, f"Username is not same is response body"
        user_id = user_data.get("userId")

        # Login with the user
        login_res = requests.post(login, data={"userName": user_name, "password": pass_word})
        print(login_res.text)
        assert login_res.status_code == 200, f"Login successfully"

        # Generate the token
        token_res = requests.post(generate_token, data={"userName": user_name, "password": pass_word})
        print(token_res.text)
        assert token_res.status_code == 200, f"Generated token successfully"
        token_data = json.loads(token_res.text)
        assert token_data.get("status") == "Success", "Token status is not success"
        assert token_data.get("result") == "User authorized successfully.", "Token result message mismatch"

        # Delete user
        del_res = requests.delete(user + f"/{user_id}")
        print(f"Delete data --> {del_res.text}")

    def test_get_books(self):
        res = requests.get(books)
        assert res.status_code == 200, "Retrieved books successfully"
        book_data = json.loads(res.text)
        print(book_data)
