#!/usr/bin/env python3   
#!-*- coding:utf-8 -*-
# Autor: boladao
# Add or Change API File
from time import sleep

class MainChangeApiFile:

	def __init_(self):
		pass

	def add_api(self):
		info_file = "info_client.txt"

		print("Escrever File -> {} [Y/N]".format(info_file))
		i = input(str(": "))

		if i.upper() == 'Y':
			
			info_file = "info_client.txt"
			stringfile = []

			with open(info_file, 'r') as f:
				stringfile = f.readlines()	

			console = input(str("Console: "))
			api_key = input(str("API Key: "))

			string_end = "{},{}".format(console, api_key)
			stringfile.append(string_end)	

			with open(info_file, 'w') as f:
				for s in stringfile:
					s = s.replace('\n', '')
					f.write(s + "\n")

			print("Write File -> {}".format(info_file))		

			sleep(5)

		elif i.upper() == 'N':

			try:

				novo_info_file = input(str("File: "))
				console = input(str("Console: "))
				api_key = input(str("API Key: "))

				with open(novo_info_file, 'r') as f:
					stringfile = f.readlines()	

				string_end = "{},{}".format(console, api_key)
				stringfile.append(string_end)	

				with open(novo_info_file, 'w') as f:
					for s in stringfile:
						s = s.replace('\n', '')
						f.write(s + "\n")

				print("Write File -> {}".format(novo_info_file))		
				sleep(5)
	
			except Exception as e:
				print(e)
				sleep(5)
		
	def edit_api(self):
		info_file = "info_client.txt"

		print("Escrever File -> {} [Y/N]".format(info_file))
		i = input(str(": "))

		if i.upper() == 'Y':
			
			info_file = "info_client.txt"
			stringfile = []

			with open(info_file, 'r') as f:
				stringfile = f.readlines()	

			console = input(str("Console: "))

			x = 0

			for i in stringfile:
				value = i.split(',')
				if value[0].upper() == console.upper():
					api_key = input(str("Informe a nova API KEY: "))
					value[1] = api_key
					string = '{},{}'.format(value[0],api_key)
					stringfile[x] = string

				x+=1

			with open(info_file, 'w') as f:
				for s in stringfile:
					s = s.replace('\n', '')
					f.write(s + "\n")

			print("Write File -> {}".format(info_file))		

			sleep(5)

			
		elif i.upper() == 'N':

			try:

				novo_info_file = input(str("File: "))
				stringfile = []

				with open(novo_info_file, 'r') as f:
					stringfile = f.readlines()	

				console = input(str("Console: "))

				x = 0

				for i in stringfile:
					value = i.split(',')
					if value[0].upper() == console.upper():
						api_key = input(str("Informe a nova API KEY: "))
						value[1] = api_key
						string = '{},{}'.format(value[0],api_key)
						stringfile[x] = string

					x+=1

				with open(novo_info_file, 'w') as f:
					for s in stringfile:
						s = s.replace('\n', '')
						f.write(s + "\n")

				print("Write File -> {}".format(novo_info_file))		
				sleep(5)


			except Exception as e:
				print(e)
				sleep(5)

while True:


	print("""

			##############

			{ OPTIONS }

			[c] - Change API KEY File
			[d] - Add API KEY File


			###############

			[0] - Quit
		""")

	entrada = input(str(": "))

	main = MainChangeApiFile()

	if entrada == '0':
		break

	elif entrada.lower() == 'd':
		main.add_api()

	elif entrada.lower() == 'c':
		main.edit_api()