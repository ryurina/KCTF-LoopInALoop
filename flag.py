def lts(s): 
    str1 = "" 
    return (str1.join(s))

def flagger(flag):
    for i in range(len(flag)):
        for j in range(i, len(flag)-1):
            x = flag[j]
            flag[j] = flag[j+1]
            flag[j+1] = x
    return flag

if __name__ == "__main__":
    flag = input("flag: ")
    arr = list(flag)
    repeat = int(input("rep: "))
    for i in range(repeat):
        res = flagger(arr)
        sol = lts(res)
        if sol.startswith("KCTF{"):
            print(f"{i}: {sol}")
