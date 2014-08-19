
import re
import os
import urllib2 
from xml.dom import minidom 

'''
To run this every weekday at 10am, type in

    crontab -e

and add the following line

    0 10 * * 1-5  python /home/pi/bin/phatthai_alert.py

Don't forget to setup the clock on local time!
'''

address = "http://menus.epfl.ch/cgi-bin/rssMenus"
restaurant = "hong tha. rung"

meal = "pha. tha."
text = 'This is a Phat Thai Alert! Proceed to Hong Thai Rung immediately.'
subject = 'Phat Thai Alert'

# get the RSS feed
file_request = urllib2.Request(address)
file_opener = urllib2.build_opener()
file_feed = file_opener.open(file_request).read()
file_xml = minidom.parseString(file_feed) 

# extract item elements
item_node = file_xml.getElementsByTagName("item") 

# check for Phat Thai availability
for item in item_node:

    # extract title and description from XML
    title = item.childNodes[1].firstChild.data 
    description = item.childNodes[5].firstChild.data

    # string matching
    if re.search(restaurant , title.lower()) \
        and re.search(meal, description.lower().rstrip()):

        """The first step is to create an SMTP object, each object is used for connection 
        with one server."""

        # Send email to mailing list

        import smtplib

        server = smtplib.SMTP('smtp.gmail.com', 587)

        fromaddr = 'username@gmail.com'
        toaddr = ['recipient@email.com', 'mailing-list@yahoo.com']

        message = 'Subject: %s\n\n%s' % (subject, text)

        server.starttls()
        server.login('username@gmail.com', 'password')
        server.sendmail(fromaddr, toaddr, message)
        server.quit()


