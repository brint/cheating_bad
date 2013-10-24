cheating bad
============
This is an app to test leveraging [Selenium](http://www.seleniumhq.org/)
to emulate manually playing [Clicking Bad](http://clickingbad.nullism.com/).
This simple [Python](http://python.org/) script that currently just cooks
and sells.  The script allows for a user to interact with the game and will
rescue any failures with a 5 second sleep, and then it'll scroll back to the
top of the window and start cooking again.  
  
Chrome is used due to it's superior performance versus Firefox.  If you don't
believe me, run them side by side and you'll see Chrome smoke Firefox.

Requirements
============
* [Google Chrome](https://www.google.com/chrome)
* [ChromeDriver](http://chromedriver.storage.googleapis.com/index.html?path=2.4/)
* [Python pip](https://pypi.python.org/pypi/pip)

Getting Started
===============
```
git clone 
pip install -r requirements.txt
python bad.py
```
