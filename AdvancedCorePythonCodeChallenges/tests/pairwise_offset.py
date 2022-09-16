from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')      # Declare type variable

def pairwise_offset(sequence: Sequence[T], fillvalue="*", offset=0) -> Sequence[T]:
    seq = []
    for i in range(offset):
        seq.append((sequence[i], fillvalue) if i < len(sequence) else (fillvalue, fillvalue))
    for i in range(len(sequence)):
        seq.append((sequence[i+offset], sequence[i]) if i + offset < len(sequence) else (fillvalue, sequence[i]))
    return seq

if __name__ == '__main__':

    print(pairwise_offset(['a', 'b', 'c'], offset=1))
    print(pairwise_offset(['a', 'b', 'c'], offset=2))
    actual = list(pairwise_offset('abcde'))
    expected = [('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd'), ('e', 'e')]
    assert expected == actual