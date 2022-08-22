from Singleton import singleton

def test_FactoryConfig_noParam():
  factoryConfig = singleton.FactoryConfig()
  assert "INFO" == factoryConfig.log_level

def test_FactoryConfig():
  factoryConfig = singleton.FactoryConfig(log_level="DEBUG")
  assert "INFO" == factoryConfig.log_level

def test_FactoryA_show_config():
  factoryConfig = singleton.FactoryConfig()
  factoryA = singleton.FactoryA(factoryConfig)
  assert "INFO" == factoryA.show_config().log_level

def test_FactoryB_show_config():
  factoryConfig = singleton.FactoryConfig(log_level="DEBUG")
  factoryB = singleton.FactoryB(factoryConfig)
  assert "INFO" == factoryB.show_config().log_level

def test_FactoryConfig_singleton():
  factoryConfigA = singleton.FactoryConfig()
  factoryA = singleton.FactoryA(factoryConfigA)

  factoryConfigB = singleton.FactoryConfig(log_level="DEBUG")
  factoryB = singleton.FactoryB(factoryConfigB)

  assert factoryConfigA == factoryConfigB
  assert factoryA != factoryB