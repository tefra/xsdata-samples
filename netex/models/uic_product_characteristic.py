from __future__ import annotations

from dataclasses import dataclass, field

from .uic_product_characteristic_enumeration import (
    UicProductCharacteristicEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class UicProductCharacteristic:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: None | UicProductCharacteristicEnumeration = field(
        default=None,
        metadata={
            "required": True,
        },
    )
