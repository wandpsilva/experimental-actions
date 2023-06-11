import os
import requests
import sys
import json

def run():

    try:
        #call_gh_api()
        validate_mapper()
    except Exception as ex:
        print(f'ERRO: {ex}')


def validate_mapper():
    print("-------------- VALIDATING MAPPER ---------------")

    with open('Main.java') as f:
        lines = f.readlines()

    if "@Mapper" in lines:
        print("Foi encontrado um mapper!")
        if "componentModel" not in lines:
            print("Mapper não possui a anotação componentmodel = spring")
        else:
            print("anotação componentmodel encontrada!")
        

    print("----------------------------------------------")


def call_gh_api():
    print("---------------- GETTING REPOS ----------------")
    token = os.environ['INPUT_TK']

    url = "https://api.github.com/search/repositories?"
    querystring = {"q":"wandpsilva"}
    headers = {
        'Accept': "application/vnd.github+json",
        'X-GitHub-Api-Version': "2022-11-28",
        'Authorization': "Bearer " + token
    }
    data = requests.get(url, headers=headers, params=querystring, verify=False)
    response = json.loads(data.content)

    items = response['items']
    for item in items:
        print(item['name'])
    
    print("----------------------------------------------")


if __name__ == '__main__':
      run()