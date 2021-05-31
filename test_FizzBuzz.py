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



if __name__ == '__main__':
    unittest.main()
