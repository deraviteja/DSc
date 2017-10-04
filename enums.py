from enum import Enum


class Test(Enum):
    success = 0
    failure = 1
    tie = 2


print Test.success.value
