from dataclasses import dataclass

from .priceable_object_ref_structure import PriceableObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class PriceableObjectRef(PriceableObjectRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
