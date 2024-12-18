#!python3
'''
sort all of the values of x into 2 lists.
1 list should contain all of the float values and the other list should contain all the integer values'''


def main():
    
    x = [7.7, 1, 3.3, 4.2, 1, 1, 2.8, 2, 8, 3, 4, 5, 7, 9.2, 3.1, 9, 6, 4, 8, 5, 1.9, 2, 4, 4, 5.2, 2, 5.4, 2, 3.4, 7, 9.2, 3.7, 10, 8, 7, 6, 2, 2.2, 1, 11.1]
    
    integers = []
    decimals = []
    
    for i in x:
        if i % 1 == 0:
            integers.append(i)
        else:
            decimals.append(i)
    print(integers)
    print(decimals)

    return integers and decimals
    

if __name__ == "__main__":
    main()

