## Dependencies 
* apache solr
* beautiful soup python library
* pip install beautifulsoup4`
## Installing Solr
* You will need the Java Runtime Environment (JRE) version 1.8 or higher. At a command line, check your Java version like this:
* $ java -version
* http://apache.ip-guide.com/lucene/solr/6.5.1/ 
* download: solr-6.5.1.tgz 
* $ cd ~/
* $ tar zxf solr-x.y.z.tgz
### Starting up apache solr
*`cd solr-6.5.1/`
*`sudo bin/solr start -force`
#### Starting up the app
* run testing.html file
* Note: solr has to be running in the background
* Start the Solr: sudo solr service start
* To create core: “solr create -c advisor”
* To POST the data: “bin/post -c advisor example/films/films.json”
* Note: .json files are crawled and parsed data e.g. ufl.json
* To CURL the data from terminal : ‘curl "http://localhost:8983/solr/advisor/select?indent=on&q=Mechanical&wt=json " '
* advisor is the core and you can create more cores and load more json files to it.
* launch the testing.html file and you can enter your query!
