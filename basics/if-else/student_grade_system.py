


mark_1=int(input("Enter Your  Maths marks...."))
mark_2=int(input("Enter Your English marks...."))
mark_3=int(input("Enter Your Chemistry marks...."))

tot_marks = ((mark_1 + mark_2 + mark_3)/300 ) * 100

if tot_marks >= 90:
 print("Your Grade is A1.....")
 print(f"Your Average is {tot_marks}")
elif tot_marks >= 80:
 print("Your Grade is A......")
 print(f"Your Average is {tot_marks}")
elif tot_marks >= 70:
 print("Your Grade is B....")
 print(f"Your Average is {tot_marks}")
elif tot_marks >= 60:
 print("Your Grade is C.....")
 print(f"Your Average is {tot_marks}")
else:
 print("You Failed......")
 print(f"Your Average is {tot_marks}")        