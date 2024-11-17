from employee_info import employee_data,get_employees_by_age_range,calculate_average_salary,get_employees_by_dept

def test_get_employees_by_age_range():
    tested_data = get_employees_by_age_range(20, 30)
    expected_data =[{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},{"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert(tested_data ==expected_data)

def test_calculate_average_salary():
    expected_data=((50000+60000+56000+70000+65000+60000)/6)
    tested_data= calculate_average_salary()
    #tested_data = employee_info.calculate_average_salary()
    assert(tested_data == expected_data)

def test_get_employees_by_dept():
    tested_data=get_employees_by_dept('Marketing')
    expected_data=[{"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}]
    assert(tested_data == expected_data)