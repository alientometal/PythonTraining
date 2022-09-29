import math 
  
def isPerfectSquare(x): 
    s = int(math.sqrt(x)) 
    return s*s == x 
  
# Returns true if n is a Fibonacci number.  
def isFibonacci(n): 
    
    if type(n) == float:
        raise ValueError("Floats are not supported")
    elif type(n) == str:
        raise TypeError("Strings are not supported")
    elif n < 0:
        raise ValueError("Negatives are not supported")
    
    # n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    # is a perfect square
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

class FiboNumbers(object):
    def get_sequence(self):
        pass
    
    
    
def main():      
    for i in range(1,11): 
        if (isFibonacci(i) == True): 
            print(i,"Is a fibonacci number")
        else: 
            print(i,"Is not a fibonacci number")
    return

if __name__ == "__main__": 
    main()
