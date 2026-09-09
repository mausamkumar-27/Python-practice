student_database = {
    "st_101": ("Aman", ["Maths", "Physics", "Chemistry"], "85%"),
    "st_102": ("Riya", ["Biology", "Physics"], "N/A"),
    "st_103": ("Kunal", ["Maths", "Computer", "Physics"], "72%"),
    "st_104": ("Pooja", ["Chemistry", "Biology", "English"], "91%"),
    "st_105": ("Vikas", ["History", "English"], "invalid_entry"),
    "st_106": ("Sneha", ["Maths", "Computer", "Chemistry"], "64%")
}
unique_course=set()
for st_id,(name,courses,attendence) in student_database.items():
    unique_course.update(courses)
print(unique_course)
for st_id,(name,courses,attendence) in student_database:
    unique_course.strip("%")

