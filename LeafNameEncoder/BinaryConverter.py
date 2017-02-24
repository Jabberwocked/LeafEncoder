import string
digs = string.ascii_letters + string.digits + string.punctuation

from bitarray import bitarray

class BinaryConverter():

    def from_u_number_to_bit_array(self, value, length) -> bitarray:
        return bitarray("{0:b}".format(value).zfill(length))


    def from_bit_array_to_u_number(self, value) -> int:
        return int(value.to01(), 2)

    def from_bit_array_to_base_encoded_string(self, value) -> string:
        result = self.from_bit_array_to_u_number(value)
        return self.from_u_number_to_base_encoded_string(result, len(digs))

    def from_base_encoded_string_to_bit_array(self, value) -> bitarray:
        number = 0;
        for idx, char in enumerate(list(reversed(value))):
            number += digs.find(char) * (len(digs)**(idx))
        return self.from_u_number_to_bit_array(number, 0)

    def from_u_number_to_base_encoded_string(self, x, base) -> string:
        digits = []
        while x:
            digits.append(digs[x % base])
            x //= base
        digits.reverse()
        return ''.join(digits)