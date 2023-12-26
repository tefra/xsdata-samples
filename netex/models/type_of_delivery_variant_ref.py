from dataclasses import dataclass
from .type_of_delivery_variant_ref_structure import (
    TypeOfDeliveryVariantRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TypeOfDeliveryVariantRef(TypeOfDeliveryVariantRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
