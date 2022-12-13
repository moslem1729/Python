t=int(input())
nums=[]
for i in range(t):
    num=int(input())
    nums.append(num)

def calculate(number):
    output=""
    if number<=1023:
        output=output+str(number)+"B"
        print(output)
    elif 1024*1024>number>1023:
        output=str(number//1024)+"KiB"
        print(output)
    else:
        output=str(number//(1024*1024))+"MiB"
        print(output)
for num in nums:
    calculate(num)