#gives the second least value in the list
list1=[]
for i in range(int(input("enter total number of students:"))):
        name = str(input(f"enter the name of the student{i}:"))
        score = float(input(f"enter the score obtained by student{i}:"))
        list1.append([name,score])
        sortedli=sorted(set(score for name,score in list1))
second_lowscore=sortedli[1]
second_name=sorted(set(name for name,score in list1 if second_lowscore==score))
print("the second lowest score obtained by the student is:",second_name)   
