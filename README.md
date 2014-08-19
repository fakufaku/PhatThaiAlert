Phat Thai Alert
===============

This is a simple python script reading the [EPFL Restauration](http://restauration.epfl.ch/) 
RSS flux and sends an email to a mailing list whenever there is 
[Phat Thai](https://en.wikipedia.org/wiki/Pad_Thai) at [Hong Thai Rung](http://www.thai-epfl.ch/).

<p><a href="https://commons.wikimedia.org/wiki/File:Phat_Thai_kung_Chang_Khien_street_stall.jpg#mediaviewer/File:Phat_Thai_kung_Chang_Khien_street_stall.jpg"><img alt="Phat Thai kung Chang Khien street stall.jpg" src="https://upload.wikimedia.org/wikipedia/commons/3/39/Phat_Thai_kung_Chang_Khien_street_stall.jpg" height="480" width="480"></a><br>"<a href="https://commons.wikimedia.org/wiki/File:Phat_Thai_kung_Chang_Khien_street_stall.jpg#mediaviewer/File:Phat_Thai_kung_Chang_Khien_street_stall.jpg">Phat Thai kung Chang Khien street stall</a>" by <a href="//commons.wikimedia.org/wiki/User:Takeaway" title="User:Takeaway">Takeaway</a> - <span class="int-own-work">Own work</span>. Licensed under <a title="Creative Commons Attribution-Share Alike 3.0" href="http://creativecommons.org/licenses/by-sa/3.0">CC BY-SA 3.0</a> via <a href="//commons.wikimedia.org/wiki/">Wikimedia Commons</a>.</p>

Run the script automatically
----------------------------

The script is run every week-day at 10 am from a Raspberry Pi with access to the internet.
I simply use `Cron` to do the job. To setup cron, do the following. Type in the command line

    crontab -e

and add the following line to the file

    
    0 10 * * 1-5  python path/to/script/phatthai_alert.py

Replace `path/to/script/` by the actual path to the script. Don't forget to
setup the clock on local time!
