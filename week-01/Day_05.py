# a = input()
# b = " ".join(a.split()).replace("java","python",1)

# print(b.rjust(40, "#"))
# print(b.find("python"))
# print(b)



name = "youssef azazy" 
age = 19
rank = 8
bank_money = 80393949858

print("my name's : {:s} \nmy age is: {:d} & rank: {:.2f} ".format(name ,age , rank))
print("my name's : {:.7s} \nmy money in bank {:,d}" .format(name , bank_money))


n , k , l = "azazy" , "youssef" , "mohamed"

print("hello: {1} {2} {0}".format(n , k , l))


s,d,f,g= 39 , "ahmed", 672873889 , 16

print("my detail {1:s} \n{0:d} \n{2:,d} \n{3:.2f}".format(s,d,f,g))
print(f"my detail: name {d}\nage  {s}\n my money {f}\n rank {g}")

print(type(100))
print(type(-10))
print(type(-10.00))
print(type(10.3))

complex_number= 6+ 3j

print(type(complex_number))
print("real num {}".format(complex_number.real))
print("imagnary num {}".format(complex_number.imag))

print(10)
print(float(10))
print(complex(10))

print(10.55)
print(int(10.55))
print(complex(10.55))


# 1. Addition and Subtraction
print(10 + 30)          # 40
print(10 + 20)          # 30
print(3.66 + 2.33)      # 5.99
print(1.2 + 1.2)        # 2.4
print(40 - 10)          # 30
print(-30 - 20)         # -50
print(-30 - (-20))      # -10

# 2. Multiplication and Operator Precedence
print(10 * 3)           # 30
print(5 + 10 * 100)     # 1005 (Multiplication is evaluated first)
print((5 + 10) * 100)   # 1500 (Parentheses change the priority)

# 3. Division
print(100 / 20)         # 5.0 (Returns a float)
print(int(100 / 20))    # 5 (Converting division result to an integer)

# 4. Modulus (Remainder)
print(8 % 2)            # 0 (No remainder)
print(9 % 2)            # 1 (Remainder is 1)
print(20 % 5)           # 0
print(22 % 5)           # 2 (Closest multiple is 20, remainder is 2)

# 5. Exponentiation
print(2 ** 5)           # 32 (2 to the power of 5)
print(5 ** 4)           # 625 (5 to the power of 4)

# 6. Floor Division
print(100 // 20)        # 5
print(110 // 20)        # 5
print(119 // 20)        # 5
print(120 // 20)        # 6
print(130 // 20)        # 6
print(139 // 20)        # 6
print(140 // 20)        # 7
print(142 // 20)        # 7

a = int(input())
b = int(input())

print (f" a + b = {a+b} \na - b = {a-b}")
print (f" a * b = {a*b} \na / b = {a/b:.2f}")
print (f" a // b = {a//b} \na % b = {a%b} \na ** b = {a**b}" )


all_time = int(input("Enter a time of minutes"))

print ("{} hours {} minutes".format(all_time // 60 ,all_time % 60))