matrix = [[0] * 4 for _ in range(3)]
for row in matrix:
    print(row)

print("""\
Usage: thingy [OPTIONS]\
    -h
    -H hostame\
""")

word = 'python'
print(word[:2])
print(word[4:])
print(word[-2:])
print(word[:2] + word[2:])

# List
# slice list_name[start, end]
# concatenate
squares = [1, 4, 9, 16, 25]
print(squares + [36, 49, 64, 81, 100])

a = len(squares)
print(a)

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(range(len(users)))


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# pass Statements
# def initlog(*args)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
Point(1, 2)
Point(2, 1)
Point(0,0)
Point(0,1)
for i in range(3):
    print(i)
