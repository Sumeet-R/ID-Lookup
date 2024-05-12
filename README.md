# ID-Lookup
<h3>A powerful search tool that can find exposed email addresses and mobile numbers on Internet.</h3>

<b>First Thing First</b><br>
This tool is only capable of finding publicly available information using search engine, and do not illicitly breaks into any private databases. This tool should not be used as a recon tool for harvesting email addresses.
<br><br>
<b> Short working demonstration of ID-Looup </b><br>
https://www.youtube.com/watch?v=upqk_G0_hzc&feature=youtu.be
<br><br>
<b>How stuff works?</b>
This program  utilises requests package to send crafted search requests to Google Search engine. The program then reads the reponse from search results, peeps into every URL and extracts information using regular expression.
<br><br>
<b> Installation on Red Hat Enterprise Linux, CentOS, and Fedora</b><br>
> sudo yum update <br>
> sudo yum install python3 python3-pip git -y <br>
> git clone https://github.com/Sumeet-R/ID-Lookup <br>
> cd ID-Lookup <br>
> sudo pip3 install -r requirements <br>

<b> Installation on Debian, Ubuntu, Linux Mint, and elementary OS</b><br>
> sudo apt-get update <br>
> sudo apt-get install python3 python3-pip git -y <br>
> git clone https://github.com/Sumeet-R/ID-Lookup <br>
> cd ID-Lookup <br>
> sudo pip3 install -r requirements <br>

<b> Running the ID-Lookup</b><br>
> python3 idlookup.py
![alt text](https://github.com/Sumeet-R/ID-Lookup/blob/master/init.PNG?raw=true)


