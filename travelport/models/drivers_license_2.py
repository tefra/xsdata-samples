from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_element_status_3 import TypeElementStatus3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class DriversLicense2:
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
        namespace = "http://www.travelport.com/schema/common_v32_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        }
    )
    license_number: None | str = field(
        default=None,
        metadata={
            "name": "LicenseNumber",
            "type": "Attribute",
            "required": True,
        }
    )
    el_stat: None | TypeElementStatus3 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        }
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        }
    )
