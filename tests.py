# Copyright 2020 Marcos Del Sol Vives <marcos@orca.pet>
# SPDX-License-Identifier: WTFPL

from collections import namedtuple
import leekoq
from unittest import TestCase, main

Vector = namedtuple('Vector', ('key', 'plain', 'cipher'))

# Test vectors from a EG301 chip
TEST_VECTORS = [
	Vector(0xBEEFDEADBEEFDEAD, 0x2000C022, 0x054C90C2)
]

class CryptoTest(TestCase):
	def test_decrypt(self):
		for vector in TEST_VECTORS:
			assert leekoq.decrypt(vector.cipher, vector.key) == vector.plain

	def test_encrypt(self):
		for vector in TEST_VECTORS:
			assert leekoq.encrypt(vector.plain, vector.key) == vector.cipher

if __name__ == '__main__':
	main()
