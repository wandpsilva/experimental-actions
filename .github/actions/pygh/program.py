import os
import requests
import sys
import json
import subprocess
from github import Github
#from github import Auth

def run():
    try:
        token = os.environ['INPUT_TK']

        #validate()
        #call_gh_api(token)
        call_gh_pygithub(token)

    except Exception as ex:
        print(f'ERRO: {ex}')
        sys.exit(1)


def validate():
    print('### iniciando terraform ###')
    subprocess.run(['terraform', 'init'], check=True)

    print('### validando código terraform ###')
    subprocess.run(['terraform', 'validate'], check=True)


def call_gh_api(token):
    print("---------------- GETTING REPOS ----------------")

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


def call_gh_pygithub(token):
    print("---------------- GETTING REPOS ----------------")

    #auth = Auth.Token(token)
    g = Github(token)
    g = Github(base_url="https://{hostname}/api/v3/api/v3", login_or_token=token)

    for repo in g.get_user().get_repos():
        print(repo.name)

    print("----------------------------------------------")


if __name__ == '__main__':
      run()