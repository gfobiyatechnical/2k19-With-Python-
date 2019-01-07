# to find the number notes  of Entered ammount

ammount = int (input("Enter the ammount: "))

thou_notes = ammount // 2000
ammount = ammount % 2000

fivehund_notes = ammount // 500

ammount = ammount % 500

hund_notes = ammount // 100

print("number of note of Rs. 2000: %d" %thou_notes)
print("number of note of Rs. 500: %d" %fivehund_notes)
print("number of note of Rs. 100: %d" %hund_notes)

