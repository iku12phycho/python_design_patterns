from TemplateMethod import template_method

def test_TestFrame__init__():
  testFrame = template_method.TestFrame()
  assert testFrame.counter == 0

def test_TestFrame__test(capfd):
  testFrame = template_method.TestFrame()
  testFrame.test()
  out, err = capfd.readouterr()
  assert err == '. => TestFrame\n'

def test_TestFrame_printMethodName(capfd):
  testFrame = template_method.TestFrame()
  methodName = 'test'
  testFrame.printMethodName(methodName=methodName)
  out, err = capfd.readouterr()
  assert out == 'TestFrame class test method\n'

def test_Test1_setup(capfd):
  test1 = template_method.Test1()
  test1.setup()
  out, err = capfd.readouterr()
  assert out == 'Test1 class setup method\n'

def test_Test1_main(capfd):
  test1 = template_method.Test1()
  test1.main()
  out, err = capfd.readouterr()
  assert out == 'Test1 class main method\n'
  assert err == ''

def test_Test1_teardown(capfd):
  test1 = template_method.Test1()
  test1.teardown()
  out, err = capfd.readouterr()
  assert out == 'Test1 class teardown method\n'

def test_Test1_test(capfd):
  test1 = template_method.Test1()
  test1.test()
  out, err = capfd.readouterr()
  assert out == 'Test1 class setup method\n'\
                'Test1 class main method\n'\
                'Test1 class teardown method\n'
  assert err == '. => Test1\n'

def test_Test2_setup(capfd):
  test2 = template_method.Test2()
  test2.setup()
  out, err = capfd.readouterr()
  assert out == 'Test2 class setup method\n'

# def test_Test2_main(capfd):
#   test2 = template_method.Test2()
#   test2.main()
#   out, err = capfd.readouterr()
#   assert out == 'Test2 class main method\n'
#   assert err == ''

def test_Test2_teardown(capfd):
  test2 = template_method.Test2()
  test2.teardown()
  out, err = capfd.readouterr()
  assert out == 'Test2 class teardown method\n'

def test_Test2_test(capfd):
  test2 = template_method.Test2()
  test2.test()
  out, err = capfd.readouterr()
  assert out == 'Test2 class setup method\n'\
                'Test2 class main method\n'\
                'Test2 class teardown method\n'
  assert err == 'E => Test2\n'