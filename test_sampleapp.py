from sampleapp import max1

def test_max1():
   assert max1(1,-15)==1
   assert max1(0,15)==15
   assert max1(10,10)==10
