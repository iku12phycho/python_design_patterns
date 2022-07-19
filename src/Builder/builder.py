import abc

def main():
  html = Director().construct(HTMLBuilder())
  text = Director().construct(TextBuilder())
  print(html)
  print("********")
  print(text)

class Director():
  def construct(self, builder):
    all_str = ""
    all_str += builder.build_title("Monthly Report")
    all_str += builder.build_header("-------")
    all_str += builder.build_contents(["Monday: 20", "Tuesday: 30"])
    all_str += builder.build_footer("-*-*-*-")
    return all_str

class AbstractBuilder(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def build_title(self, title):
    pass

  @abc.abstractmethod
  def build_header(self, header):
    pass

  @abc.abstractmethod
  def build_contents(self, contents):
      pass

  @abc.abstractmethod
  def build_footer(self, footer):
      pass

class HTMLBuilder(AbstractBuilder):
  def build_title(self, title):
    return "<h1>{}</h1>\n".format(title)
  
  def build_header(self, header):
        return "<header><p>{}</p></header>\n".format(header)

  def build_contents(self, contents):
      html_contents = []
      for content in contents:
          html_contents.append("<p>{}</p>\n".format(content))
      return "".join(html_contents)

  def build_footer(self, footer):
      return "<footer><p>{}</p></footer>".format(footer)

class TextBuilder(AbstractBuilder):

  def build_title(self, title):
      return "**{}**\n".format(title)

  def build_header(self, header):
      return "{}\n".format(header)

  def build_contents(self, contents):
      text_contents = []
      for content in contents:
          text_contents.append("{}\n".format(content))
      return "".join(text_contents)

  def build_footer(self, footer):
      return "{}".format(footer)

if __name__ == "__main__":
  main()