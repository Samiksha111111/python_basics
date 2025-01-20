import requests
url=''
response=request.get(url)
if response.status_code==200:
    data=response.json()
    print("")













if response.status_code == 200:
    posts = response.json()  # Parse JSON response
    print("Titles of the first 5 posts:")
    for post in posts[:5]:
        print(post['title'])
else:
    print("Failed to retrieve posts")
