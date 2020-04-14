import unittest
from calc import calc_me

class CalcTest(unittest.TestCase):
    def test_add(self):
        """Сложение"""
        self.assertEqual(calc_me(1, 2,"+"), 3)
        
    def test_sub(self):
        """Вычитание"""
        self.assertEqual(calc_me(4, 2,"-"), 2)
        
    def test_mul(self):
        """Умножение"""
        self.assertEqual(calc_me(12345679, 8,"*"), 98765432)
        
    def test_div(self):
        """Деление"""
        self.assertEqual(calc_me(111111111, 9,"/"), 12345679)

    def test_exponen(self):
        """Возведение в степень"""
        self.assertEqual(calc_me(7, 2,"^") or (7,2,"**"), 49)

    def test_oper_neg(self):
        """Негативный, недопустимая операция"""
        self.assertEqual(calc_me(7,2,"!&("), "ERROR: Uknow operation")

    def test_div_neg(self):
        """Негативный, деление на ноль"""
        self.assertEqual(calc_me(12, 0,"/"), 'ERROR: Divide by zero!')

    def test_symb_neg(self):
        """Негативный, символы в Num"""
        self.assertEqual(calc_me(4, "!@#$%^") or ("!@#$%^", 3), "ERROR: now it is does not supported")

    def test_num1_none_neg(self):
        """Негативный, отсутствует значение 1"""
        self.assertEqual(calc_me(None,0), "ERROR: send me Number1")

    def test_num2_none_neg(self):
        """Негативный, отсутствует значение 2"""
        self.assertEqual(calc_me(2,None), "ERROR: send me Number2")


if __name__ == '__main__':
    unittest.main(verbosity=2)