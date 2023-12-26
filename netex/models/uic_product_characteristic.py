from dataclasses import dataclass, field
from typing import Optional
from .uic_product_characteristic_enumeration import (
    UicProductCharacteristicEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UicProductCharacteristic:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: Optional[UicProductCharacteristicEnumeration] = field(
        default=None,
        metadata={
            "required": True,
        },
    )
