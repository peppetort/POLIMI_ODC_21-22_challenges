
from pwn import *
import string
from itertools import product
from time import time

FLAG = 'flag{packer-4_3-1337&-annoying__}'

def x(string: str, index: int):
	input_string_len = len(string)
	if index + 22 < input_string_len:
		if string[index+20] ^ '.'[index] == string[index+21]:
			res = x(string=string, index=index+1)
		else:
			res = 0
	else:
		return 1
	return res


all_char = string.digits + string.ascii_letters + string.punctuation

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


def decrypt_flag(starting_letter):
	key = b'\x0b\x4c\x0f\x00\x01\x16\x10\x07\x09\x38\x00'
	flag = starting_letter

	for b in key:
		xor_res = int.from_bytes(flag[-1].encode(), "little") ^ b
		string_res = xor_res.to_bytes(1, "little").decode('utf-8')
		if string_res not in all_char:
			return 'NO'

		flag = flag + string_res

	return flag


for char in all_char:
	result = decrypt_flag(char)

	if result.find('NO') != 0:
		print(result)