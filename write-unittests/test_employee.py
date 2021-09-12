import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee('Hua', 'Mulan', 50000)
        self.emp_2 = Employee('J', 'Mascis', 60000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Hua.Mulan@email.com')
        self.assertEqual(self.emp_2.email, 'J.Mascis@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Hua Mulan')
        self.assertEqual(self.emp_2.fullname, 'J Mascis')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True   
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('March')
            mocked_get.assert_called_with('http://company.com/Mulan/March')
            self.assertEqual(schedule, 'Success')    

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('November')
            mocked_get.assert_called_with('http://company.com/Mascis/November')
            self.assertEqual(schedule, 'Bad Response!')



    if __name__ == '__main__':
        unittest.main()            

