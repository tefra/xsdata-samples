from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_key_element_2 import TypeKeyElement2
from travelport.models.type_phone_type_2 import TypePhoneType2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypePhone2(TypeKeyElement2):
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
    description
        An optional description detailing the phone number use.
    location
        The IATA airport/city code that corresponds to the location of the
        phone number.
    """

    class Meta:
        name = "typePhone"

    type_value: None | TypePhoneType2 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    country: None | str = field(
        default=None,
        metadata={
            "name": "Country",
            "type": "Attribute",
            "max_length": 5,
        },
    )
    area_code: None | str = field(
        default=None,
        metadata={
            "name": "AreaCode",
            "type": "Attribute",
            "max_length": 5,
        },
    )
    local_number: None | str = field(
        default=None,
        metadata={
            "name": "LocalNumber",
            "type": "Attribute",
            "required": True,
            "max_length": 50,
        },
    )
    extension: None | str = field(
        default=None,
        metadata={
            "name": "Extension",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "max_length": 6,
        },
    )
