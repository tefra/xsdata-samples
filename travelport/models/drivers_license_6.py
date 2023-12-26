from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_element_status_7 import TypeElementStatus7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class DriversLicense6:
    """
    Details of drivers license.

    Parameters
    ----------
    key
    license_number
        The driving license number of the booking traveler.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        name = "DriversLicense"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    license_number: None | str = field(
        default=None,
        metadata={
            "name": "LicenseNumber",
            "type": "Attribute",
            "required": True,
        },
    )
    el_stat: None | TypeElementStatus7 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
