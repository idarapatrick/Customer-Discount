
#A program that gets customer's input and calculates their discount based 
#On how much they spend with a percentage 0f 15 or 20

print("Is your bill between the range of $100 and $1000? ")
print("CAUTION! Do not type everything in capital letters")
answer = input()
print("okay then, input your bill here: ")
Bill = int(input())

#Discount for customers whose bill ranges from $100 to $999
#constraints for Bill: 100 <= n <= 999
if answer == "yes" or "Yes":
  if Bill >= 100 and Bill <= 990:
    Discount1 = Bill / 100 
    final_discount1 = Discount1 * 15
    total_bill1 = float(Bill) - float(final_discount1)
    print(total_bill1)
#Discount for customers whose bill ranges from $1000 and above 
  elif Bill >= 1000:  
    Discount2 = Bill / 100 
    final_discount2 = Discount2 * 20
    total_bill2 = Bill - final_discount2  
    print(total_bill2 )
#For customers whose bill does not exceed $99
  elif answer == "No" or "no":
    if Bill > 0 and Bill <= 99:
     total_bill3 = float(Bill)
     print(total_bill3)
     SystemExit()
   



