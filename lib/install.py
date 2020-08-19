import os
import platform
import re
import shutil
import sys
import tarfile
import tempfile
import urllib.request

URL = 'https://downloads.haskell.org/~cabal/'

def install(install_dir, version):
  filename = next(__compatible_filenames(__extract_filenames(__version_index(version))))
  __install_from_url(install_dir, f'{URL}cabal-install-{version}/{filename}')

def __compatible_filenames(filenames):
  ffilter = __filename_filter()
  return filter(
    lambda filename: ffilter in filename and filename.endswith('tar.xz'),
    filenames
  )

def __filename_filter():
  osname = sys.platform
  arch = platform.machine()
  if osname == 'linux':
    return f'{arch}-unknown-{osname}'

  return f'{arch}-apple-{osname}'

def __extract_filenames(html):
  return re.findall('(?<=href=")(cabal-install-.*)(?=")', html)

def __version_index(version):
  with urllib.request.urlopen(f'{URL}cabal-install-{version}') as resp:
    return resp.read().decode('utf-8')

def __install_from_url(install_dir, url):
  with tempfile.TemporaryDirectory() as download_dir:
    path, _ = urllib.request.urlretrieve(url, f'{download_dir}/cabal-install.tar.xz')
    with tarfile.open(path) as tar:
      tar.extractall(download_dir)
      os.mkdir(f'{install_dir}/bin')
      shutil.copy(f'{download_dir}/cabal', f'{install_dir}/bin/cabal')
