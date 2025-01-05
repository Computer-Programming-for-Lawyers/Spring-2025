
## Week 8 In Class Activity Instructions

*October 21, 2024*

Work with a partner to scrape [job postings from electionline](https://electionline.org/electionline-weekly/#tab-10).

First, open [the website](https://electionline.org/electionline-weekly/#tab-10) and use your browser's Inspect tool to examine how the site is structured. For example, focus on elements like `<div>`, `<p>`, and `<a>`, and check where the job titles, descriptions, and links are located.

Second, building off the starter code below, collect the following information and store it in a pandas dataframe: `job_title`, `job_url`, and `job_description`.

### Starter code
``` python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Electionline Weekly job postings page
url = "https://electionline.org/electionline-weekly"

# Header to prevent 403 error
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Send a GET request to fetch the content of the page
response = requests.get(url, headers=headers)

# Parse the page content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")
```

Some notes: 
* The job descriptions are listed under `#tab-10` but the content from each tab is returned when you scrape the url. As such, you will likely need to instruct your AI helper to select the content that is within the div element containing the `h2` header `Job Postings This Week`.
* The second half of lecture will feature a demonstration from Prof. Will Adler on:
    - how to extract information from the job descriptions
    - how to use GitHub Actions to automatically scrape and analyze the job descriptions each week.

Once you feel good about what you've scraped, add it to a Google Sheet and:
- File > Share > Publish to Web
- Set the options Link, Entire Document, Comma-separated values, hit Publish
- Copy the link and email it to will@wtadler.com

*Hint: You may want to write your pandas df to a csv, download that csv, and import into Google Sheets to avoid copy/paste issues.*

### Extra credit
If you finish early, try the following:

* Use a `for` or `while` loop to scrape job descriptions from previous electionline Weeklys. All job descriptions should still just go into one big DataFrame. Make sure that the date in the `date` column corresponds to the date on which the job was posted.
* If you finish **all** of that and still have time left over, try using the `gspread` package to write your DataFrame directly to a Google Sheet.

**After ~15 minutes of work, we'll ask students to volunteer to share their screens and show us what they accomplished, troubleshooting together as needed.**
