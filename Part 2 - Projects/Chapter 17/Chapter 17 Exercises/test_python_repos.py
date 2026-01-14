import requests


def test_github_api_status_code():
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
