from collections.abc import Iterable
from dataclasses import dataclass, field

from .fare_contract import FareContract
from .frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareContractsInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "fareContractsInFrame_RelStructure"

    fare_contract: Iterable[FareContract] = field(
        default_factory=list,
        metadata={
            "name": "FareContract",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
