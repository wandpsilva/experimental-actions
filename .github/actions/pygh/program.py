import os
import requests
import sys
import json
import subprocess

def run():
    try:
        validate()
        #call_gh_api()
    except Exception as ex:
        print(f'ERRO: {ex}')
        sys.exit(1)


def compile():
    subprocess.run(['terraform', 'validate'], check=True)


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