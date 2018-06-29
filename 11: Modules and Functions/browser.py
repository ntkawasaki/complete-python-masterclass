import webbrowser

# chrome won't open new window
# webbrowser.open("https://python.org/", new=1)

chrome = webbrowser.get(using="chrome")
chrome.open_new("https://www.python.org/")