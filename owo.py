import pyautogui
import time

n = input("How many times ?: ")

print("t minus")

count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Fire in the hole!!!")

for i in range(0,int(n)):{
        time.sleep(15),
	pyautogui.typewrite("owo h"+ '\n')
}
