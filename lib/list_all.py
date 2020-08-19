import gzip
import re
import urllib.request

URL = 'https://downloads.haskell.org/~cabal/'

def list_all(printer = print):
  printer(' '.join(__extract_versions(__downloads_index())))

def __extract_versions(html):
  return filter(
    lambda version: version != 'latest',
    re.findall('(?<=href="cabal-install-)(.*)(?=/")', html)
  )

def __downloads_index():
  with urllib.request.urlopen(URL) as resp:
    return gzip.decompress(resp.read()).decode('utf-8')

if __name__ == '__main__':
  list_all()
