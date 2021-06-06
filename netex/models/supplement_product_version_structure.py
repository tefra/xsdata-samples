from dataclasses import dataclass, field
from typing import Optional
from .fare_product_ref_structure import FareProductRefStructure
from .fare_product_refs_rel_structure import FareProductRefsRelStructure
from .preassigned_fare_product_version_structure import PreassignedFareProductVersionStructure
from .supplement_product_enumeration import SupplementProductEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SupplementProductVersionStructure(PreassignedFareProductVersionStructure):
    class Meta:
        name = "SupplementProduct_VersionStructure"

    supplement_product_type: Optional[SupplementProductEnumeration] = field(
        default=None,
        metadata={
            "name": "SupplementProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    supplement_to_fare_product_ref: Optional[FareProductRefStructure] = field(
        default=None,
        metadata={
            "name": "SupplementToFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    supplement_to: Optional[FareProductRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "supplementTo",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
