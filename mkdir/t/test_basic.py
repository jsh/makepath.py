" tests of basic makepath functionality"
import sys
sys.path.append('.')
sys.path.append('..')
import os
import unittest
import makepath
import xmlrunner

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
    dirname = os.path.join(os.getcwd(), str(os.getpid()))
    self.assertFalse(os.path.isdir(dirname))
    makepath.makedirs(dirname)
    self.assertTrue(os.path.isdir(dirname))

  def test_DirWithBlanks(self):
    "make dir with embedded blanks"
    self.assertFalse(os.path.isdir('hello world'))
    makepath.makedirs('hello world')
    self.assertTrue(os.path.isdir('hello world'))

  def test_MultipleDirs(self):
    "make a list of directories"
    for dirname in 'a','b','c','d':
      self.assertFalse(os.path.isdir(dirname))

    makepath.makedirs('a','b','c','d')

    for dirname in 'a','b','c','d':
      self.assertTrue(os.path.isdir(dirname))

unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
