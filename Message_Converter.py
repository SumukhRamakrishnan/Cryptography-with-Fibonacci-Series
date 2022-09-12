"""
It is the main program for the encryption . It calls other function message-divisor  . It takes two input two values.
One is the input text and theother is a numeric integer to shift the numeric values of the unicode characters
It call the message divisor to determine determine the side length, to construct the square matrix- M,
construct a 1-dimensional matrix, slice it to a 2-dimensional matrix D.  Divide D into block matrices  B-i and
finds the determinant . Construct the matrix K eliminating te 3rd column and and shifting column1 and 2 to right by one positions.
Fill the column  with determinant found.  This is then used as input to the Decryption process.

"""
import array as arr
import numpy as np

a_in = input('Input text: ')
n_user = input('Choose your n > 0 : ')
try:
    n = int(n_user)
except ValueError:
    print("This is not a positive integer.", end = ' ')
    n = input('Please choose an integer for n > 0 : ')
try:
    n_int = int(n)
except ValueError:
    exit()
n_int = int(n)
if (n_int <= 0):
    print("This is not a postive integer greater than zero.")
    exit()
#If the value is greater than 97, the numeric values for org_character in Fibonacci_Decode_Main.py would result in negative values.
# The values would be out of the range for the function chr() in Fibonacci_Decode_Main.py. Hence it would give an error or an unexpected character.
#The Message_Converter.py and Message_Divisor.py has no such limitation and will run for all values of n.
if n_int > 97:
    n_int = 97


len_a_in = len(a_in)
list_a_in = list(a_in)
print("Length of the Text:", len_a_in)

#It determines the side-length for the given length of the message of the square matrix M.

def side_length(x):
    c = 2
    for i in range(len_a_in):
        if len_a_in > c ** 2:
            c = c + 2
        elif len_a_in < c ** 2:
            break
        elif len_a_in == c ** 2:
            break
    return c

# if the length of input text is  less than 8 then pad with spaces to start with a minimum  side-length of 4

if len_a_in < 8:
    while len_a_in < 8:
        len_a_in = len_a_in + 1
        a_in = a_in.ljust(len_a_in)
        print(a_in)

print("Sidelength of the square matrix M:", side_length(len_a_in))

# pad zeroes to the right to fill the matrix.

l=side_length(len_a_in)/2
k = int(l) #sidelength divided by 2
k_2 = k^2
zero_array = []
number_zeros = (side_length(len_a_in)) ** 2 - len_a_in
for i in range(number_zeros):
    zeros = 0
    zero_array.append(zeros)
print("Number of zeros", zero_array)

# form the 1-dimensional matrix with the zeros

smallArrays = (side_length(len_a_in) / 2) ** 2
y = int(smallArrays)
print("2-by-2 Matrices:", y)

a_in == a_in.lower()
output = []
for character in a_in:
    number = ord(character) -97\
             + n_int
    output.append(number)
output.extend(zero_array)

# slice the matrix D into block matrices

nArr2D = np.matrix(output)
print("1-dimensional Matrix:", "\n", output)
a = nArr2D.reshape(side_length(len_a_in),side_length(len_a_in))
h = int((side_length(len_a_in)**2)/2) #Sidelength squared divided by 2
print("2m^2:",h)
b_tobeslicedup = nArr2D.reshape(2,h)
print("Square Matrix M to determine the number of zeros:", "\n", a)
print("Matrix D:", "\n", b_tobeslicedup)

if side_length(len_a_in) > 2:
    split = y
    A_slice = a[:split,:split]

