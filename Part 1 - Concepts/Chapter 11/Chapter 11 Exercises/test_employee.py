import pytest
from employee import Employee


@pytest.fixture
def employee_salary_raise():
    """Employee object that will be able to all the tests."""
    employee1 = Employee("Abdul", "Basit", 2360)
    return employee1


def test_give_default_raise(employee_salary_raise):
    """Test whether giving a default raise of $5000 works correctly."""
    increment = employee_salary_raise.give_raise()
    assert increment == 5000


def test_give_custom_raise(employee_salary_raise):
    """Test whether giving a custom raise works correctly."""
    increment = employee_salary_raise.give_raise(1000)
    assert increment == 1000
