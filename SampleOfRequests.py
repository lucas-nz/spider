import requests

githubEvents = requests.get("https://api.github.com/events")
print(githubEvents.text)
print(githubEvents.status_code)
print(githubEvents.content)
print(githubEvents.json())