from lib.install import install

import subprocess
import tempfile
import unittest

class TestInstall(unittest.TestCase):
  def test_install_3x(self):
    with tempfile.TemporaryDirectory() as install_dir:
      install(install_dir, '3.2.0.0')
      output = subprocess.check_output([f'{install_dir}/bin/cabal', '--version'])
      self.assertIn(b'3.2.0.0', output)

  def test_install_2x(self):
    with tempfile.TemporaryDirectory() as install_dir:
      install(install_dir, '2.4.1.0')
      output = subprocess.check_output([f'{install_dir}/bin/cabal', '--version'])
      self.assertIn(b'2.4.1.0', output)
