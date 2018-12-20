from pip._vendor import requests


U="https://ccapi.csslcloud.net/api/room/link?roomid=41EEFCE481E030309C33DC5901307461&userid=6634678BEDA5BB7D&time=1539831085&hash=a8e8b8c06e82d9c2ef7f94e4b070a00e====提交数据：roomid=41EEFCE481E030309C33DC5901307461&userid=6634678BEDA5BB7D&time=1539831085&hash=a8e8b8c06e82d9c2ef7f94e4b070a00e "
url = "https://document.csslcloud.net/api/document/upload?userid=83F203DAC2468694&docid=1FE5491B7EAA3A599C33DC5901307461"

files = {'file':open('F:/MyqWork/test.docx','rb')}
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Cache-Control': "no-cache",
    'Postman-Token': "a33c9ef5-55f1-4e92-93ba-f765bd08a62b"
    }

response = requests.request("POST", url, files=files)

print(response.text)