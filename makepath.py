import os

def makedirs(dir):
  if (not dir) or os.path.isdir(dir):
    return
  dirname = os.path.dirname(dir)
  makedirs(dirname)
  os.mkdir(dir)
