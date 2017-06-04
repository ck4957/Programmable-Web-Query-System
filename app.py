"""
Creation Date: 4/11/2017
Course: Topics in Data Management(Web Services)
Description: Flask App
Author: Chirag Kular (ck4957)
Version: Initial Version
"""
import json
from pymongo import MongoClient

from flask import Flask,render_template

application = Flask(__name__)

global mongo_obj
global db

@application.route('/')
def load_page():
    htmlpage = 'index.html'
    return render_template(htmlpage)


@application.route('/getMashupData',methods=['GET'])
def getMashupDatafromDB():

    # Create object of Mongo Client
    mongo_obj = MongoClient('localhost:27017')

    # Select the database
    db = mongo_obj.test

    # Now get the data from the database
    mashup_data = db.mashup_data.find()

    resultList = []

    for index,data in enumerate(mashup_data):
        one_item = {
            'id': data['id'],
            'title': data['title'],
            'summary': data['summary'],
            'rating': data['rating'],
            'name': data['name'],
            'label': data['label'],
            'author': data['author'],
            'description': data['description'],
            'type': data['type'],
            'downloads': data['downloads'],
            'useCount': data['useCount'],
            'sampleUrl': data['sampleUrl'],
            'dateModified': data['dateModified'],
            'numComments': data['numComments'],
            'commentsUrl': data['commentsUrl'],
            'tags': data['tags'],
            'APIs': data['APIs'],
            'updated': data['updated']

        }
        resultList.append(one_item)
    mongo_obj.close()
    return json.dumps(resultList)

@application.route('/getApiData',methods=['GET'])
def getDatafromDB():

    # Create object of Mongo Client
    mongo_obj = MongoClient('localhost:27017')

    # Select the database
    db = mongo_obj.test

    # Now get the data from the database
    api_data = db.api_data.find()
    resultList = []
    for index,data in enumerate(api_data):
        one_item = {
            'id' : data['id'],
            'title': data['title'],
            'summary': data['summary'],
            'rating': data['rating'],
            'name': data['name'],
            'label': data['label'],
            'author': data['author'],
            'description': data['description'],
            'type': data['type'],
            'downloads': data['downloads'],
            'useCount': data['useCount'],
            'sampleUrl': data['sampleUrl'],
            'downloadUrl': data['downloadUrl'],
            'dateModified': data['dateModified'],
            'remoteFeed': data['remoteFeed'],
            'numComments': data['numComments'],
            'commentsUrl': data['commentsUrl'],
            'tags': data['tags'],
            'category': data['category'],
            'protocols': data['protocols'],
            'serviceEndpoint': data['serviceEndpoint'],
            'version': data['version'],
            'wsdl': data['wsdl'],
            'data_formats': data['data_formats'],
            'apigroups': data['apigroups'],
            'example': data['example'],
            'clientInstall': data['clientInstall'],
            'authentication': data['authentication'],
            'ssl': data['ssl'],
            'readonly': data['readonly'],
            'VendorApiKits': data['VendorApiKits'],
            'CommunityApiKits': data['CommunityApiKits'],
            'blog': data['blog'],
            'forum': data['forum'],
            'support': data['support'],
            'accountReq': data['accountReq'],
            'commercial': data['commercial'],
            'provider': data['provider'],
            'managedBy': data['managedBy'],
            'nonCommercial': data['nonCommercial'],
            'dataLicensing': data['dataLicensing'],
            'fees': data['fees'],
            'limits': data['limits'],
            'terms': data['terms'],
            'company': data['company'],
            'updated': data['updated']
        }

        resultList.append(one_item)
    mongo_obj.close()
    return json.dumps(resultList)


if __name__ == '__main__':
    application.run(host = '127.0.0.1')