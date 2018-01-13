#!/usr/bin/python3

import random
import shelve
import time

def simulate_work(current_value):
	time.sleep(1)
	return current_value + 1		

def new_mode():
	start_value = random.randint(1,10)
	try:
		while start_value < 50:
			start_value = simulate_work(start_value)	
		return start_value
	except KeyboardInterrupt:
		with shelve.open('work_in_progress') as store:
			store['current_val'] = start_value
		raise

def resume_mode():
	try:
		with shelve.open('work_in_progress') as store:
			current_val = store['current_val']
			while current_val < 50:
				current_val = simulate_work(current_val)
		return current_val
	except KeyboardInterrupt:
		with shelve.open('work_in_progress') as store:
			store['current_val'] = current_val
		raise

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('mode', choices=['new', 'resume'], type=str, help='choose whether to begin a new task, or to resume one that has been previously shelved.')	
	args = parser.parse_args()
	if args.mode == 'new':
		result = new_mode()
		print(result)	
	elif args.mode == 'resume':
		result = resume_mode()
		print(result)
