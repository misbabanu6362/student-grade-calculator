students=input("enter a students name:") 
subject1=int(input("enter subject marks1:")) 
subject2=int(input("enter subject marks2:")) 
subject3=int(input("enter subject marks3:")) 
total=subject1+subject2+subject3
print(total)
avg=total/3
print(avg)
if avg>=90:
   grade="A"
elif avg>=80:
   grade="B"
elif avg>=70:
   grade="C"
elif avg>=50:
    grade="D"
else:   
   grade="Fail"
print(grade)
