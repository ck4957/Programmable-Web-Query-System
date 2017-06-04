"""
Creation Date: 4/10/2017
Course: Topics in Data Management(Web Services)
Description: Parse Text File to create Json File
Author: Chirag Kular (ck4957)
Version: Initial Version
"""
import json
import csv

def read_file_api(filename):
    '''

    :param filename:name of the file
    :return:json data of the given file
    '''
    result = []
    with open(filename) as txtfile:
        lines = txtfile.readlines()
        for index, row in enumerate(lines):
            splitdata = row.split("$#$")
            for id, value in enumerate(splitdata):
                if ("###") in value:
                    splitdata[id] = value.split("###")
            # print(len(splitdata))
            # JSON Structure #
            json_list = {
                'id': splitdata[0],
                'title': splitdata[1],
                'summary': splitdata[2],
                'rating': splitdata[3],
                'name': splitdata[4],
                'label': splitdata[5],
                'author': splitdata[6],
                'description': splitdata[7],
                'type': splitdata[8],
                'downloads': splitdata[9],
                'useCount': splitdata[10],
                'sampleUrl': splitdata[11],
                'downloadUrl': splitdata[12],
                'dateModified': splitdata[13],
                'remoteFeed': splitdata[14],
                'numComments': splitdata[15],
                'commentsUrl': splitdata[16],
                'tags': splitdata[17],
                'category': splitdata[18],
                'protocols': splitdata[19],
                'serviceEndpoint': splitdata[20],
                'version': splitdata[21],
                'wsdl': splitdata[22],
                'data_formats': splitdata[23],
                'apigroups': splitdata[24],
                'example': splitdata[25],
                'clientInstall': splitdata[26],
                'authentication': splitdata[27],
                'ssl': splitdata[28],
                'readonly': splitdata[29],
                'VendorApiKits': splitdata[30],
                'CommunityApiKits': splitdata[31],
                'blog': splitdata[32],
                'forum': splitdata[33],
                'support': splitdata[34],
                'accountReq': splitdata[35],
                'commercial': splitdata[36],
                'provider': splitdata[37],
                'managedBy': splitdata[38],
                'nonCommercial': splitdata[39],
                'dataLicensing': splitdata[40],
                'fees': splitdata[41],
                'limits': splitdata[42],
                'terms': splitdata[43],
                'company': splitdata[44],
                'updated': splitdata[45]
            }
            result.append(json_list)
    # print(result)
    with open('apiJson.json', 'w') as outfile:
        data = json.dumps(result)
        outfile.write(data)
    print('Successfully created the apiJson File')


def read_file_mashup(filename):
    '''

    :param filename:name of the file
    :return:json data of the file
    '''
    result = []
    with open(filename) as txtfile:
        lines = txtfile.readlines()
        for index, row in enumerate(lines):
            splitdata = row.split("$#$")
            for id, value in enumerate(splitdata):
                if ("###") in value:
                    splitdata[id] = value.split("###")
            json_list = {
                'id': splitdata[0],
                'title': splitdata[1],
                'summary': splitdata[2],
                'rating': splitdata[3],
                'name': splitdata[4],
                'label': splitdata[5],
                'author': splitdata[6],
                'description': splitdata[7],
                'type': splitdata[8],
                'downloads': splitdata[9],
                'useCount': splitdata[10],
                'sampleUrl': splitdata[11],
                'dateModified': splitdata[12],
                'numComments': splitdata[13],
                'commentsUrl': splitdata[14],
                'tags': splitdata[15],
                'APIs': splitdata[16],
                'updated': splitdata[17]
            }
            result.append(json_list)
    with open('mashupJson.json', 'w') as outfile:
        data = json.dumps(result)
        outfile.write(data)
    print('Successfully created the apiJson File')

def createCSV(filename):
    title = "id$#$title$#$summary$#$rating$#$name$#$label$#$author$#$description$#$type$#$downloads$#$useCount$#$sampleUrl$#$downloadUrl$#$dateModified$#$remoteFeed$#$numComments$#$commentsUrl$#$tag1###tag2###tag3$#$category$#$protocols$#$serviceEndpoint$#$version$#$wsdl$#$dataFormats$#$apigroups$#$example$#$clientInstall$#$authentication$#$ssl$#$readonly$#$VendorApiKits$#$CommunityApiKits$#$blog$#$forum$#$support$#$accountReq$#$commercial$#$provider$#$managedBy$#$nonCommercial$#$dataLicensing$#$fees$#$limits$#$terms$#$company$#$updated"
    splittitle = title.split("$#$")
    for id, value in enumerate(splittitle):
        if ("###") in value:
            splittitle[id] = ','.join(value.split("###"))
    with open('api.csv','w',newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(splittitle)

        with open(filename) as txtfile:
            lines = txtfile.readlines()
            for index, row in enumerate(lines):
                splitdata = row.strip().split("$#$")
                for id, value in enumerate(splitdata):
                    if ("###") in value:
                        splitdata[id] = '|'.join(value.split("###"))
                writer.writerow(splitdata)
    #print(splitdata)


def main():
    '''
    Main to provide the filename and call the respective function to parse them
    :return:
    '''
    # filename = 'api.txt'
    # read_file_api(filename)
    # filename = 'mashup.txt'
    # read_file_mashup(filename)
    createCSV('api.txt')


if __name__ == '__main__':
    main()
