from flask import Flask, request
import requests
import urllib2
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/notification')
def notification():
    return "Received a notification!"

@app.route('/api/jenkins', methods=['POST'])
def add_message():
    build = request.json['build']
    phase = build['phase']
    if not phase == 'COMPLETED':
      return "Uninteresting phase"
    if 'status' in build and build['status'] == 'FAILURE':
      commit = build['scm']['commit']
      commitUrl = "https://api.github.com/repos/Shumakriss/JenkinsAlertsTestRepo/commits/" + commit
      commitDetails = requests.get(commitUrl).content
      commitJson = json.loads(commitDetails)
      print commitJson['author']['login']
    return "Received notification"

if __name__ == '__main__':
    app.run(host='192.168.33.10', debug=True)
