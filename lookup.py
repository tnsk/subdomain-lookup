# -*- coding: utf-8 -*-
import urllib
import urllib2
import os
import subprocess
import sys

print "##############################################################"
print u"[+]          Yahya Tanışık [Subdomain Lookup]"
print u"[!]        iletisim : yahyatanisik[at]gmail.com"
print "##############################################################"


url = "http://anonymouse.org/cgi-bin/anon-www.cgi/http://api.hackertarget.com/reversedns/?q=" + sys.argv[1]

istek = urllib2.Request(url)

yanit = urllib2.urlopen(istek)

html = yanit.read()

print html

dosya = open("lists.txt","w")

dosya.write(html)

dosya.close()

subprocess.check_output("cat lists.txt | cut -d' ' -f1 > ip_lists.txt", shell=True)

subprocess.check_output("cat lists.txt | cut -d' ' -f2 > subs_lists.txt", shell=True)
