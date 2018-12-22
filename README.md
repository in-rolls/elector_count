## Elector Count

Electoral rolls within a state follow a set format. And you can use that fact to estimate the total number of electors in a state. Count the total number of pages in all the electoral rolls in a state, dock the count appropriately for front matter, etc., and estimate the total number of electors from that.

The [script](total_pdf_pages_in_tar_gz.py) iterates over a tarred and gzipped folder of pdfs and counts the total number of pages. It also spits out a list of errors, like empty pdfs. To run the script, edit the main method to enter the file name, and then type in the following on the command line:

```
pip install -r requirements.txt
python total_pdf_pages_in_tar_gz.py
```

The sample tar.gz that we have included doesn't include electoral rolls as the rolls have some personal information.

### Sample Approximate Counts

For Kerala, there are 24,445 English PDF files with total of 833,451 pages. And there are about 30 electors per page. The first two pages are devoted to information and map. This leaves us with (833451 - 24445*2)*30 or 23,536,830 electors.



