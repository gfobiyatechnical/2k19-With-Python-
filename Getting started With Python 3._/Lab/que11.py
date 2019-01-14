
#Aim : Program  to  find  the  number  of  currency  notes  of  each  type  (Rs.  2000,  Rs.  500  and  Rs.  100), when the total number of currency notes counted altogether is minimum and there must be at least a 100 rupee note dispensed. The amount to be withdrawn is to be entered by the user.

#Developer: Rakesh yadav


ammount = int (input("Enter the ammount: "))


	# calculation for required notes

ammount = ammount - 100

thou_notes = ammount // 2000

ammount = ammount % 2000

fivehund_notes = ammount // 500

ammount = ammount % 500

twohund = ammount // 200

ammount = ammount % 200

hund_notes = ammount // 100

print("number of note of Rs. 2000: %d" %thou_notes)
print("number of note of Rs. 500: %d" %fivehund_notes)
print("number of note of Rs. 200: %d" %twohund)
print("number of note of Rs. 100: %d" %hund_notes)


