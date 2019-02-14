import math
import datetime
import os


def hello(a_name):
  print("Hello! " + a_name)


def hello2(name_a,name_b):
  print("Hello! " + name_a + " and " + name_b)


def sum_two(x,y):
  z = x + y
  return z


def circle_area(radius):
  a = math.pi * radius ** 2
  return a


def today():
  now = datetime.datetime.now()
  return now.day


def my_sum(a_list):
  total = 0
  for n in a_list:
    total = total + n
  return total


def my_prod(a_list):
  total = 1
  for n in a_list:
    total = total * n
  return total


def my_count(a_list):
  count = 0
  for n in a_list:
    count = 1 + count
  return count


def my_count_less_5(a_list):
  count = 0
  for n in a_list:
    if n < 5:
      count = count + 1
  return count


def my_count_ones(a_list):
  count = 0
  for n in a_list:
    if n == 1:
      count = count + 1
  return count


def is_list_empty(a_list):
  if my_count(a_list) == 0:
    return True
  else:
    return False


def my_max(a_list):
  if is_list_empty(a_list):
    return None
  else:
    b = a_list[0]
    for n in a_list:
      if n > b:
        b = n
    return b


# get_filenames('C:\\Users\\sback')
# --> list of file names
# ['C:\\Users\\sback\\code.py', 'C:\\Users\\sback\\imageprocessor.py', 'C:\\Users\\sback\\loops.py', 'start.py']
def get_filenames(a_dirname):
  list_of_files = os.listdir(a_dirname)
  all_files = []
  for filename in list_of_files:
    full_path = os.path.join(a_dirname,filename)
    if os.path.isdir(full_path): # if the file is a dir we skip it
      pass
    else:
      all_files.append(full_path)
  return all_files

#[12,34,[56,67]] -->12, 34, 56, 67


def flatten(a_list_with_list):
    new_list = []
    for n in a_list_with_list:
     if isinstance(n,list):   # is n a type list?
        for i in n:
            new_list.append(i)
     else:
            new_list.append(n)   # como no es una lista ese elemento, agrega el mismo valor a la lista prin 
    return new_list

def print_right(a_list_with_list):
    for n in a_list_with_list:
        if isinstance(n,list):
            for i in n:
                print(i, end='')
            print("")
        else:
            print(n)

a_list_with_list= [12,3,[58,67],78]
#print_right(a_list_with_list)

#

def single_row_stars(number):
    for n in range(number):
        print("*", end='')
    print(" ")

#ingle_row_stars(4) 

def single_row_stars_line(number):
    for n in range(number):
        print("*", end='-')    #podes poner algo en el " end "" " que va a estar


#num = int(input("Give a number: ")) 
#num2= int(input("Give a number: ")) 
#stg = input("Give me a symbol: ")
#single_row_stars_line(num)


def single_row_of(num,stg):
    for n in range(num):
        print(stg, end = "")

#single_row_of(num,stg) 

a = [0,0,0,0]
def square_of_stars(num):
    for n in a:
        for n in range(num):
            print("*", end="")
        print("")

#square_of_stars(num)

def square_of_starss(num):
    for n in range(num):
        for n in range(num):
            print("*", end="")
        print("")

def rectangle_of_stars(rows,cols):
    for n in range(rows):
        for n in range(cols):
            print("*", end="")
        print("")

#rectangle_of_stars(num,num2)

# list_by_2([1,2,3]) --> [2,4,6]
a_list= [1,2,3]

def list_by_2(a_list):
    new_list = []
    for n in a_list:
        i = n*2
        new_list.append(i)
    print(new_list)

#list_by_2(a_list)

def list_reverse(a_list):
    new_list = []
    index = -1
    for i in range( len(a_list)):        
        new_list.append(a_list[index])
        index = index - 1
    return new_list

#list_inverted(a_list)

# Create_grid(4)

def create_grid(size):
    new_grid = []
    for row in range(size):
        new_sublist = []
        for column in range(size):
            new_sublist.append("-")
        new_grid.append(new_sublist)
    return new_grid

#grind = create_grid(4)
#print(grind)

#grind[0][1] ="x"


# is_duplicate_there(list_a,list_b)
list_a = [1,2,3]
list_b = [4,5,6]
def is_duplicate_there(list_a,list_b):
    for n in range(len(list_a)):
        list_a[n] = list_b[n]
    return list_a


def analize_duplicate(list_a,list_b):
    for n in range(len(list_a)):
        if list_a == list_b :
            return True
        else:
            return False

print(analize_duplicate(list_a,list_b))

print(is_duplicate_there(list_a,list_b))

