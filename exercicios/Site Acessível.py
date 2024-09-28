import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/playlist?list=PLjBY7MkpJQuXc7gtNsDSTtN9FmYXn377M')
except urllib.error.URLError:
    print('Sua playlist de músicas não está acessível no momento')
else:
    print('Consegui acessar a playlist Músicas')
