" tests of basic makepath functionality"
import sys
sys.path.append('.')
sys.path.append('..')
import os
import unittest
import makepath

class TestBase(unittest.TestCase):
  @classmethod
  def setUp(self):
    ###  code to do setup
    self.olddir = os.getcwd()
    self.tmpdir = os.path.join('/tmp', 'makepathtest.%s' %os.getpid())
    os.system('rm -rf %s' %self.tmpdir)
    os.mkdir(self.tmpdir)
    os.chdir(self.tmpdir)


  def tearDown(self):
    ###  code to do tear down
    os.chdir(self.olddir)
    os.system('rm -rf %s' %self.tmpdir)

  def test_Subdir(self):
    "make a simple directory, relative path"
    self.assertFalse(os.path.isdir('a'))
    makepath.makedirs('a')
    self.assertTrue(os.path.isdir('a'))

  def test_SubdirPath(self):
    "make a full relative path"
    self.assertFalse(os.path.isdir('a/b/c/d'))
    makepath.makedirs('a/b/c/d')
    self.assertTrue(os.path.isdir('a/b/c/d'))

  def test_AbsPath(self):
    "make dir with absolute path"
    dir = os.path.join(os.getcwd(), str(os.getpid()))
    self.assertFalse(os.path.isdir(dir))
    makepath.makedirs(dir)
    self.assertTrue(os.path.isdir(dir))

unittest.main()
