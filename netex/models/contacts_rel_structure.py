from dataclasses import dataclass, field
from typing import Optional
from .contact import Contact
from .containment_aggregation_structure import ContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ContactsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "contacts_RelStructure"

    contact: Optional[Contact] = field(
        default=None,
        metadata={
            "name": "Contact",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
