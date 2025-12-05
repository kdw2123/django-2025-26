score = {
    "jone":85,
    "sara":92,
    "fraol":78
}
name = input("enter the student name : ")
try:
    print(f"the student score is : {score[name]}")
except KeyError:
    print("student not found ")