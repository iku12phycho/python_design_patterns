from Adapter import adapter

def test_htmlwriter_out_header(capfd):
  htmlwriter = adapter.HtmlWriter()
  htmlwriter.out_header()
  out, err = capfd.readouterr()
  assert out == '<!DOCTYPE HTML>\n<html>\n'

def test_htmlwriter_out_title(capfd):
  htmlwriter = adapter.HtmlWriter()
  text = 'test'
  htmlwriter.out_title(text)
  out, err = capfd.readouterr()
  assert out == '<head><title>test</title></head>\n'

def test_htmlwriter_out_start_body(capfd):
  htmlwriter = adapter.HtmlWriter()
  htmlwriter.out_start_body()
  out, err = capfd.readouterr()
  assert out == '<body>\n'

def test_htmlwriter_out_body(capfd):
  htmlwriter = adapter.HtmlWriter()
  texts = ['test0', 'test1']
  htmlwriter.out_body(texts)
  out, err = capfd.readouterr()
  assert out == '<p>test0</p>\n<p>test1</p>\n'

def test_htmlwriter_out_end_body(capfd):
  htmlwriter = adapter.HtmlWriter()
  htmlwriter.out_end_body()
  out, err = capfd.readouterr()
  assert out == '</body>\n'

def test_htmlwriter_out_footer(capfd):
  htmlwriter = adapter.HtmlWriter()
  htmlwriter.out_footer()
  out, err = capfd.readouterr()
  assert out == '</html>\n'

def test_plaintextreporter_header(capfd):
  plaintextreporter = adapter.PlainTextReporter()
  text = 'test'
  plaintextreporter.header(text)
  out, err = capfd.readouterr()
  assert out == '**test**\n'

def test_plaintextreporter_main(capfd):
  plaintextreporter = adapter.PlainTextReporter()
  texts = ['test0', 'test1']
  plaintextreporter.main(texts)
  out, err = capfd.readouterr()
  assert out == 'test0\ntest1\n'

def test_htmlreporter_header(capfd):
  htmlreporter = adapter.HtmlReporter()
  text = 'test'
  htmlreporter.header(text)
  out, err = capfd.readouterr()
  assert out == '<!DOCTYPE HTML>\n<html>\n'\
                '<head><title>test</title></head>\n'\
                '<body>\n'

def test_htmlreporter_main(capfd):
  htmlreporter = adapter.HtmlReporter()
  texts = ['test0', 'test1']
  htmlreporter.main(texts)
  out, err = capfd.readouterr()
  assert out == '<p>test0</p>\n<p>test1</p>\n'

def test_htmlreporter_footer(capfd):
  htmlreporter = adapter.HtmlReporter()
  htmlreporter.footer()
  out, err = capfd.readouterr()
  assert out == '</body>\n</html>\n'