mystring = "mystring python"

print(mystring [0])  # Output: m
print(mystring [1])  # Output: y
print(mystring [2])  # Output: s    
print(mystring [3])  # Output: t
print(mystring [4])  # Output: r
print(mystring [5])  # Output: i
print(mystring[6])  # Output: n
print(mystring[7])  # Output: g
print(mystring[0:8])  # Output: mystring
print(mystring[:8])  # Output: mystring
print(mystring[:-6])  # Output: mystring

print(mystring[-6])  # Output: p
print(mystring[-5])  # Output: y
print(mystring[-4])  # Output: t
print(mystring[-3])  # Output: h
print(mystring[-2])  # Output: o
print(mystring[-1])  # Output: n
print(mystring[-6:])  # Output: python
print(mystring[-6:-1])  # Output: pytho
print(mystring[-6:-2])  # Output: pyth
print(mystring[-6:-3])  # Output: pyt
print(mystring[-6:-4])  # Output: py
print(mystring[-6:-5])  # Output: p
print(mystring[-6:-6])  # Output: (empty) because start and end are the same place, and end is not included

print(mystring[-6:-7])  # Output: (empty) because the end is before the start and the default step is +1

print(mystring[1:5:3])  # Output: yr
print(mystring[1:6:2])  # Output: yti
print(mystring[::3])  # Output: mtnph
print(mystring[::-2])  # Output: nhy nrsm
print(mystring[::-1])  # Output: nohtyp gnirtsym
print(mystring[:5:-1])  # Output: nohtyp gn   (with a negative step it starts from the last letter and stops before index 5)
print(mystring[5:1:-1])  # Output: irts
print(mystring[-3:])  # Output: hon

a = "I love python and 4g technology and 3rd generation"
b = "  I love python    "
print(len(a)) # Output: 50
print(len(b)) # Output: 19
print(b.strip()) # Output: I love python
print(b.rstrip()) # Output:   I love python    
print(b.lstrip()) # Output:I love python

c = " @#@$! I love python @#@$!"
print(c.strip("@#@$! ")) # Output: I love python
print(c.rstrip("@#@$! ")) # Output:  @#@$! I love python
print(c.lstrip("@#@$! ")) # Output: I love python @#@$!

print(a.upper())  # Output: I LOVE PYTHON AND 4G TECHNOLOGY AND 3RD GENERATION
print(a.lower())  # Output: i love python and 4g technology and 3rd generation
print(a.title())  # Output: I Love Python And 4G Technology And 3Rd Generation
print(a.capitalize())  # Output: I love python and 4g technology and 3rd generation

d , f ,g , h = "" , "1", "11", "111"

print(d.zfill(3))  # Output: 000
print(f.zfill(3))  # Output: 001
print(g.zfill(3))  # Output: 011
print(h.zfill(3))  # Output: 111

print(a.split())  # Output: ['I', 'love', 'python', 'and', '4g', 'technology', 'and', '3rd', 'generation']
print(a.split("and"))  # Output: ['I love python ', ' 4g technology ', ' 3rd generation']
print(a.split("and", 1))  # Output: ['I love python ', ' 4g technology and 3rd generation']
print(a.rsplit("and", 1)) # Output: ['I love python and 4g technology ', ' 3rd generation']
print(type(a.split()))  # Output: <class 'list'>

print(a.center(56, "*"))  # Output: ***I love python and 4g technology and 3rd generation***
print(a.center(56))  # Output:    I love python and 4g technology and 3rd generation

print(a.count("and"))  # Output: 2
print(a.count("and", 0, 20))  # Output: 1
print(a.count("and", 20, 50))  # Output: 1
print(a.count("and", 0, 50))  # Output: 2
print(a.count("and", 20, 30))  # Output: 0
print(a.count("and", 0, ))  # Output: 2
print(a.count("And"))  # Output: 0

v = "I lOvE pYtHoN"
n = "i LoVe PyThOn"

print(v.swapcase())  # Output: i LoVe PyThOn
print(n.swapcase())  # Output: I lOvE pYtHoN

print(v.startswith("I"))  # Output: True
print(v.startswith("i"))  # Output: False
print(v.startswith("I l"))  # Output: True
print(v.startswith("v", 4, 10))  # Output: True

print(v.endswith("N"))  # Output: True
print(v[::-1].endswith("I")) # Output: True
print(v.endswith("n"))  # Output: False


s = "  Python is FUN and python is POWERFUL  "

print(s.strip())  # Output: Python is FUN and python is POWERFUL
print(s.lower().count("python"))  # Output: 2
print(s[::-1])  # Output: LUFREWOP SI NOHTYP DNA NUF SI NOHTYP
print(s.strip().startswith("Python"))  # Output: True
print(s.strip().endswith("L"))  # Output: True
print(s.strip()[:6]) # Output: Python
print(s.strip()[-8:]) # Output: POWERFUL
print(s.strip().title().center(50,"-"))  # Output: -------Python Is Fun And Python Is Powerful-------
print(len(s.strip().split())) # Output: 7