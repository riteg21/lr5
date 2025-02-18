def analyze_grades(main_grades, secondary_grades):


    fail_resitters = []
    absent_students = []

    for surname, grade in secondary_grades.items():
        if surname in main_grades:  
            if main_grades[surname] == 2 and grade > 2: 
                fail_resitters.append(surname)
        else: 
            absent_students.append(surname)

    return fail_resitters, absent_students


main_grades = {
    "Иванов": 5,
    "Петров": 2,
    "Сидоров": 3,
    "Кузнецов": 4,
    "Смирнов": 2
}

secondary_grades = {
    "Петров": 4,
    "Смирнов": 3,
    "Соколов": 5,
    "Михайлов": 4
}

fail_resitters, absent_students = analyze_grades(main_grades, secondary_grades)

print("Студенты, пересдавшие 'двойку':", fail_resitters)
print("Студенты, не явившиеся на основной экзамен:", absent_students)