import requests
from bs4 import BeautifulSoup
import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('JOBLIST')

def job_scrape():
    
    titleList = []
    companyList = []
    locationList = []

    for i in range(1, 6, 1):
        pageURL = "https://www.simplyhired.ca/search?q=temporary&jt=temporary.htm"
        
        if i > 1:
            pageURL = pageURL.replace(".htm", "&pn="+str(i)+".htm")
            print(pageURL)
        
        page = requests.get(pageURL)
        
        content = BeautifulSoup(page.content, 'html.parser')

        allJobs = content.select('.SerpJob')

        for job in allJobs:
            try:
                title = job.find("h2", class_="jobposting-title").text.replace('\n', '')
            except:
                title = 'Not Available'

            titleList.append(title)

            try:
                location = job.find(
                    "span", class_="jobposting-location").text.replace('\n', '')
            except:
                location = 'Not Available'

            locationList.append(location)

            try:
                company = job.find(
                    "span", class_="jobposting-company").text.replace('\n', '')
            except:
                company = 'Not Available'

            companyList.append(company)
    
    return {
        'jobTitles': titleList,
        'companies': companyList,
        'locations': locationList
    }


def lambda_handler(event,context):
    
    data = job_scrape()
    response = table.scan()
    databaseIndexCount= int(response['ScannedCount'])
    print(databaseIndexCount)
    
    for id in range(0,len(data['jobTitles'])):
            dynamoRecord = {
                'JOB_ID': id + databaseIndexCount,
                'TITLE': data['jobTitles'][id],
                'COMPANY':data['companies'][id],
                'LOCATION':data['locations'][id],
                'WEBSITE': 'simplyhired.com'
            }
            table.put_item(Item = dynamoRecord)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
