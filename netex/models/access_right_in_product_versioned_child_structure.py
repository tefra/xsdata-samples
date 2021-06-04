from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.fare_element_in_sequence_versioned_child_structure import FareElementInSequenceVersionedChildStructure
from netex.models.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.models.supplement_product_ref import SupplementProductRef
from netex.models.validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRightInProductVersionedChildStructure(FareElementInSequenceVersionedChildStructure):
    class Meta:
        name = "AccessRightInProduct_VersionedChildStructure"

    validable_element_ref: Optional[ValidableElementRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    supplement_product_ref: List[SupplementProductRef] = field(
        default_factory=list,
        metadata={
            "name": "SupplementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
        }
    )
    preassigned_fare_product_ref: Optional[PreassignedFareProductRef] = field(
        default=None,
        metadata={
            "name": "PreassignedFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
