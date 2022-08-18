from FactoryMethod import factory_method

def test_DogFactory_factory_method():
  dogFactory = factory_method.DogFactory()
  dog = dogFactory.factory_method()
  assert type(dogFactory) is factory_method.DogFactory
  assert type(dog) is factory_method.Dog

def test_DogFactory_animalBhaivor(capfd):
  dogFactory = factory_method.DogFactory()
  dogFactory.animalBehaivor()
  out, err = capfd.readouterr()
  assert out == 'Dog:eat\n'\
                'Dog:speak\n'

def test_CatFactory_factory_method():
  catFactory = factory_method.CatFactory()
  cat = catFactory.factory_method()
  assert type(catFactory) is factory_method.CatFactory
  assert type(cat) is factory_method.Cat

def test_CatFactory_animalBhaivor(capfd):
  catFactory = factory_method.CatFactory()
  catFactory.animalBehaivor()
  out, err = capfd.readouterr()
  assert out == 'Cat:eat\n'\
                'Cat:speak\n'

def test_Dog_eat(capfd):
  dog = factory_method.Dog()
  dog.eat()
  out, err = capfd.readouterr()
  assert out == 'Dog:eat\n'

def test_Dog_speak(capfd):
  dog = factory_method.Dog()
  dog.speak()
  out, err = capfd.readouterr()
  assert out == 'Dog:speak\n'

def test_Cat_eat(capfd):
  cat = factory_method.Cat()
  cat.eat()
  out, err = capfd.readouterr()
  assert out == 'Cat:eat\n'

def test_Cat_speak(capfd):
  cat = factory_method.Cat()
  cat.speak()
  out, err = capfd.readouterr()
  assert out == 'Cat:speak\n'