def calculate_grades(student_filename,grade_filename):
    students_file = open(student_filename, "r")
    grade_file = open(grade_filename, "r")
    students = students_file.readlines()
    grades = grade_file.readlines()
    avg_list = []
    for line in range(len(students)):
        student = students[line].replace("\n", "")
        student_grade = grades[line]
        grade_list = student_grade.split(" ")
        grade_sum = 0
        for grade_item in grade_list:
            grade_sum += float(grade_item)
            grade_avg = grade_sum / len(grade_list)
        avg_list.append(f"{student}: {grade_avg}\n")
    avg_file = open("student_grades.txt", "w")
    avg_file.writelines(avg_list)
    avg_file.close()
def main():
    calculate_grades("names.txt","grades.txt")
main()