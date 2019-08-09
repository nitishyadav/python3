#launching web browsers using python
import webbrowser
import subprocess

url = 'https://www.gmail.com'
#webbrowser.open('http://google.co.kr', new=2)

webbrowser.get('safari').open_new(url)