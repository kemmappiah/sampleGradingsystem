import pandas as pd

print("""
            TINY GEM SCHOOL, TEMA
                GRADING SYSTEM
                
Enter your name and the marks obtained in all subjects. 
The system will generate your grades for you.
""")

subjects = ["Mathematics", "English Language", "General Science", "Social Studies", "Vocational Skills", "French",
            "Ghanaian Lang", "Technical Skills"]
marks_keeper = []
grades_keeper = []
total_marks = int(0)


def grading(marks):
    if marks >= 90: 
        return "A"
    elif marks >= 80: 
        return "B"
    elif marks >= 70: 
        return "C"
    elif marks >= 60: 
        return "D"
    elif marks >= 50: 
        return "E"
    else: 
        return "F"
        

student_name = input("Please enter your name: ")
for i in subjects:
    print(i)
    score = int(input("Score: "))
    marks_keeper.append(score)
    grade = grading(score)
    grades_keeper.append(grade)
    total_marks = total_marks + score
 
dataset = {
    "SUBJECTS": subjects,
    "MARKS": marks_keeper,
    "GRADES": grades_keeper
}

final_output = pd.DataFrame(dataset) 
print("\nBelow are your grades", "\n", final_output, "\n", "\nTOTAL SCORE IS ", total_marks, "/800", "\nTHANK YOU")
