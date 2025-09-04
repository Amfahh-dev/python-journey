(Increment iterations):
i = 15
while i >= -9:
    print(f"Number {i}")
    i -= 1

    (FOR LOOPS):
matrix = []
rows = 3
cols = 4

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j + 1)  # Example value
    matrix.append(row)

for row in matrix:
    print(row)w)

(10s table):
    for i in range(1, 11):  
    for j in range(1, 11):  
        print(f"{i} x {j} = {i*j}")
    print("............")  
