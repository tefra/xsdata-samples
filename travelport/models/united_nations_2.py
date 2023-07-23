from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofileCommon_v30_0"


@dataclass
class UnitedNations2:
    """
    United Nations Form of Payments.
    """
    class Meta:
        name = "UnitedNations"
        namespace = "http://www.travelport.com/schema/uprofileCommon_v30_0"

    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
