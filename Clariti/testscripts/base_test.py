import pytest


@pytest.mark.usefixtures("getDriver", "getDriver1")
class BaseTest:
    pass


@pytest.mark.usefixtures("getDriver", "getDriver1", "getDriver2")
class BaseTest3:
    pass


@pytest.mark.usefixtures("getDriver")
class BaseTest1:
    pass
