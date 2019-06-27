from flask import Flask
from flask import jsonify
from flask import request
from mail import sendmail 
from gevent.pywsgi import WSGIServer
app = Flask(__name__)
@app.route('/mailserver',methods=['GET','POST'])
def mailService():
    try:
        payload = dict(request.get_json())
        name=payload['username']
        emailid=payload['emailid']
        result=sendmail(name,emailid)
        return jsonify({"Result":str(result)})
    except Exception as e:
        return jsonify({"Result":str(e)})

if __name__ == '__main__':
    http_server = WSGIServer(('', 8007), app)
    http_server.serve_forever()
