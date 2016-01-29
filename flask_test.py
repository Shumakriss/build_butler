from flask import Flask, request
import requests
import urllib2
import json

app = Flask(__name__)

@app.route('/api/jenkins', methods=['POST'])
def receive_build_data():
    build = request.json['build']
    phase = build['phase']
    if not phase == 'COMPLETED':
      return
    if 'status' in build and build['status'] == 'FAILURE':
      commit = build['scm']['commit']
      commitUrl = "https://api.github.com/repos/Shumakriss/JenkinsAlertsTestRepo/commits/" + commit
      commitDetails = requests.get(commitUrl).content
      commitJson = json.loads(commitDetails)
      print commitJson['author']['login']
    return "Received notification"

if __name__ == '__main__':
    app.run()
