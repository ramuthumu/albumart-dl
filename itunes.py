
import requests, sys, pyperclip, bs4, webbrowser
if len(sys.argv) > 1:
    album = ' '.join(sys.argv[1:])
else:
    album = pyperclip.paste()


res = requests.get('https://itunes.apple.com/search?term=%s&entity=album' % (album))
res = res.json()
url = res["results"][0]["artworkUrl100"].replace("100x100","600x600")

webbrowser.open(url)
