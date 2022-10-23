import donut
import argparse
import binascii
from ShellcodeRDI import * # https://github.com/monoxgas/sRDI
from base64 import b64encode

def use_srdi(file_name):
	dll = open(file_name, 'rb').read()
	shellcode = ConvertToShellcode(dll)
	return shellcode

def use_donut(file_name):
	shellcode = donut.create(file=file_name)
	return shellcode

def format_shellcode(shellcode):
	return ''.join(f'\\x{byte:02x}' for byte in shellcode)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f", "--file-name", dest="file_name")
	parser.add_argument("-m", "--method")
	args = parser.parse_args()

	file = args.file_name
	output_file_raw = file.replace('.dll', '.bin')
	output_file_txt = file.replace('.dll', '.txt')
	output_file_b64 = file.replace('.dll', '_b64.txt')
	method = args.method

	if method == "donut":
		print("[+] Using donut...")
		shellcode = use_donut(file)
	elif method == "srdi":
		print("[+] Using srdi...")
		shellcode = use_srdi(file)
	else:
		print("Invalid method selected. Use donut or srdi")
		return 

	with open(output_file_raw, "wb") as f:
		f.write(shellcode)
	print(f"[+] Wrote raw shellcode to {output_file_raw}")

	with open(output_file_b64, "wb") as f:
		f.write(b64encode(shellcode))
	print(f"[+] Wrote base64 encoded shellcode to {output_file_b64}")

	formatted_shellcode = format_shellcode(shellcode)
	with open(output_file_txt, "w") as f:
		f.write(formatted_shellcode)

	print(f"[+] Wrote formatted shellcode to {output_file_txt}")

if __name__ == "__main__":
	main()
