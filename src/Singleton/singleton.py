class SingletonMeta(type):
  _instances = {}

  def __call__(cls, *args, **kwds):
    if cls not in cls._instances:
      instance = super().__call__(*args, **kwds)
      cls._instances[cls] = instance
    return cls._instances[cls]

class FactoryConfig(metaclass=SingletonMeta):
  def __init__(self, log_level="INFO"):
    self.log_level = log_level

class FactoryA:
  def __init__(self, config):
    self.config = config

  def show_config(self):
    return self.config

class FactoryB:
  def __init__(self, config):
    self.config = config

  def show_config(self):
    return self.config

def main():
  configA = FactoryConfig(log_level="DEBUG")
  factoryA = FactoryA(configA)
  print(vars(factoryA.show_config()))

  configB = FactoryConfig(log_level="WARNING")
  factoryB = FactoryB(configB)
  print(vars(factoryB.show_config()))

if __name__ == "__main__":
  main()