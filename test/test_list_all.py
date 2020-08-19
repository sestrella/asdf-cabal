from lib.list_all import list_all
from unittest.mock import Mock

import unittest

class TestListAll(unittest.TestCase):
  def test_list_all(self):
    printer = Mock()
    list_all(printer)
    self.assertIn('3.2.0.0', printer.call_args.args[0])

  def test_list_all_not_latest(self):
    printer = Mock()
    list_all(printer)
    self.assertNotIn('latest', printer.call_args.args[0])
