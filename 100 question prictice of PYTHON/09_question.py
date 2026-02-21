# Generate Fibonnachi sequence upto user provided input 
# Example: n = 7, fib sequence : 0,1,1,2,3,5,8......

# use:
# 1. user input
# 2. function
# 3. f_string

def fibonnachi(n):
    fibo_seq = [0,1]

    while len(fibo_seq) < n :
        next_term = fibo_seq[-1] + fibo_seq[-2]
        fibo_seq.append(next_term)
    return fibo_seq

user_inpur = int(input("Enter the number: "))
fibo_num = fibonnachi(user_inpur)
print(f"the {user_inpur} of fibonnachi is {fibo_num}")