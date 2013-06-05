import unittest

from tests.test_client import TestClient
from tests.test_handler import TestRedis
from tests.test_pool import TestPool

TEST_MODULES = [
    "test_client",
    "test_handler",
    "test_pool",
]

def all_tests():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestClient))
    suite.addTest(unittest.makeSuite(TestRedis))
    suite.addTest(unittest.makeSuite(TestPool))
    return suite
