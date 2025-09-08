import requests

url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url)
if response.status_code == 200:
    pull_requests = response.json()
    pr_creators = {}
    for pull in pull_requests:
        creator = pull["user"]["login"]
        if creator in pr_creators:
            pr_creators[creator] += 1
        else:
            pr_creators[creator] = 1
    print(f"The pull request creator and their count")
    for creator, count in pr_creators.items():
        print(f"{creator}: {count}")
else:
    print(f"Unable to fetch the site , {response.status_code}")