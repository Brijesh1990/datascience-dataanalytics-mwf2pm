"""
Python statements — brief overview and examples i.e called python statements.

A statement is an instruction that the Python interpreter can execute. Statements are broadly grouped into:

1) Simple (single-line) statements:
   - Expression statements
   - Assignment
   - Pass
   - Del
   - Import
   - Print (Python 2) / function call (Python 3)
   - Assert

2) Compound (block) statements or conditional statements:
   - if / elif / else
   - for / else
   - while / else
   - try / except / else / finally
   - with
   - def (function definition)
   - class (class definition)

3) Control-flow statements:
   - break
   - continue
   - return
   - raise
   - yield

Examples (executable):

Simple statements
-----------------
# expression statement
2 + 3

# assignment
message = 'Hello, Python statements'

# pass (no-op)
if True:
	pass

# del
temp = 10
del temp

# import
import math

# assert
assert math.sqrt(4) == 2

Compound statements
-------------------
def sign(x):
	# if / elif / else
	if x > 0:
		return 'positive'
	elif x < 0:
		return 'negative'
	else:
		return 'zero'

for i in range(3):
	# for loop with else
	print('i =', i)
else:
	print('loop finished')

count = 0
while count < 2:
	print('count', count)
	count += 1
else:
	print('while finished')

try:
	1 / 1
except ZeroDivisionError:
	print('division by zero')
else:
	print('try succeeded')
finally:
	pass

with open(__file__, 'r') as f:
	# with statement (context manager) — reading this file safely
	first_line = f.readline()

class Greeter:
	def __init__(self, name):
		self.name = name

	def greet(self):
		return f'Hello, {self.name}'

# Control flow statements
def generator():
	for n in range(3):
		if n == 1:
			# continue skips to next iteration
			continue
		if n == 2:
			# break exits loop
			break
		yield n

def raises_example():
	# raise an exception
	raise ValueError('example')

if __name__ == '__main__':
	print(message)
	print('sign(10):', sign(10))
	print('first line of this file:', first_line.strip())
	print('greeter:', Greeter('World').greet())
	print('generator list:', list(generator()))

"""
 
  
   
