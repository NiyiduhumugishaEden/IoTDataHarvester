import requests

formData = {"device": "EdenDevice", "temperature": "32 cm"}
HTTP_Request = requests.post("http://insecure.benax.rw/iot/", data=formData)

if HTTP_Request:
    HTTP_Response = HTTP_Request.text
    print(HTTP_Response)