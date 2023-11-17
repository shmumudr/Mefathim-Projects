import requests


API_GITHUB = 'https://api.github.com/search/repositories?q=language:python&sort=stars&per_page=30'
def get_github_data():
    response = requests.get(API_GITHUB)
    if response.status_code == 200:
        data = response.json()
        print(type(data))
        items = data['items']
        forks_stars = [(item["forks_count"], item["stargazers_count"]) for item in items]
        print (forks_stars)




get_github_data()