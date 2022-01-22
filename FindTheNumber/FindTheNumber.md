# KCTF-FindTheNumber

KniightCTF2022 - Programming - Find The Number - WriteUp

Challenge Link: https://knightctf.com/challenges#Find%20The%20Number-69

Authors: Rina RANARISON (loonatic) https://knightctf.com/users/724

This is a pretty easy challenge, you just need to code the FlowChart and execute it with the integer "25" and get the result

![image](https://user-images.githubusercontent.com/45909337/150625032-a350ab50-9c31-484d-a312-5fb836b5ee1f.png)

Here I code the flowchart with Python so, we got this

```python
from math import pow

def g_sum(n):
    if(n<0):
        return 0
    else:
        return (1/pow(2,n)) + g_sum(n-1)

if __name__ == "__main__":
    result = g_sum(25)
    print(result)
```

Then when we run it, this is the result

![image](https://user-images.githubusercontent.com/45909337/150625075-2c5f6e06-6620-4423-96cf-cbade5a3e4db.png)

So the flag is: KCTF{1.9999999701976776}
