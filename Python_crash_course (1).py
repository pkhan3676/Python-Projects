# Python_crash_course.py
#
# Prince Khan
# 2025-09-17

#%% --- Execute commands in console, from editor or as script ---
print('Hello world!')

# print('Hello world!')
# Hello world!
# runcell('Execute commands in console, from editor or as script', '/home/conrad/untitled0.py')
# Hello world!

3+5
3-5
3*5
5/3


#%% --- Variables and values ---
a = 3
b = 5
B = 10

print(b, B)

c = a+b


#%% --- Data types ---
i = 123
f = 1.23
b = True
s = 'Text'
l = [5, 6, 7, 8]

print(i, f, b, s, l)

type(i)
type(f)
type(b)
type(s)
type(l)


#%% --- Type conversion ---
print(s + f)
print(s + str(f))
print(s + ' ' + str(f))
s2 = s + ' ' + str(f)
print(s2)

s3 = '4.56'
print(f+s3)
print(f+float(s3))
f2 = f+float(s3)
print(f2)


#%% --- Indexing/ slicing ---
print(l[0])
print(l[1])
print(l[1:3])
print(l[1:])
print(l[:2])

print(s[0])
print(s[1])
print(s[1:3])
print(s[1:])
print(s[:2])


#%% --- If statements ---
condition = False

if condition:
    print('Yes')
else:
    print('No')
    
    
#%% --- Logic expressions (>, <, ==, >=, <=, !=) ---
setpoint = 5
value = 5

if value > setpoint:
    print('Too high')
elif value < setpoint:
    print('Too low')
else:
    print('Good!')


#%% --- For loops ---
for j in range(10):
    print('Counter is ' + str(j))

my_list = ['A', 'B', 'C']
for my_element in my_list:
    print('Element is ' + my_element)


#%% --- While loops ---
k = 0
while k < 5:
    k = k+1
    print(k)

while True:
    my_input = input('Type number: ')
    if my_input == '0':
        print('Done.')
        break

    
#%% --- Functions ---
def say_hello(name):
    print('Hello, ' + name + '!')
    
say_hello('Bob')

def calc_square(value):
    return value*value

print(calc_square(3))


#%% --- Error handling ---
x = 5
y = 2
print(x/y)

try:
    print(x/y)
except:
    print('y is zero!')
    

#%% --- String analysis and decomposition ---
my_string = 'Find the *word* between the starts.'

idx_start = my_string.find('*')
my_string[idx_start]
my_string[idx_start+1:]
idx_end = my_string.find('*', idx_start+1)
my_word = my_string[idx_start+1:idx_end]
print(my_word)

my_messi_string = 'UpPer anD lOwer CASE miXed!'
print(my_messi_string.lower())


#%% --- Tipps for the chat bot ---
# - Use the input function to query user input
# - Use an if statement to react on differents inputs
# - Define if or elif blocks for each case
# - Analyse/ decompose the input string
# - Calculate the result if a calculation was asked for
# - Compose and print your response string
# - Use an infinite while loop for an ongoing conversation
