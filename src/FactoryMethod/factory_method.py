import abc

def main():
  dog = DogFactory()
  dog.animalBehaivor()
  cat = CatFactory()
  cat.animalBehaivor()

# Creator
class Factory:
  def __init__(self):
    self.animal = self.factory_method()

  # template_method
  def animalBehaivor(self):
    self.animal.eat()
    self.animal.speak()

  @abc.abstractmethod
  def factory_method(self):
    pass

# Product
class Animal:
  @abc.abstractmethod
  def eat(self):
    pass

  @abc.abstractmethod
  def speak(self):
    pass

# ConcreteCreator
class DogFactory(Factory):
  def factory_method(self):
    return Dog()

# ConcreteCreator
class CatFactory(Factory):
  def factory_method(self):
    return Cat()

# ConcreteProduct
class Dog(Animal):
  def eat(self):
    print("Dog:eat")

  def speak(self):
    print("Dog:speak")

# ConcreteProduct
class Cat(Animal):
  def eat(self):
    print("Cat:eat")

  def speak(self):
    print("Cat:speak")

if __name__ == "__main__":
  main()