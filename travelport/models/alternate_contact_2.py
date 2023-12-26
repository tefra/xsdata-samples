from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_contact_2 import TypeContact2
from travelport.models.type_taggable_address_2 import TypeTaggableAddress2
from travelport.models.type_taggable_electronic_address_2 import (
    TypeTaggableElectronicAddress2,
)
from travelport.models.type_taggable_phone_2 import TypeTaggablePhone2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class AlternateContact2(TypeContact2):
    """
    Outside Contact information refering to relationships such as Emergency
    Contact.

    Parameters
    ----------
    address
        Contact Address
    phone
        Contact Phone
    electronic_address
        Contact Email
    """

    class Meta:
        name = "AlternateContact"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    address: list[TypeTaggableAddress2] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    phone: list[TypeTaggablePhone2] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    electronic_address: list[TypeTaggableElectronicAddress2] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
            "max_occurs": 999,
        },
    )
