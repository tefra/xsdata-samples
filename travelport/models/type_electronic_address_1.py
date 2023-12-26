from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_email_format_1 import TypeEmailFormat1
from travelport.models.type_tckey_element import TypeTckeyElement

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeElectronicAddress1(TypeTckeyElement):
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
    format: None | TypeEmailFormat1 = field(
        default=None,
        metadata={
            "name": "Format",
            "type": "Attribute",
        },
    )
