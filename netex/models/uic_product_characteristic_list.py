from collections.abc import Iterable
from dataclasses import dataclass, field

from .uic_product_characteristic_enumeration import (
    UicProductCharacteristicEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UicProductCharacteristicList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Iterable[UicProductCharacteristicEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
