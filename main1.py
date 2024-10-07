# write a function that takes one input parameter and evaluates an expression a = n*10, for all values between 0 to n
import time 
n = 10000
def testfn(n):
    for i in range(0,n):
        a = i * 10
        
# extimate execution time of this functio  for n

start_time = time.time()
print(start_time)

testfn(n)

end_time = time.time()*10000
print(end_time)
print(f"For n =(n)\nExecutin time is(end_time - start_time) micro seconds")