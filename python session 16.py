            FOR AND WHILE LOOP WORK PYTHON PRO
                      APTECH PAKISTAN

FIRST PROGRAM:

employees = [
    {'id': 1, 'name': 'Alice',   'position': 'developer', 'salary': 70000},
    {'id': 2, 'name': 'Amfahh',  'position': 'manager',   'salary': 90000},
    {'id': 3, 'name': 'Alya',    'position': 'designer',  'salary': 65000},
    {'id': 4, 'name': 'Kamran',  'position': 'ceo',       'salary': 120000},
    {'id': 5, 'name': 'Eve',     'position': 'intern',    'salary': 30000},
]

print("Program 1: All Employee Records")
print("------------------------------")
for emp in employees:
    print(f"ID: {emp['id']}, Name: {emp['name']}, Position: {emp['position']}, Salary: ${emp['salary']}")

SECONED PROGRAM:


for emp in employees:
    if emp['position'] == 'manager' or emp['position'] == 'ceo':
        continue
    print(f"ID: {emp['id']}, Name: {emp['name']}, Position: {emp['position']}, Salary: ${emp['salary']}")

THIRD PROGRAM:


salaries = [emp['salary'] for emp in employees]

highest = salaries[0]
lowest = salaries[0]

for salary in salaries:
    if salary > highest:
        highest = salary
    if salary < lowest:
        lowest = salary

print("Program 3: Highest and Lowest Salary")
print("------------------------------------")

for emp in employees:
    if emp['salary'] == highest:
        print(f"Highest Salary:")
        print(f"ID: {emp['id']}, Name: {emp['name']}, Position: {emp['position']}, Salary: ${emp['salary']}")

for emp in employees:
    if emp['salary'] == lowest:
        print(f"\nLowest Salary:")
        print(f"ID: {emp['id']}, Name: {emp['name']}, Position: {emp['position']}, Salary: ${emp['salary']}")
