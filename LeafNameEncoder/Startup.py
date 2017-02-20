#!/usr/bin/env python
from LeafNameEncoder.BinaryConverter import BinaryConverter


def getTotalSize() -> int:
    """
    Gets the total number of bytes available for a leaf.
    :return:
    """
    return 8*7

def main():
    print(getTotalSize())


if __name__ == '__main__':
    main()