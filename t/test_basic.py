import sys
sys.path.append('..')
import os
import unittest
import makepath

class testBase(unittest.TestCase):
  @classmethod
  def setUp(self):
    ###  code to do setup
    self.tmpdir = os.path.join('/tmp', 'makepathtest.%s' %os.getpid())
    os.system('rm -rf %s' %self.tmpdir)
    os.mkdir(self.tmpdir)
    os.chdir(self.tmpdir)

  def tearDown(self):
    ###  code to do tear down
    os.system('rm -rf %s' %self.tmpdir)

  def test_Basic(self):
    ###  A test case
    self.assertFalse(os.path.isdir('a'))
    makepath.makedirs('a')
    self.assertTrue(os.path.isdir('a'))

unittest.main()
