#dictionary search
n = int(input("enter the total no of student :"))
student_marks = {}
print("enter the name and score :")
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input("enter the student name to find the average:")
s=[]
if query_name in student_marks.keys():
    s=student_marks[query_name]
avg=sum(s)/len(s)
print(f"the avereage of {query_name}:{avg:.2f}")
