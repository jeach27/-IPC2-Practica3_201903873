from flask import Flask, Response, request

app = Flask(__name__)

@app.route('/events/', methods=['POST'])
def post_events():
    data = open('data.txt', 'w+')
    data.write(request.data.decode('utf-8'))
    data.close()
    return 'Se uso el metodo POST'


@app.route('/events/', methods=['GET'])
def get_events():
    data = open('data.txt', 'r+')
    return Response(response=data.read(),
                        mimetype='text/plain', content_type='text/plain')


@app.route('/events/', methods=['PUT'])
def put_events():
    data = open('data.txt', 'w')
    data.write(request.data.decode('utf-8'))
    data.close()
    return 'Se uso el metodo PUT'


@app.route('/events/', methods=['DELETE'])
def delete_events():
    data = open('data.txt', 'w')
    data.write(' ')
    data.close() 
    data = open('data.txt', 'r+')   
    return Response(response=data.read(),
                        mimetype='text/plain', content_type='text/plain')


if __name__=='__main__':
    app.run(debug=True,port=5000)