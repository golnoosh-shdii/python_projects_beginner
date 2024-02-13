def check_triangle(n1, n2, n3):
    if (n1 + n2 >= n3) or (n1 + n3 >= n2) or (n2 + n3 >= n1):
        print("it's a triangle")
        if n1 == n2 == n3:
            print("equilateral triangle")
        elif n1 == n2 or n1 == n3 or n2 == n3:
            print("isosceles triangle")
        else:
            print("scalene triangle")
    else:
        print("it's not a triangle")


n1 = int(input("please enter a number: "))
n2 =int(input("please enter a number: "))
n3 = int(input("please enter a number: "))
check_triangle(n1, n2, n3)

