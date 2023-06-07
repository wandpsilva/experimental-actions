from github import Github
import os

def run():
    token = os.environ['INPUT_GHTOKEN']
    print(token)

    # using an access token
    g = Github(token)

    # Github Enterprise with custom hostname
    g = Github(base_url="https://api.github.com/api/v3", login_or_token="access_token")

    repo = g.get_repo("PyGithub/PyGithub")

    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        print(repo.name)


if __name__ == '__main__':
      run()