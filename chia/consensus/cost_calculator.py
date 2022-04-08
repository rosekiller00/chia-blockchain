from dataclasses import dataclass
from typing import Optional

from chia_rs import PySpendBundleConditions

from chia.util.ints import uint16, uint64
from chia.util.streamable import Streamable, streamable


@streamable
@dataclass(frozen=True)
class NPCResult(Streamable):
    error: Optional[uint16]
    conds: Optional[PySpendBundleConditions]
    cost: uint64  # The total cost of the block, including CLVM cost, cost of
    # conditions and cost of bytes
