# Gumawa ng list,tuple at dictionary para mag-imbak ng impormasyon ng mga estudyante
Students_List = []
Grades_Tuple = []
Student_Records = {}
for i in range(3):
  name = input(f"Enter Student {1+i} name:")
  Students_List.append(name)
for name in Students_List:
    print(f"Enter {name} grades in Biology, Chemistry,Physics:")
    Grades_Input = input() # Kumuha ng input galing sa user
    Grades = Grades_Input.split() # I-split ang input sa isang list ng string
    Biology_Grade = int(Grades[0])
    Chemistry_Grade = int(Grades[1])
    Physics_Grade = int(Grades[2])
    Grades_Tuple.append(( Biology_Grade,  Chemistry_Grade, Physics_Grade))
# I-imbak ang impormasyon ng mga estudyante sa dictionary
for i, name in enumerate(Students_List):
    Student_Records[name] = Grades_Tuple[i]
# I-print ang student records na parang isang talahanayan
print("-"*40)
print("Student Names Biology Chemistry Physics")
print("-"*40)
# Ulitin ang Student_Records dictionary
for name, grades in Student_Records.items():
    print(f"{name:<15}  {grades[0]:>3}  {grades[1]:>4}  {grades[2]:>7}") 
print("-"*40)
# Kunin ang Unique Subjects Offered
Subject_Set = set()
for i in range(3):
    subject = input(f"Enter subject {i+1}:")
    Subject_Set.add(subject)
print("Unique Subjects offered:")
for subject in Subject_Set:
    print("-" + subject)

    
