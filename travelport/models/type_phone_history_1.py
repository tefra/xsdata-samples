from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_contact_purpose_1 import TypeContactPurpose1
from travelport.models.type_key_tagged_element_1 import TypeKeyTaggedElement1
from travelport.models.type_phone_type_1 import TypePhoneType1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypePhoneHistory1(TypeKeyTaggedElement1):
    """
    Profile Phone Number.

    Parameters
    ----------
    type_value
        The type of a phone.
    country
        The phone number's country code
    area_code
        The phone number's area code
    local_number
        The phone number
    extension
        The phone number's extension
    location
        The IATA airport/city code that corresponds to the location of the
        phone number.
    description
        An optional description detailing the phone number use.
    purpose
        A code for categorizing a contact mechanism based on purpose or use.
        Examples include business, persona., etc.
    provisioned
        Indicator to show if this phone is used as the provisioned phone.
    priority_order
        Priority order associated with this Phone.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """
    class Meta:
        name = "typePhoneHistory"

    type_value: None | TypePhoneType1 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    area_code: None | str = field(
        default=None,
        metadata={
            "name": "AreaCode",
            "type": "Attribute",
            "max_length": 5,
        }
    )
    local_number: None | str = field(
        default=None,
        metadata={
            "name": "LocalNumber",
            "type": "Attribute",
            "max_length": 50,
        }
    )
    extension: None | str = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    purpose: None | TypeContactPurpose1 = field(
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
