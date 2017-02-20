import string
digs = string.ascii_letters + string.digits + string.punctuation

from bitarray import bitarray

class BinaryConverter():

    def fromUNumber(self, value, length) -> bitarray:
        return "{0:b}".format(value).zfill(length)


    def toUNumber(self, value) -> int:
        return int(value, 2)


    def toAsciiString(self,value) -> string:
        result = int.from_bytes(value.tobytes(), byteorder='big')
        return self.int2base(result, len(digs) )

    def int2base(self, x, base):
        digits = []
        while x:
            digits.append(digs[x % base])
            x //= base

        digits.reverse()
        return ''.join(digits)