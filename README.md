# ID-Lookup
<h3>A powerful search tool that can find exposed email addresses and mobile numbers on Internet.</h3>

<b>First Thing First</b><br>
This tool is only capable of finding publicly available information using search engine, and do not illicitly breaks into any private databases. The tool should not be used as a recon tool for harvesting email addresses.


<br>
<b> Short working demonstration of HackTheKeyBoard </b><br>
https://www.youtube.com/watch?v=upqk_G0_hzc&feature=youtu.be
<br><br>

<b>How stuff works?</b>
This program  utilises requests package to send crafted search requests to Google Search engine. The program then reads the reponse from search results, peeps into every URL and extracts information using regular expression.

<br>
<b> Installation</b><br><br>
1) Install python interpreter (ignore if already installed) -> `apt-get install python3`<br>
2) Download or Clone this repository -> `git clone https://github.com/Sumeet-R/ID-Lookup`<br>
3) Install Dependencies -> `pip3 install -r requirements.txt` or manually install the mentioned packages in requirements.txt<br>
4) Run the program -> `python3 idlookup.py`<br>

