from datetime import datetime
from exceptions.exceptions import DayOfWeekNotFound, InputBadFormat


DAYS_OF_WEEK = {'MO': 1, 'TU': 2, 'WE': 3, 'TH': 4, 'FR': 5, 'SA': 6, 'SU': 7}


class EmployeePayment():
    """
    Employee Payment to manage information about days worked by employee

    Attributes:
        employee_info: String with employee name and schedule they worked
        employee: employee name
        total_pay: total amount payment
    """
    def __init__(self, employee_info: str):
        """
        Args:
            employee_info (str): employee information with name and
                                 schedule they worked
        """
        self.employee_info = employee_info.strip()
        self._employee = None
        self._total_pay = None

    def _get_pay_for_day(self, day: int, start_time: str, end_time: str) -> int:
        """
        Calculate payment for day based in hours and day that an employee
        worked

        Args:
            day (int): day of week 1 = Monday ... 7 = Sunday
            start_time (str): start time in '%H:%M' format
            end_time (str): end time in '%H:%M' format

        Returns:
            int: payment for hours that they worked in a day
        """
        start_time = datetime.strptime(start_time, '%H:%M')
        end_time = datetime.strptime(end_time, '%H:%M')

        hour_amount = (end_time - start_time).seconds//3600
        start_time = start_time.time()
        end_time = end_time.time()

        first_period = datetime.strptime('00:01', '%H:%M').time()
        second_period = datetime.strptime('09:01', '%H:%M').time()
        third_period = datetime.strptime('18:01', '%H:%M').time()

        pay = 0

        if day > 0 and day < 6:
            if start_time > first_period and end_time < second_period:
                pay = hour_amount*25
            elif start_time > second_period and end_time < third_period:
                pay = hour_amount*15
            else:
                pay = hour_amount*20
        else:
            if start_time > first_period and end_time < second_period:
                pay = hour_amount*30
            elif start_time > second_period and end_time < third_period:
                pay = hour_amount*20
            else:
                pay = hour_amount*25
        return pay

    def calculate_total_payment(self) -> None:
        """
        Calculate total payment for a employee based on day and hours that
        they worked
        """
        self._employee, schedule = self._get_employee_and_schedule()
        total_pay = 0
        for day_hour in schedule:
            day, start_time, end_time = self._get_day_and_time(day_hour)
            pay_amount = self._get_pay_for_day(day, start_time, end_time)
            total_pay += pay_amount
        self._total_pay = total_pay

    def _get_employee_and_schedule(self) -> tuple:
        """
        Get employee and schedule

        Raises:
            InputBadFormat: When input format does not match
                            with EMPLOYEE_NAME=MO10:00-20:00,SU16:00-21:00

        Returns:
            tuple: Employee name and schedule
        """
        employee_info_splitted = self.employee_info.split('=')
        if len(employee_info_splitted) != 2:
            raise InputBadFormat("Input format could not be processed")

        employee = employee_info_splitted[0]
        schedule = employee_info_splitted[1].split(',')
        return employee, schedule

    def _get_day_and_time(self, day_hour: str) -> tuple:
        """
        Get day, start time and end time

        Args:
            day_hour (str): day and hours in this format
                            MO00:00-12:00

        Raises:
            DayOfWeekNotFound: When day of week doest not match
                               with MO,TU,WE,TH,FR,SA,SU
            InputBadFormat:  When input format does not match
                             with EMPLOYEE_NAME=MO10:00-20:00,SU16:00-21:00

        Returns:
            tuple: Tuple of number of day, string of start time and
                    string of end time
        """
        if day_hour[0:2] not in DAYS_OF_WEEK:
            raise DayOfWeekNotFound("Day of week could not be found")

        day = DAYS_OF_WEEK[day_hour[0:2]]
        time_splitted = day_hour[2:].split('-')

        if len(time_splitted) != 2:
            raise InputBadFormat("Input format could not be processed")

        start_time = time_splitted[0]
        end_time = time_splitted[1]
        return day, start_time, end_time

    def output_employee_payment(self) -> None:
        """
        Print message with total amout payment for an employee
        """
        print(f'The amount to pay {self._employee} is: {self._total_pay} USD')


if __name__ == "__main__":
    with open("data/input.txt") as f:
        lines = f.readlines()
        for line in lines:
            employee_payment = EmployeePayment(line)
            employee_payment.calculate_total_payment()
            employee_payment.output_employee_payment()
