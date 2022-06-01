import unittest
from unittest.mock import MagicMock, patch
from employee_payments import EmployeePayment
from exceptions import DayOfWeekNotFound, InputBadFormat

class TestEmployeePayments(unittest.TestCase):

    @patch('builtins.print')
    def test_output_employee_payment(self, mock_print):
        line_test = 'TEST=MO10:00-12:00,SU20:00-21:00'
        test_ep = EmployeePayment(line_test)
        test_ep.calculate_total_payment()
        test_ep.output_employee_payment()
        mock_print.assert_called_with('The amount to pay TEST is: 55 USD')

    def test_calculate_total_payment(self):
        line_test = 'TEST=MO10:00-12:00'
        test_ep = EmployeePayment(line_test)

        return_value=('TEST', 'MO10:00-12:00')
        test_ep._get_employee_and_schedule = MagicMock(return_value=return_value)
        return_value = (1,'10:00','12:00')
        test_ep._get_day_and_time = MagicMock(return_value=return_value)
        return_value = 30
        test_ep._get_pay_for_day= MagicMock(return_value=30)

        test_ep.calculate_total_payment()

        test_ep._get_employee_and_schedule.assert_called()
        test_ep._get_day_and_time.assert_called()
        test_ep._get_pay_for_day.assert_called()

    def test_day_of_week_not_found(self):
        line_test = 'TEST=MI10:00-12:00'
        test_ep = EmployeePayment(line_test)
        self.assertRaises(DayOfWeekNotFound, test_ep.calculate_total_payment)

    def test_input_bad_format(self):
        line_test = 'TESTMO10:00-12:00'
        test_ep = EmployeePayment(line_test)
        self.assertRaises(InputBadFormat, test_ep.calculate_total_payment)


if __name__ == '__main__':
    unittest.main()
