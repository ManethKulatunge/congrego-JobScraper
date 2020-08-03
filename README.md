# congrego-JobScraper
Built an hourly job dashboard to assist individuals that lost their jobs due to the COVID-19 pandemic.

## Installation
```bash
* pip install bs4
* pip install requests
* pip install json
```
## AWS Architecture
![](images/architecture-draft1.jpeg)

There are two major sections for this AWS driven solution. One is to write data with regards to job postings to the DynamoDB. The other section is to read details with regards to job postings from the populated DynamoDB. 

There are 2 write lambdas with the code in the [Indeed Job Scraper](https://github.com/ManethKulatunge/congrego-JobScraper/blob/master/backEnd/indeedScraper.py) and the [Simply Hired Job Scraper](https://github.com/ManethKulatunge/congrego-JobScraper/blob/master/backEnd/simplyHiredScraper.py). These lambdas are scheduled by CloudWatch events and are triggered daily at 2pm EST (Cron Expression ```0 13 * * ? *```)
