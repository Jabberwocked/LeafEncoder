import numbers

class Validator():
    def isNumberType(value):
        if not isinstance(value, numbers.Integral):
            raise Exception('expected number, got:', type(value))

    def lenOfTuple(args, expectedAmount):
        if (len(args) != expectedAmount):
            raise Exception(expectedAmount, ' arguments expected, got:', len(args))

    def minValue(value, min):
        if (value < min):
            raise Exception('value should be bigger than: ', min, 'and was:', value)

    def maxValue(value, max):
        if (value > max):
            raise Exception('value should be smaller than: ', max, 'and was:', value)
