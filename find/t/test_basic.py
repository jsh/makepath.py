" tests of basic functionality"

import sys
sys.path.append('.')
sys.path.append('..')
import os
import unittest
import find
import xmlrunner

class TestBase(unittest.TestCase):
  @classmethod
  def setUp(self):
    ###  code to do setup
    self.olddir = os.getcwd()
    self.tmpdir = os.path.join('/tmp', 'findtest.%s' %os.getpid())
    os.system('rm -rf %s' %self.tmpdir)
    os.mkdir(self.tmpdir)
    os.chdir(self.tmpdir)


  def tearDown(self):
    ###  code to do tear down
    os.chdir(self.olddir)
    os.system('rm -rf %s' %self.tmpdir)

  #def test_Subdir(self):
  #  "make a simple directory, relative path"
  #  self.assertFalse(os.path.isdir('a'))
  #  makepath.makedirs('a')
  #  self.assertTrue(os.path.isdir('a'))

unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
