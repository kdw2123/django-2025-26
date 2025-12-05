def get_grade(student_greads,student_name):
    try :
        grade = student_greads[student_name]
        return f"{student_name} has grade {grade}"
    except KeyError:
        return "syudent not found in the system"
grade = {
    "abebe": "A",
    "KEBEDE": "B",
    "aster": "C",

}
print(get_grade(grade, "aster"))
print(get_grade(grade,"dogu"))

