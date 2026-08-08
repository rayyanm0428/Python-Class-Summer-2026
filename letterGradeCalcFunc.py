def letterGrade(grades):
    max = len(student1)
    total = 0
    for i in range(max):
        total += grades[i]
    average = total/max
    if average >= 89.5:
        return "A"
    elif average >= 79.5:
        return "B"
    elif average >= 69.5:
        return "C"
    elif average >=59.5:
        return "D"
    else:
        return "F"
student1 = [70,86,82,93,73,87]
student2 = [90,91,98,78,82,99]
print(letterGrade(student2))