from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def proxy(path):
    # The local URL of your Raspberry Pi
    local_url = f'http://127.0.0.1:5000/{path}'
    
    if request.method == 'POST':
        response = requests.post(local_url, data=request.form, headers=request.headers)
    elif request.method == 'PUT':
        response = requests.put(local_url, data=request.form, headers=request.headers)
    elif request.method == 'DELETE':
        response = requests.delete(local_url, headers=request.headers)
    else:
        response = requests.get(local_url, params=request.args, headers=request.headers)
    
    return Response(response.content, status=response.status_code, headers=dict(response.headers))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
