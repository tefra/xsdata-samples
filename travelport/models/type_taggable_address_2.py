from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.tag_ref_2 import TagRef2
from travelport.models.type_address_2 import TypeAddress2
from travelport.models.type_contact_purpose_2 import TypeContactPurpose2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeTaggableAddress2(TypeAddress2):
    """
    Base type of an address that is taggable.

    Parameters
    ----------
    tag_ref
    delivery_description
        An optional description detailing the delivery.
    purpose
        A code for categorizing a contact mechanism based on purpose or use.
        Examples include business, persona., etc.
    priority_order
        Priority order associated with this Address.
    """
    class Meta:
        name = "typeTaggableAddress"

    tag_ref: list[TagRef2] = field(
        default_factory=list,
        metadata={
            "name": "TagRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "max_occurs": 999,
        }
    )
    delivery_description: None | str = field(
        default=None,
        metadata={
            "name": "DeliveryDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    purpose: None | TypeContactPurpose2 = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
