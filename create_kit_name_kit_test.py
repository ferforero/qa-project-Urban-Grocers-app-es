import sender_stand_request
import data
def get_kit_body(name):
    current_name = data.kit_body.copy()
    current_name["name"] = name
    return current_name
def positive_assert(name):
    token = sender_stand_request.get_token()
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert kit_response.status_code == 201
def negative_assert_symbol(name):
    token = sender_stand_request.get_token()
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres"

def test_create_kit_1_letter_name_get_success_response():
    positive_assert(data.tests_kit["test_case_1"])
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert(data.tests_kit["test_case_2"])
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol(data.tests_kit["test_case_4"])
def test_create_kit_has_special_symbol_in_name_get_success_response():
    positive_assert(data.tests_kit["test_case_5"])
def test_create_kit_has_space_in_name_get_success_response():
    positive_assert(data.tests_kit["test_case_6"])
def test_create_kit_has_number_in_name_get_error_response():
    positive_assert(data.tests_kit["test_case_7"])
def negative_assert_no_name(kit_body):
    token = sender_stand_request.get_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)# aqui deberia ir el post_new_client_kit???
    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name") #test case 8
    negative_assert_no_name(kit_body)
def test_create_user_empty_first_name_get_error_response():
    kit_body = get_kit_body("") #test case 3
    negative_assert_no_name(kit_body)
def test_create_user_number_type_first_name_get_error_response():
    token = sender_stand_request.get_token()
    kit_body = get_kit_body(data.tests_kit["test_case_9"]) #test case 9
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400

