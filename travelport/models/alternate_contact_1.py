from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_contact_1 import TypeContact1
from travelport.models.type_taggable_address_1 import TypeTaggableAddress1
from travelport.models.type_taggable_electronic_address_1 import TypeTaggableElectronicAddress1
from travelport.models.type_taggable_phone_1 import TypeTaggablePhone1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class AlternateContact1(TypeContact1):
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
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    address: list[TypeTaggableAddress1] = field(
        default_factory=list,
        metadata={
            "name": "Address",
            "type": "Element",
        }
    )
    phone: list[TypeTaggablePhone1] = field(
        default_factory=list,
        metadata={
            "name": "Phone",
            "type": "Element",
        }
    )
    electronic_address: list[TypeTaggableElectronicAddress1] = field(
        default_factory=list,
        metadata={
            "name": "ElectronicAddress",
            "type": "Element",
        }
    )
