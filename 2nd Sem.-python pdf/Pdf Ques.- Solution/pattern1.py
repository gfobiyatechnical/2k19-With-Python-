alfa="ABCD"
alf1="PQR"
for i in range(5):
    for j in range(5):
        if i<=j:
            print (alfa[i],end="")
        print(alf1[j:],end="")
    print()
