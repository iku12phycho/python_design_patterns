def builtin_iterator():
  items = [1,2,3]
  for item in items:
    print(item)

def main():
  my_iterator = MyIterator(4,5,6)
  for i in my_iterator:
    print(i)


class MyIterator:
  
  def __init__(self, *numbers) -> None:
      self.numbers = numbers
      self._i = 0
  
  def __iter__(self):
    print('__iter__ is called')
    return self

  def __next__(self):
    print('__next__ is called')
    if self._i == len(self.numbers):
      raise StopIteration()
    current_value = self.numbers[self._i]
    self._i += 1
    return current_value

if __name__ == '__main__':
  main()