from Builder import builder

def test_director_htmlbuilder(capfd):
  html = builder.Director().construct(builder.HTMLBuilder())
  print(html)
  out, err = capfd.readouterr()
  assert out == '<h1>Monthly Report</h1>\n'\
                '<header><p>-------</p></header>\n'\
                '<p>Monday: 20</p>\n'\
                '<p>Tuesday: 30</p>\n'\
                '<footer><p>-*-*-*-</p></footer>\n'

def test_director_textbuilder(capfd):
  text = builder.Director().construct(builder.TextBuilder())
  print(text)
  out, err = capfd.readouterr()
  assert out == '**Monthly Report**\n'\
                '-------\n'\
                'Monday: 20\n'\
                'Tuesday: 30\n'\
                '-*-*-*-\n'