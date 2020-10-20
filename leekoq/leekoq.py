# Copyright 2020 Marcos Del Sol Vives <marcos@orca.pet>
# SPDX-License-Identifier: WTFPL

# 1-bit lookup table for the NLF
LUT = 0x3A5C742E

def encrypt(block: int, key: int) -> int:
	"""
	Encrypts a 32-bit block of plaintext using the KeeLoq algorithm.

	:param int block: 32-bit plaintext block
	:param int key: 64-bit key
	:return: 32-bit ciphertext block
	:rtype: int
	"""

	for i in range(528):
		# Calculate LUT key
		lutkey = (block >> 1) & 1 | (block >> 8) & 2 | (block >> 18) & 4 | (block >> 23) & 8 | (block >> 27) & 16

		# Calculate next bit to feed
		msb = (block >> 16 & 1) ^ (block & 1) ^ (LUT >> lutkey & 1) ^ (key & 1)

		# Feed it
		block = msb << 31 | block >> 1

		# Rotate key right
		key = (key & 1) << 63 | key >> 1

	return block

def decrypt(block: int, key: int) -> int:
	"""
	Decrypts a 32-bit block of ciphertext using the KeeLoq algorithm.

	:param int block: 32-bit ciphertext block
	:param int key: 64-bit key
	:return: 32-bit plaintext block
	:rtype: int
	"""

	for i in range(528):
		# Calculate LUT key
		lutkey = (block >> 0) & 1 | (block >> 7) & 2 | (block >> 17) & 4 | (block >> 22) & 8 | (block >> 26) & 16

		# Calculate next bit to feed
		lsb = (block >> 31) ^ (block >> 15 & 1) ^ (LUT >> lutkey & 1) ^ (key >> 15 & 1)

		# Feed it
		block = (block & 0x7FFFFFFF) << 1 | lsb

		# Rotate key left
		key = (key & 0x7FFFFFFFFFFFFFFF) << 1 | key >> 63

	return block
