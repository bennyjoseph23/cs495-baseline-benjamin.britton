import pytest
import unittest

class TestStringMethods(unittest.TestCase):

    def test_input(self):
        self.assertEqual(type(getMessage), str)

    def test_isupper(self):
        self.assertEqual(type(getMessage).isupper(), True)
    def test_islower(self):
        self.assertEqual(type(getMessage).islower(), True)
if __name__ == '__main__':
    unittest.main()

def getMessage(input):
    return Str(input(print(input)))

def test_answerIsString(string):
    assert Type(string) is Str

def test_answerIsUpper():
    assert string.isupper()

def test_answerIsLower():
    assert string.islower()

userInput = getMessage("Type something")

print(test_answerIsString(userInput))
print(test_answerIsUpper(userInput))
print(test_answerIsLower(userInput))
