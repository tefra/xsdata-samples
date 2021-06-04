from dataclasses import dataclass, field
from typing import Optional
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.customer_ref import CustomerRef
from netex.models.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CustomerEligibilityVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "CustomerEligibility_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_ref: Optional[CustomerRef] = field(
        default=None,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
