from collections.abc import Iterable
from dataclasses import dataclass, field

from .frame_containment_structure import FrameContainmentStructure
from .priceable_object_version_structure import PriceGroup

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FarePricesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "farePricesInFrame_RelStructure"

    price_group: Iterable[PriceGroup] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
