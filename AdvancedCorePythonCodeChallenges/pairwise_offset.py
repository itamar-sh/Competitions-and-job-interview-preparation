from collections.abc import Sequence
from typing import TypeVar

T = TypeVar('T')      # Declare type variable

def pairwise_offset(sequence: Sequence[T], fillvalue="*", offset=0) -> Sequence[T]:
    seq = []
    for i in range(offset):
        seq.append((sequence[i], fillvalue))
    for i in range(len(sequence)):
        seq.append((sequence[i+offset], sequence[i]) if i + offset < len(sequence) else (fillvalue, sequence[i]))
    return seq

print(pairwise_offset(['a', 'b', 'c'], offset=1))
print(pairwise_offset(['a', 'b', 'c'], offset=2))
