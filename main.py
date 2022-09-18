import requests
from datetime import datetime
today = datetime.now()
GRAPH_ID = "graph1"
TOKEN = "Randomization"
USERNAME = "ayedegbe"
pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_delete_endpoint = f"{graph_update_endpoint}/{today.strftime('%Y%m%d')}"
user_params = {
    "token" : TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)
graph_config = {
    "id": "graph1",
    "name": "Workout graph",
    "unit": "km",
    "type": "float",
    "color": "ichou"

}
headers = {
    "X-USER-TOKEN": TOKEN
}
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many kilometers did you run todar?: "),
}
# graph_response = requests.put(url=update_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)
#
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)
response = requests.delete(url=pixel_delete_endpoint, headers=headers)
print(response.text)

