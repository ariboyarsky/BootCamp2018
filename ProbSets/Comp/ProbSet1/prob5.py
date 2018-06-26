import box as b
import sys
import random
import numpy as np
import time


if len(sys.argv) != 3:
	print("You need 3 arguments")
	exit(0)

pts = 0
nums = list(range(1,11))
over = 0
name = sys.argv[1]
remaining_time = float(sys.argv[2])

while(over == 0):
	while time > 0:
		timer = time.time()
		if sum(nums) < 7:
			roll = random.randint(1,6)
		else:
			roll1 = random.randint(1,6)
			roll2 = random.randint(1,6)
			roll = roll1 + roll2

		end = time.time()
		loop_time = end-timer
		remain -= loop_time

		if remain < 0:
			print("Lost")
			break

		if b.isvalid(roll, nums):
			print("Left: ", str(nums))
			print("Roll: ", str(roll))
			e = input("Nums to elminate?")

			while b.parse_input(e, nums) == []:
				print("Invalid!")
				e = input("Nums to elminate?")
			while sum(b.parse_input(e,nums)) != roll:
				print("Inavlid!")
				e = input("Nums to elminate?")

			rem = b.parse_input(e, nums)
			nums = [n for n in nums if n not in rem]

		else:
			over = 1
			print("Game Over")
pts = sum(numbers)
print(name, ": ", score)
if pts == 0:
	print("You win")
