import unittest

class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        # tu código aquí
        self.result = self.result + num
        for n in nums:
            #print(v)
            self.result = self.result + n
        return self
    def subtract(self, num, *nums):
        self.result = self.result - num
        for n in nums:
            #print(v)
            self.result = self.result - n
        return self
md = MathDojo()
#md2 = MathDojo()

class mathDojoTest(unittest.TestCase):
    def testUno(self):
        #self.assertEqual(md.add(2,5,1).result, 8)
        self.assertTrue(md.add(2,5,1).result==8)
    def testDos(self):
        self.assertEqual(md.subtract(3,2).result, -5)

    def setUp(self):
        md.result=0
        print(md.result, "Desde SETUP")

    def tearDown(self):
        print("Prueba")
if __name__ == '__main__':
    unittest.main()