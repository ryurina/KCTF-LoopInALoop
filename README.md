# KCTF-LoopInALoop

KniightCTF2022 - Programming - Loop In A Loop - WriteUp

Challenge Link: https://knightctf.com/challenges#Loop%20In%20A%20Loop-70

Authors: Rina RANARISON (loonatic) https://knightctf.com/users/724

## The code which the flag was made
```cpp
#include <iostream>
using namespace std;

int main() {
	string flag;
	cout << "Enter the flag: ";
	cin >> flag;

	for (int i=0; i < flag.length(); i++) {
		for (int j=i; j < flag.length() - 1; j++) {
			char x = flag[j];
			flag[j] = flag[j+1];
			flag[j+1] = x;
		}
	}

	if (flag == "CFb5cp0rm1gK{1r4nT_m4}6")
		cout << "Congrats. That's the flag!" << endl;
	else
		cout << "Wrong flag. Bye" << endl;

	return 0;
}
```
The code swap flag[j] and flag[j+1] character
So I was thinking, If I repeat the process of swaping n-times at the end I'll get the plaintext flag in order:
```
eg: Let's take the word "CTF"
We ran it in the program and it will give us: "TCF"
Then if we ran "TCF" in the program we get: "CTF"
```

I decided to make the same program but in Python (because I'm more efficient in python) and loop it until I get the correct flag and by adding starwith() to filter only the flag beginning with "KCTF{"

![image](https://user-images.githubusercontent.com/45909337/150624446-1ffe4e80-263d-43b7-8c5c-418da406aa05.png)

So, it required us to run it 124-times to get the right flag

### KCTF{b451c_pr06r4mm1ng}
