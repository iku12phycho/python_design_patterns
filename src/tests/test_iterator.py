from Iterator import iterator

def test_builtin_iterator(capfd):
  iterator.builtin_iterator()
  out, err = capfd.readouterr()
  assert out == '1\n2\n3\n'

def test_main(capfd):
  iterator.main()
  out, err = capfd.readouterr()
  assert out == '__iter__ is called\n'\
                '__next__ is called\n'\
                '4\n'\
                '__next__ is called\n'\
                '5\n'\
                '__next__ is called\n'\
                '6\n'\
                '__next__ is called\n'