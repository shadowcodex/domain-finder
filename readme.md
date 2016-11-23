# pydomainfinder
Passive Domain Discover Tool using Python and a Whois API

This tool is meant to be used as a form of passive reconnaissance for Penetration Testing. It will allow you to find additional domains owned by a company or website you are trying to test.

It is important to note, that if you go to one of these site you break your passive reconnaissance. 

There will be an additional tool coming soon to grab screenshots passively as well.

[See Main Site! http://shadowxcodex.github.io/pydomainfinder] (http://shadowxcodex.github.io/pydomainfinder)

Install
---

First you need to download the dependencies...

    pip install requests

or 

    easy_install requests

Then download the actual program

    wget https://github.com/SHADOWxCODEX/pydomainfinder/archive/master.zip
    
    unzip master.zip
    
Use
---

Run the program 

    python pydomainfinder.py

1. The first prompt asks you for your targets acronym. For example "GGA".

2. The program then prompts for the meaning of each character in the acronym. 

3. The program asks if you want the domain contents in order or full combination. This will greatly reduce the amount of items you are polling for if you select in order. 

4. The program asks if you want .com's, .net's, .org's, or all.

5. The program confirms you want to make X amount of API calls.

6. The program checks the domains and stores them into the log files.


Log Files
===

* domain_available.txt
 * This file shows all domains that are available to register.
* domain_log.txt
 * This file shows all the domains that were tested.
* domain_registered.txt
 * This file shows all the domains that are currently registered (aka possible targets)
* domain_whois.txt
 * This file dumps the full whois data for later consumption and targets.

##TODO

* Allow other types of API's to be use (Aggregate to get more requests per month)
* Use JsonWhois to pull passive screenshots of targets website.
