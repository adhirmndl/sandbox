'''
whatTime
takes an int, seconds
returns a String "<H>:<M>:<S>"
<H> : hours
<M> : minutes
<S> : seconds
'''

def whatTime(seconds):
  m = seconds / 60
  H = seconds / (60*60)
  M = m - (H * 60)
  S = seconds - m * 60
  return str(H) + ':' + str(M) + ':' + str(S)

import unittest

class Tester(unittest.TestCase):
  def test0(self):
    self.assertEqual('0:0:0', whatTime(0))
  def test3661(self):
    self.assertEqual('1:1:1', whatTime(3661))
  def test5436(self):
    self.assertEqual('1:30:36', whatTime(5436))
  def test86399(self):
    self.assertEqual('23:59:59', whatTime(86399))

if __name__ == '__main__':
  unittest.main()
