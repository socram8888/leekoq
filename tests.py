# Copyright 2019 Marcos Del Sol Vives <marcos@orca.pet>
# SPDX-License-Identifier: WTFPL

from collections import namedtuple
import leekoq
from unittest import TestCase

Vector = namedtuple('Vector', ('key', 'plain', 'cipher'))

# Test vectors from a EG301 chip
TEST_VECTORS = [
	Vector(0xBEEFDEADBEEFDEAD, 0x2000C022, 0x054C90C2)
]

class EncryptionTest(TestCase):
	def test(self):
		for vector in TEST_VECTORS:
			assert leekoq.encrypt(vector.plain, vector.key) == vector.cipher

class DecryptionTest(TestCase):
	def test(self):
		for vector in TEST_VECTORS:
			assert leekoq.decrypt(vector.cipher, vector.key) == vector.plain
