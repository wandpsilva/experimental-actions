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
        merged_branches = os.environ['INPUT_BRANCHES']
        print(f'{merged_branches}')

        #call_gh_api(token)
        call_gh_pygithub(token)

    except Exception as ex:
        print(f'ERRO: {ex}')
        sys.exit(1)


def call_gh_pygithub(token):
    g = Github(token)
    g = Github(base_url="https://api.github.com", login_or_token=token)

    repo = "wandpsilva/experimental-actions"

    for branch in g.get_repo(repo).get_branches():
        branch_name = branch.name
        
        sha = branch.commit.sha
        
        commit = g.get_repo(repo).get_commit(sha)        
        commit_date = commit.commit.author.date

        if commit_date.month == 8 and branch.name != "main":
            # VERIFICAR SE O STATUS DA BRANCH É MERGED, SE SIM, DELETAR A MESMA
            # VERIFICAR SE O COMMIT DA BRANCH LIDA EXISTE NA BRANCH MAIN
            
            print("-------------------------------------------------")
            print(f'deleting branch: {branch_name} because its last commit was in {commit_date}')
            try:
                ref = g.get_repo(repo).get_git_ref(f'heads/{branch_name}')
                ref.delete()
                print(f'branch {branch_name} deleted.')
            except Exception:
                print(f'No such branch: {branch_name}')


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


if __name__ == '__main__':
      run()