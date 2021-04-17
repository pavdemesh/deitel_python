ndlist = list([None] * 3 for i in range(2))

filling_order = 1

for i in range(len(ndlist)):
    for j in range(len(ndlist[i])):
        ndlist[i][j] = filling_order
        filling_order += 1
        

def prnt_lst(lst):
    print(" ", end="")
    for i in range(len(lst[0])):
        print(f"{i:>4}", end="")
    print("\n")
    
    for row in range(len(lst)):
        print(row, end="")
        for col in range(len(lst[row])):
            print(f"{lst[row][col]:>4}", end="")
        print("\n")

    
prnt_lst(ndlist)
