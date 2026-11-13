"""sentence="python is great and python is easy to learn because python is powerful"
sentence_list=sentence.split(" ")
#print(sentence_list)
my_dict= {i:sentence_list.count(i)  for i in sentence_list }
print(my_dict)"""

students = [
    {"name": "Aman", "stream": "Science", "marks": 85},
    {"name": "Rohan", "stream": "Commerce", "marks": 78},
    {"name": "Priya", "stream": "Science", "marks": 92},
    {"name": "Neha", "stream": "Arts", "marks": 88},
    {"name": "Karan", "stream": "Commerce", "marks": 90}
]
for i in students:
    name,stream,marks=i
print(i)