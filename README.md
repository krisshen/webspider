# webspider project

## a web spider project

## tasks

### crawl data
- crawl property data per city (Done)
- save data to local csv file using Scrapy pipeline (Done)
- name csv files with city names (Done)
- format data, trim and remove blank lines (Done)
- command
  
    ```python
        #crawl and save data into csv files named with city name
        scrapy crawl tmlist
        #upload csv files to Google Sheet named with date time, currently hard coded file to be uploaded
        python myproject/sheets/uploaddata.py
    ```

### upload them to Google through Google Sheet and Drive API
- new Google sheet based on date, move it to specific folder (Done)
- read local csv file, upload to Google sheet (Done)
- name Google sheet by city name (To Do)

### publish data to web site (To Do)

