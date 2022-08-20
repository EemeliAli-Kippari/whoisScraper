from operator import index
from bs4 import BeautifulSoup
import requests
import sys


f= open('domains.txt', 'r')

#if you want to use command line arguments instead of a separate list, use this:
# replace main for loop beginning with "for domain in sys.argv[1:]"

for domain in f:
    url = 'https://www.whois.com/whois/' + domain
    params = {'param': domain}
    whois_page = requests.get(url).text
    soup = BeautifulSoup(whois_page, 'lxml')
    registrar = soup.find('pre', class_ = 'df-raw')
    tld = (domain.split('.')[-1]).strip()

    if tld == "com":
        print("\n" + domain.strip())
        for i in registrar:
            if "Registrar:" in i:
                words = i.split()
                print('Registrar: ' + words[words.index('Registrar:')+1])
    elif tld == "fi":
        print("\n" + domain.strip())
        for i in registrar:
            if "registrar..........:" in i:
                words = i.split()
                print('Registrar: ' + words[words.index('registrar..........:')+1])
    elif tld == "ee":
        print("\n" + domain.strip())
        for i in registrar:
            if "Registrar:" in i:
                words = i.split()
                print('Registrar: ' + words[words.index('Registrar:')+2] + " " + words[words.index('Registrar:')+3])
    elif tld == "se":
        print("\n" + domain.strip())
        for i in registrar:
            if "registrar:" in i:
                words = i.split()
                print('Registrar: ' + words[words.index('registrar:')+1])


        


#.fi, .ee, .se, .com and others seem to have a certain presentation in the whois searches. Needs a check for the TLD before performing the search