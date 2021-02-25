import json
file=open('Movies.json','r')
movies=json.loads(file.read())
print(movies['Inception']['date'])
print(movies['Inception'])