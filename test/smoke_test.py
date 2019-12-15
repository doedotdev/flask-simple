import requests

request_info = requests.get('http://0.0.0.0:8080/info')

assert request_info.status_code == 200
assert request_info.headers['Content-Type'] == 'application/json'
assert request_info.json()['description'] == 'Flask Simple Example | Structure + Simplicity'
assert request_info.json()['version'] == '0.0.1'
assert request_info.json()['name'] == 'flask-simple'


request_home = requests.get('http://0.0.0.0:8080/home')

assert request_home.status_code == 200
assert 'text/html' in request_home.headers['Content-Type']
assert '<p>NAME: flask-simple</p>' in request_home.text
assert '<p>DESCRIPTION: Flask Simple Example | Structure + Simplicity</p>' in request_home.text
assert '<p>VERSION: 0.0.1</p>' in request_home.text


request_root = requests.get('http://0.0.0.0:8080/')

assert request_root.status_code == 200
assert 'text/html' in request_root.headers['Content-Type']
assert '<p>NAME: flask-simple</p>' in request_root.text
assert '<p>DESCRIPTION: Flask Simple Example | Structure + Simplicity</p>' in request_root.text
assert '<p>VERSION: 0.0.1</p>' in request_root.text


request_math_add_sub = requests.get('http://0.0.0.0:8080/add-sub?value_one=2&value_two=3')

assert request_math_add_sub.status_code == 200
assert request_math_add_sub.headers['Content-Type'] == 'application/json'
assert request_math_add_sub.json()['value_one'] == 2
assert request_math_add_sub.json()['value_two'] == 3
assert request_math_add_sub.json()['addition'] == 2 + 3
assert request_math_add_sub.json()['subtraction'] == 2 - 3


request_math_add_sub = requests.get('http://0.0.0.0:8080/mul-div?value_one=2&value_two=3')

assert request_math_add_sub.status_code == 200
assert request_math_add_sub.headers['Content-Type'] == 'application/json'
assert request_math_add_sub.json()['value_one'] == 2
assert request_math_add_sub.json()['value_two'] == 3
assert request_math_add_sub.json()['multiplication'] == 2 * 3
assert request_math_add_sub.json()['division'] == 2 / 3
