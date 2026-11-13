sentence="python is great and python is easy to learn because python is powerful"
sentence_list=sentence.split(" ")
#print(sentence_list)
my_dict= {i:sentence_list.count(i)  for i in sentence_list }
print(my_dict)