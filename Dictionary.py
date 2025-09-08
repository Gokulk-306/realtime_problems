import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

output = response.json()
if response.status_code != 200:
    print(f"Failed to fetch data. Status code: {response.status_code}")
else:
    for i in range(0,len(output)):
        print(i+1,":",output[i]["user"]["login"])