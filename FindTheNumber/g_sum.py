from math import pow

def g_sum(n):
    if(n<0):
        return 0
    else:
        return (1/pow(2,n)) + g_sum(n-1)

if __name__ == "__main__":
    result = g_sum(25)
    print(result)


    
