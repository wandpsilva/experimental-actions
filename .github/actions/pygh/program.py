from github import Github

# First create a Github instance:

# using an access token
g = Github("access_token")

print("$$$$$$$$$$$$$$$$$$$$$$$ ESTOU AQUI $$$$$$$$$$$$$$$$$$$$$$$")

repo = g.get_repo("PyGithub/PyGithub")
print(repo)

# Github Enterprise with custom hostname
g = Github(base_url="https://{hostname}/api/v3", login_or_token="access_token")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name)