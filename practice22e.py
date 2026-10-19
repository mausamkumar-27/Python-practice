def calculate_sum(*nums):
    sum=0
    for i in nums:
        sum +=i
    print(sum)
calculate_sum(10,20,30,40,50)



def check(*args):
    print(args)
    print(type(args))
check('Mausam',19,'Delhi')