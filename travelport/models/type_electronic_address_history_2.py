from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_contact_purpose_2 import TypeContactPurpose2
from travelport.models.type_email_format_2 import TypeEmailFormat2
from travelport.models.type_key_tagged_element_2 import TypeKeyTaggedElement2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeElectronicAddressHistory2(TypeKeyTaggedElement2):
    """
    Electronic address or account such as Email, Twitter, etc.

    Parameters
    ----------
    name
        Value of the address (e.g email address, twitter account, etc.)
    type_value
        Type of address (Home, Business, etc)
    format
        Type of address (HTML, PDF, Text, etc)
    purpose
        A code for categorizing a contact mechanism based on purpose or use.
        Examples include business, persona., etc.
    provisioned
        Indicator to show if this electronic address is used as the
        provisioned electronic address.
    priority_order
        Priority order associated with this Electronic address.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """
    class Meta:
        name = "typeElectronicAddressHistory"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 1000,
        }
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        }
    )
    format: TypeEmailFormat2 = field(
        default=TypeEmailFormat2.HTML,
        metadata={
            "name": "Format",
            "type": "Attribute",
        }
    )
    purpose: None | TypeContactPurpose2 = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
    provisioned: None | bool = field(
        default=None,
        metadata={
            "name": "Provisioned",
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
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )
