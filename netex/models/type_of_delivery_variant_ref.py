from __future__ import annotations

from dataclasses import dataclass

from .type_of_delivery_variant_ref_structure import (
    TypeOfDeliveryVariantRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfDeliveryVariantRef(TypeOfDeliveryVariantRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
