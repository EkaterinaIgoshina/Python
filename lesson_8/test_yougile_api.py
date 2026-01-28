import requests
import json

BASE_URL="https://ru.yougile.com/api-v2"


my_headers = {}
my_headers["Authorization"] = API_TOKEN
my_headers["Content-Type"] = "application/json; charset=utf-8"

def test_create_project():
    len_before = requests.get(BASE_URL + "/projects", headers=my_headers)
    list1 = json.loads(len_before.text)['paging']['count']
    payload = {
        "title": "Поток",
        "users": {}
    }
    response = requests.post(BASE_URL + "/projects", headers=my_headers, json=payload)
    len_after = requests.get(BASE_URL + "/projects", headers=my_headers)
    list2 = json.loads(len_after.text)['paging']['count']
    assert response.status_code == 201
    assert list2 == list1 + 1


def test_create_project_missing_title():
    payload = {
        "users": [
            {"id": "8c4b2647-7cbe-4418-82a4-e3edb90ef2d3"}
        ]
    }
    response = requests.post(BASE_URL + "/projects", headers=my_headers, json=payload)
    assert response.status_code == 400, "Ожидали статус 400 при отсутствии названия проекта"
    print("Ответ:", response.text)


def test_get_project():
    response = requests.get(f"{BASE_URL}/projects/{PROJECT_ID}", headers=my_headers)
    print(response.json())
    assert response.status_code == 200
    assert response.json().get("id") == PROJECT_ID


def test_get_project_invalid_id():
    invalid_project_id = "invalid_id"
    response = requests.get(f"{BASE_URL}/projects/{invalid_project_id}", headers=my_headers)
    print(response.json())
    assert response.status_code == 404


def test_update_project():
    len_before = requests.get(BASE_URL + "/projects", headers=my_headers)
    list1 = json.loads(len_before.text)['paging']['count']
    payload = {
        "title": "Поток1",
        "users": {}
    }
    response = requests.put(f"{BASE_URL}/projects/{PROJECT_ID}", headers=my_headers, json=payload)
    len_after = requests.get(BASE_URL + "/projects", headers=my_headers)
    list3 = json.loads(len_after.text)['paging']['count']
    assert response.status_code == 200
    assert list1 == list3



def test_update_project_with_empty_title():
    valid_project_id = PROJECT_ID
    payload = {
        "title": "",  # Пустое название проекта
        "users": {}
    }

    response = requests.put(f"{BASE_URL}/projects/{valid_project_id}", headers=my_headers, json=payload)
    assert response.status_code == 400, f"Ожидали статус 400, получили {response.status_code}: {response.text}"

















































