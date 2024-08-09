file = open("./estudantes.csv")
lines = file.readlines()
students = list(map(lambda x: x.strip("\n").split(","), lines))
students_names = list(map(lambda x: x[0], students))
higher_grades = list(map(lambda student: sorted(list(map(lambda x: int(x), student[1:])), reverse=True)[:3] , students))
means = list(map(lambda x: round(sum(x)/3,2), higher_grades))
all_values = sorted(list(zip(students_names, higher_grades, means)), key= lambda x: x[0], reverse=False)

for value in all_values:
    print(f"Nome: {value[0]} Notas: {value[1]} Média: {value[2]}")
