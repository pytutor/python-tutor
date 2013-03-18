# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 10:36:36 2013

@author: Peter
"""
import numpy as np

def gauss1d(x=None,x0=None,sig=None):
  if x == []:
      print('vector of x values is undefined')
      return(0)
  if x0 == None:
      x0 = np.array([-1,1])
  if sig == None:
      sig = np.array([0.5,1])
  
  if len(x0) != len(sig):
    print('x0 and sigma must have the same length')

  
  n = len(x0)
  g = np.zeros((np.shape(x)))
  
  for k in np.arange(len(x0)):
      g = g + 1/(np.sqrt(2*np.pi)*sig[k])*np.exp(-(x-x0[k])**2/(2*sig[k]**2))

  
  g = g / n
  return(g)