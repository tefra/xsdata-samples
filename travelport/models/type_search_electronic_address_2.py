from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_contact_purpose_2 import TypeContactPurpose2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeSearchElectronicAddress2:
    """
    The electronic address of the profile to search for.

    Parameters
    ----------
    address
        The address or account to search for.
    type_value
        Type of Electronic Address to search for
    purpose
        A code for categorizing a contact mechanism based on purpose or use.
        Examples include business, persona., etc.
    """
    class Meta:
        name = "typeSearchElectronicAddress"

    address: None | str = field(
        default=None,
        metadata={
            "name": "Address",
            "type": "Attribute",
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
    purpose: None | TypeContactPurpose2 = field(
        default=None,
        metadata={
            "name": "Purpose",
            "type": "Attribute",
        }
    )
