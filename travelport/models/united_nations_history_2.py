from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class UnitedNationsHistory2:
    """
    United Nations Form of Payments.
    """

    class Meta:
        name = "UnitedNationsHistory"
        namespace = "http://www.travelport.com/schema/uprofile_v37_0"

    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
        },
    )
