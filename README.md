# HIV-Project
Study of HIV in North America Region

### Articles of News Papers
The articles of different news paper of North America region is scraped here

### Prerequisites
* `python3` needs to be installed
* Required python libraries: `selenium` , `pandas` , `bs4`
* The `chromedriver` needs to be installed and added to `PATH` for this
* `newspaper` lib is used here to collect the articles details

### Content
 Every folder contains mainly 4 files :
 * The `grab_article_links.py` file collects the url of all the articles for a search keyword
 * The `article_links.txt` file contains urls for all the articles
 * The `grab_articles_details.py` file collects the details of an article (like headline, date of publication, text etc.) based on the urls from `articles_links.txt`
 * The `newspaper.csv` file contains the details of all the articles in `csv` format.
