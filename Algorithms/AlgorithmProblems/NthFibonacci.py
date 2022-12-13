def nth_fibonacci_recursive(number):
    if number==1:
        return 0
    elif number==2:
        return 1
    else:
        return nth_fibonacci_recursive(number-1) + nth_fibonacci_recursive(number-2)

def nth_fibonacci_recursive_hashmap(number,memoize={1:0,2:1}):
    if number in memoize:
        return memoize[number]
    else:
        memoize[number]=nth_fibonacci_recursive_hashmap(number-1,memoize)+nth_fibonacci_recursive_hashmap(number-2,memoize)
        return memoize[number]



def nth_fibonacci_iterative(number):
   last_two_fibonacci=[0,1]
   counter=3

   while counter<=number:
        next_fibonacci=last_two_fibonacci[0]+last_two_fibonacci[1]
        last_two_fibonacci[0]=last_two_fibonacci[1]
        last_two_fibonacci[1]=next_fibonacci
        counter+=1
   return last_two_fibonacci[1]

print(nth_fibonacci_recursive(10))
print(nth_fibonacci_iterative(10))
print(nth_fibonacci_recursive_hashmap(10))