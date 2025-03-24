import requests
import pytest
import json

base_url ="https://openlibrary.org/search.json"

extracted_data={}

def test_search_book_byName():
    query_params ={"q":"the lord of the rings"}
    headers = {}
    payload = {}
    response = requests.get(base_url, params=query_params, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200

def test_search_book_by_title():
    query_params ={"q":"API Testing"}
    headers = {}
    payload = {}
    response = requests.get(base_url, params=query_params, headers=headers, data=payload)
    print(response.text)
    assert response.status_code == 200

def test_get_authorKey():
    query_params ={"q":"API Testing"}
    headers = {}
    payload = {}
    response = requests.get(base_url, params=query_params, headers=headers, data=payload)
    response_json = json.loads(response.text)
    print(response_json["docs"][0])
    print(response_json["docs"][0]["author_name"])
    print(response_json["docs"][0]["author_key"])    
    extracted_data["author"] = response_json["docs"][0]["author_name"]
    extracted_data["author_key"] = response_json["docs"][0]["author_key"]

def test_search_book_by_author():
    author_name = json.dumps(extracted_data['author'])
    url = f"?author={author_name}&sort=new"
    headers = {}
    payload = {}
    response = requests.get(base_url + url, headers, data=payload)
    response_json = json.loads(response.text)
    response_author_keys = response_json["docs"][0]["author_key"]
    extracted_author_keys = str(extracted_data["author_key"])
    for author_key in response_author_keys:
        if author_key in extracted_author_keys:
            print(f"Author key {author_key} found in extracted data.")
    assert response.status_code == 200
    
def test_author_works():
    author_key = extracted_data['author_key'][0]
    base_url ="https://openlibrary.org/works/"
    url = f"{author_key}.json"
    headers = {}
    payload = {}
    print (base_url + url)
    response = requests.get(base_url + url, headers, data=payload)
    response_json = json.loads(response.text)
    print(response_json)
    assert response.status_code == 200
