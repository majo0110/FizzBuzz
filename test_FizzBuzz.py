import unittest
from unittest.mock import patch
import FizzBuzz
from io import StringIO

class TestCaseFizzBuzz(unittest.TestCase):
    #Test if the numbers printed are from 1-100 excluding multiples of 3 and 5
    def test_printedNum(self):
        with patch('sys.stdout', new = StringIO()) as printedNum:
            FizzBuzz.FizzBuzz()
            testedVal = ""
            for i in range(1,101):
                if( (i % 3 == 0) or (i % 5 == 0)):
                    pass
                else:
                    testedVal += str(i)
            result = (printedNum.getvalue()).replace('\n','')
            result = result.replace('Fizz','')
            result = result.replace('Buzz','')

            self.assertEqual(result, testedVal)

    #Test if the numbers printed are from 1-100
    # if it is a multiple of 3 then print Fizz
    # If it is a multiple of 5 then print buzz
    # If multiple of 3 and 5 then pritn FizzBuzz
    def test_program(self):
        with patch('sys.stdout', new = StringIO()) as printedNum:
            FizzBuzz.FizzBuzz()
            testedVal = ""
            for i in range(1,101):
                if( (i % 3 == 0) and (i % 5 == 0)):
                    testedVal += "FizzBuzz"
                elif (i % 3 == 0):
                    testedVal += "Fizz"
                elif (i % 5 == 0):
                    testedVal += "Buzz"
                else:
                    testedVal += str(i)
            result = (printedNum.getvalue()).replace('\n','')

            self.assertEqual(result, testedVal)


if __name__ == '__main__':
    unittest.main()
