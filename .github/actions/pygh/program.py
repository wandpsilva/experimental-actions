import os
import requests
import sys
import json

def run():

    try:
        call_gh_api()
        read_files()
    except Exception as ex:
        print(f'ERRO: {ex}')


def read_files():
    with open('Main.java') as f:
        lines = f.readlines()

    print(f'arquivo lido: ${lines}')


def call_gh_api():
    token = os.environ['INPUT_TK']
    url = "https://api.github.com/search/repositories?"
    querystring = {"q":"wandpsilva"}
    headers = {
        'Accept': "application/vnd.github+json",
        'X-GitHub-Api-Version': "2022-11-28",
        'Authorization': "Bearer " + token
    }
    print(headers)
    data = requests.get(url, headers=headers, params=querystring, verify=False)
    response = json.loads(data.content)
    print(response)

    #repo_name = response['items'][0]['name']
    #print(repo_name)


if __name__ == '__main__':
      run()