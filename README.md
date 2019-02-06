LeeKoq
======

This project is an open source pure Python 3 implementation of Microchip's KeeLoq propietary
encryption algorithm, used in their series of KeeLoq remote key entry (RKE) devices.

Amongst others, these devices include:

 - [Microchip HCS200](http://ww1.microchip.com/downloads/en/devicedoc/40138c.pdf)
 - [Microchip HCS301](http://ww1.microchip.com/downloads/en/devicedoc/21143b.pdf)
 - [Electronic Giant EG301](https://www.egmicro.com/download/EG301_datasheet.pdf)

Usage example
-------------

This project literally has two methods, so using it is pretty straightforward:

```
>>> import leekoq
>>> key = 0xCAFED00D
>>> cipher = leekoq.encrypt(0x12345678, key)
>>> hex(cipher)
'0x260afde3'
>>> plain = leekoq.decrypt(cipher, key)
>>> hex(plain)
'0x12345678'
```

Keys are 64-bit integers, and cipher- and plaintexts are 32-bit integers.

License
-------

The code of this project is licensed under the Do What The Fuck You Want License, version 2:

```
            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                    Version 2, December 2004

 Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

 Everyone is permitted to copy and distribute verbatim or modified
 copies of this license document, and changing it is allowed as long
 as the name is changed.

            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

  0. You just DO WHAT THE FUCK YOU WANT TO.
```

KeeLoq is a registered trademark of Microchip Technologies Inc.

Please note that neither the author is not affiliated with, nor this project is endorsed by
Microchip Technologies, Inc.
