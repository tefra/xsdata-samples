from __future__ import annotations

from dataclasses import dataclass

from .type_of_delivery_variant_value_structure import (
    TypeOfDeliveryVariantValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfDeliveryVariant(TypeOfDeliveryVariantValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
