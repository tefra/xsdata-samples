from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_email_format_2 import TypeEmailFormat2
from travelport.models.type_key_element_2 import TypeKeyElement2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeElectronicAddress2(TypeKeyElement2):
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
    """

    class Meta:
        name = "typeElectronicAddress"

    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 255,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 128,
        },
    )
    format: None | TypeEmailFormat2 = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Attribute",
        },
    )
