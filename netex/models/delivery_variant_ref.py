from dataclasses import dataclass

from .delivery_variant_ref_structure import DeliveryVariantRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DeliveryVariantRef(DeliveryVariantRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
