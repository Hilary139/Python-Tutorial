
'''
According to Python's standard documentation, the webbrowser module provides a high-level interface to allow
displaying Web-based documents to users. This topic explains and demonstrates proper usage of the webbrowser
module.

'''
import webbrowser
website = webbrowser.open('http://stackoverflow.com')

'''If a browser window is currently open, the method will open a new tab at the specified URL. If no window is open,
the method will open the operating system's default browser and navigate to the URL in the parameter. The open
method supports the following parameters:'''

#* Opening new tab at the specified URL
website_newtab = webbrowser.open_new_tab('http://google.com/')

