#9.1
#i)
def good():
    return{'Harry', 'Ron', 'Hermione'}

good()

#ii)
def good(*args):
  return list(args)
good('Harry', 'Ron', 'Hermione')

#9.2 
#i)
def get_odds(start=1, end=10, step=1):
    for start in range(10):
        if start%2==1:
            print(start)
        else:
            pass

get_odds()

#ii)
def get_odds(start, end, step):
    for start in range(10):
        if start%2==1:
            print(start)
        else:
            pass

get_odds(1, 10, 1)

#iii)
def get_odds():
    for number in range(1,10,2):
        print(number)
        yield number
    
for count, number in enumerate(get_odds(),1):
    if count==3:
        print("The third odd number is:", number)
        break

#9.3
def test(func):
    def new_function(*args, **kwargs):
        print("start")
        result=func(*args, **kwargs)
        print("ends")
        return result
    return new_function

@test
def a():
    print("hello")

a()

#9.4
class OopsException(Exception):
    print("Caught an oops")
    pass

list=[1,2,3]
position=3

try:
    print(list[position])
    raise OopsException
except Exception as e:
    print("예외가 발생했습니다",e)
