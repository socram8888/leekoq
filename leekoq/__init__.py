# Copyright 2020 Marcos Del Sol Vives <marcos@orca.pet>
# SPDX-License-Identifier: WTFPL

"""
KeeLoq encryption and decryption.

KeeLoq is a propietary encryption algorithm developed for code-hopping remote key entry (RKE)
devices such as:

 - `Microchip HCS200 <http://ww1.microchip.com/downloads/en/devicedoc/40138c.pdf>`
 - `Microchip HCS301 <http://ww1.microchip.com/downloads/en/devicedoc/21143b.pdf>`
 - `EG Micro EG301 <https://www.egmicro.com/download/EG301_datasheet.pdf>`

Please note this algorithm is pretty weak and should not be used for any real crypto.
"""

from .leekoq import encrypt, decrypt
