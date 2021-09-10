# type elements separated by space
row0=input("enter 1st row :"). split()
row1=input("enter 2nd row :"). split()
row2=input("enter 3rd row :"). split()
for i in range(0,3):
	row0[i]=int(row0[i])
	row1[i]=int(row1[i])
	row2[i]=int(row2[i])
print((row0[0]*((row1[1]*row2[2])-(row2[1]*row1[2])))-(row0[1]*((row1[0]*row2[2])-(row2[0]*row1[2])))+(row0[2]*((row1[0]*row2[1])-(row2[0]*row1[1]))))
