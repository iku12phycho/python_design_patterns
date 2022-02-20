import abc
import sys

#adaptee
class HtmlWriter:
  def __init__(self) -> None:
      pass
  
  def out_header(self) -> None:
    print('<!DOCTYPE HTML>', '<html>', sep='\n')
  
  def out_title(self, title) -> None:
    print(f'<head><title>{title}</title></head>')
  
  def out_start_body(self) -> None:
    print("<body>")
  
  def out_body(self, texts) -> None:
    for text in texts:
      print(f'<p>{text}</p>')
  
  def out_end_body(self) -> None:
    print("</body>")
  
  def out_footer(self) -> None:
    print("</html>")

#Target
class Reporter(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def header(self, title) -> None:
    pass

  @abc.abstractmethod
  def main(self, contents) -> None:
    pass

  @abc.abstractmethod
  def footer(self):
    pass

class PlainTextReporter(Reporter):
  def __init__(self) -> None:
    pass

  def header(self, title) -> None:
    print(f'**{title}**')

  def main(self, texts) -> None:
    for text in texts:
      print(text)
  
  def footer(self) -> None:
    pass

#Adapter 継承
class HtmlReporter(Reporter, HtmlWriter):
  def __init__(self) -> None:
    pass
  
  def header(self, title) -> None:
    self.out_header()
    self.out_title(title)
    self.out_start_body()
  
  def main(self, texts) -> None:
    self.out_body(texts)
  
  def footer(self):
    self.out_end_body()
    self.out_footer()

#Adapter 委譲
class HtmlReporter(Reporter):
  def __init__(self) -> None:
    self._htmlwriter = HtmlWriter()
  
  def header(self, title):
    self._htmlwriter.out_header()
    self._htmlwriter.out_title(title)
    self._htmlwriter.out_start_body()

  def main(self, texts):
    self._htmlwriter.out_body(texts)

  def footer(self):
    self._htmlwriter.out_end_body()
    self._htmlwriter.out_footer()

def main() -> None:
  title = "Monthly Report"
  texts = ["good", "best"]

  pr = PlainTextReporter()
  pr.header(title)
  pr.main(texts)
  pr.footer()

  print("\n\n")

  hr = HtmlReporter()
  hr.header(title)
  hr.main(texts)
  hr.footer()

if __name__ == '__main__':
  main()