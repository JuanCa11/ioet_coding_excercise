# IOET Coding Excercise
[![Python 3.8](https://img.shields.io/badge/python-3.8-green.svg)](https://www.python.org/downloads/release/python-380/)
## Context

The company ACME offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

**1. Monday - Friday**
  * 00:01 - 09:00 25 USD
  * 09:01 - 18:00 15 USD
  * 18:01 - 00:00 20 USD

**2. Saturday and Sunday**
  * 00:01 - 09:00 30 USD
  * 09:01 - 18:00 20 USD
  * 18:01 - 00:00 25 USD

The goal of this exercise is to calculate the total that the company has to pay an employee, based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

* MO: Monday
* TU: Tuesday
* WE: Wednesday
* TH: Thursday
* FR: Friday
* SA: Saturday
* SU: Sunday

### Input:

The name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

### Output:

Indicate how much the employee has to be paid

### For example:

* Case 1:

  ```
  INPUT

  RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00

  OUTPUT:

  The amount to pay RENE is: 215 USD
  ```

* Case 2:
  
  ```
  INPUT

  ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00

  OUTPUT:

  The amount to pay ASTRID is: 85 USD
  ```
## Coding solution

#### 1. Code structure

```bash
├── data
│   └── input.txt
├── employee_payments.py
├── exceptions.py
└── test_employee_payments.py
```

* ```data/input.txt``` File with 5 test cases and is a folder if new data could be included.
* ```employee_payments.py``` Python file with main logic to run test cases.
* ```exceptions.py``` Python file with custom exceptions.
* ```test_employee_payments.py``` Python file with unit test cases.

#### 2. Relevant code

A class was created to mmanage instance for every employee and all about employee and payment information. ```employee``` and ```total_pay``` variables were created to be used to print message.

```python
class EmployeePayment():
  def __init__(self, employee_info: str):
    self.employee_info = employee_info.strip()
    self._employee = None
    self._total_pay = None
```

A function was created to calculate total payment, internal functions to split, treat and extract data were created most important thing is a dictionary that cast two letters of day to a number.

```python
def calculate_total_payment(self) -> None:
```
```python
DAYS_OF_WEEK = {'MO': 1, 'TU': 2, 'WE': 3, 'TH': 4, 'FR': 5, 'SA': 6, 'SU': 7}
```

A function to calculate pay for day checking day and hours worked was created as relevant information about it, ```datetime``` library was used to manage format ```%H:%M``` and calculate timedelta.

```python
def _get_pay_for_day(self, day: int, start_time: str, end_time: str) -> int:
```

A function to print message as expected output was built.

```python
def output_employee_payment(self):
```

## Running code

To run the code and cases.

```bash
python employee_payments.py
```

To run unit test cases.

```
python -m unittest
```
