a = "I move Python"

# print(a.index("P")) # Output: 7
# print(a.index("s")) # Output: Error

print(a.find("P")) # Output: 7
print(a.find("s")) # Output: -1

print(a.rjust(20))
print(a.rjust(20,"*"))

print(a.ljust(20))
print(a.ljust(20,"*"))

print(a.rjust(17,"*").ljust(21,"*"))

b = """ I love
python from
Elzero web """

print(b.splitlines())
print(" - ".join(b.splitlines()))

c =  " I love \npython from \nElzero web "
print(c.splitlines())

d = " I love \tpython from \tElzero web "
print(d.expandtabs(10))

e = "I Love Python And 4G Technology And 3Rd Generatio"
g = "I Love Python And 4G Technology and 3Rd Generatio"

print(e.istitle())
print(g.istitle())

l = "i love python"
m = "I LOVE PYTHON" 

print(l.islower())
print(l.isupper())
print(m.islower())
print(m.isupper())

o = "i___love"
n = "I---love"

print(o.isidentifier())
print(n.isidentifier())

p="mohamed"
q="mohamed10"

print(p.isalpha())
print(q.isalpha())
print(p.isalnum())
print(q.isalnum())

print(q.replace( "m" , "M" ,2)) 

print("-".join(e.split()))


name = "youssef azazy"
age = 18
rank = 8

print("my name is: %s" % name) # print("my name is: " + name)
print("my age is: %s" % age) 
print("my rank is: %s" % rank)# %s for string
print("my name is: %s\nmy age is: %s\nmy rank is: %s" % (name, age, rank))# %d for number
print("my name is: %s\nmy age is: %d\nmy rank is: %f" % (name, age, rank))# %f for float
print("my name is: %.7s" % name)
print("my rank is: %.3f" % rank)


r = input()

print("-".join(r.split()))
print(r.find("p"))
print(r.replace("o" , "0" , 2))

w = input()
price= float(input())

print(w.ljust(15,".")+("%.2F"% price).rjust(10))
print(w.istitle())

first_name = input()
last_name = input()
grade = int(input())
score = float(input())

print("Name: %s\nGrade: %d | Score: %.1f %%" % (first_name+" "+last_name,grade,score))
print(first_name.isalpha())
print(last_name.isalpha())

one= input()
two=(" ".join(one.split()).replace("bad" , "good"))
print(two)
print(two.find("good"))
print(two.rjust(30,"*"))