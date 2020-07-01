import json
import requests
from bs4 import BeautifulSoup
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('JOBLIST')

def job_scrape():
    titleList = []
    companyList = []
    salaryList = []
    locationList = []

    for i in range(0, 50, 10):
        page = requests.get(
            "https://ca.indeed.com/jobs?q=Hourly+Jobs&l=Canada&start="+str(i))
        content = BeautifulSoup(page.content, 'html.parser')

        allJobs = content.select('.result')

        for job in allJobs:
            try:
                title = job.find("a", class_="jobtitle").text.replace('\n', '')
            except:
                title = 'Not Available'

            titleList.append(title)

            try:
                location = job.find(
                    "div", class_="location").text.replace('\n', '')
            except:
                location = 'Not Available'

            locationList.append(location)

            try:
                company = job.find(
                    "span", class_="company").text.replace('\n', '')
            except:
                company = 'Not Available'

            companyList.append(company)

            try:
                salary = job.find(
                    "span", class_="salaryText").text.replace('\n', '')
            except:
                salary = 'Not Available'
            
            salaryList.append(salary)
    
    return {
         'jobTitles': titleList,
         'companies': companyList,
         'salaries': salaryList,
         'locations': locationList
    }
    
def lambda_handler(event,context):
    data = job_scrape()
    response = table.scan()
    databaseIndexCount= int(response['ScannedCount'])
    for id in range(0,len(data['salaries'])):
            dynamoRecord = {
                'JOB_ID': id + databaseIndexCount,
                'TITLE': data['jobTitles'][id],
                'COMPANY':data['companies'][id],
                'SALARY':data['salaries'][id],
                'LOCATION':data['locations'][id],
                'WEBSITE': 'indeed.com'
            }
            table.put_item(Item = dynamoRecord)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }