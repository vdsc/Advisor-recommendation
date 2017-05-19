## Dependencies 
* apache solr
* beautiful soup python library
* `pip install beautifulsoup4`
## Starting up apache solr
*`cd solr-6.5.1/`
*`sudo bin/solr start -force`
### Starting up the app
* run testing.html file
* Note: solr has to be running in the background
* Start the Solr: sudo solr service start


*To create core: “solr create -c advisor”


*To POST the data: “bin/post -c advisor example/films/films.json”


*To CURL the data from terminal : ‘curl "http://localhost:8983/solr/advisor/select?indent=on&q=Mechanical&wt=json " '

*advisor is the core and you can create more cores and load more json files to it.