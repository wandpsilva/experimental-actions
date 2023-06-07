from github import Github
import os

def run():
    token = os.environ['INPUT_GHTOKEN']
    print(token)

    # using an access token
    g = Github(token)
    print('TENTANDO EXIBIR TOKEN')
    print(g)

    # Github Enterprise with custom hostname
    g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")
    print('TENTANDO EXIBIR BASE URL')
    print(g)

    repo = g.get_repo("PyGithub/PyGithub")
    print(repo)

    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        print(repo.name)


if __name__ == '__main__':
      run()