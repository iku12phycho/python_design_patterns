import sys

def main():
  Test1().test()
  Test2().test()

class TestFrame:
  def __init__(self) -> None:
      self.counter = 0
    
  def test(self):
    self.setup()
    try:
      self.main()
    except AssertionError:
      self.counter += 1
      sys.stderr.write("E => {}\n".format(self.__class__.__name__))
    if self.counter == 0:
      sys.stderr.write(". => {}\n".format(self.__class__.__name__))
    self.teardown()
    
  def setup(self):
    pass

  def main(self):
    pass

  def teardown(self):
    pass

  def printMethodName(self, methodName):
    print("{} class {} method".format(self.__class__.__name__, methodName))

class Test1(TestFrame):
  def setup(self):
    self.printMethodName(sys._getframe().f_code.co_name)
  
  def main(self):
    self.printMethodName(sys._getframe().f_code.co_name)
    assert 1 == 1
  
  def teardown(self):
    self.printMethodName(sys._getframe().f_code.co_name)

class Test2(TestFrame):
  def setup(self):
    self.printMethodName(sys._getframe().f_code.co_name)
  
  def main(self):
    self.printMethodName(sys._getframe().f_code.co_name)
    assert 1 == 3
  
  def teardown(self):
    self.printMethodName(sys._getframe().f_code.co_name)

if __name__ == '__main__':
  main()