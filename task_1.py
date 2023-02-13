number_elements_first_line = int(input("Enter of numbers 1: "))
first_line = []
i = 0

while i < number_elements_first_line:
    r = int(input(":"))
    first_line.append(r)
    i += 1
print(*first_line)

number_elements_second_line = int(input("Enter of numbers 2: "))
second_line = []
i = 0

while i < number_elements_second_line:
    t = int(input(":"))
    second_line.append(t)
    i += 1
print(*second_line)

third_line = []

for item in first_line:
    if item in second_line:
        third_line.append(item)


max_number = max(third_line)
min_number = min(third_line)
print(min_number, max_number)