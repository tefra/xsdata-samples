from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.penalty_2 import Penalty2

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ChargesRules:
    """
    Fare Reference associated with the BookingRules.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    voluntary_changes: list[ChargesRules.VoluntaryChanges] = field(
        default_factory=list,
        metadata={
            "name": "VoluntaryChanges",
            "type": "Element",
            "max_occurs": 999,
        }
    )
    voluntary_refunds: list[ChargesRules.VoluntaryRefunds] = field(
        default_factory=list,
        metadata={
            "name": "VoluntaryRefunds",
            "type": "Element",
            "max_occurs": 999,
        }
    )

    @dataclass
    class VoluntaryChanges:
        penalty: None | Penalty2 = field(
            default=None,
            metadata={
                "name": "Penalty",
                "type": "Element",
            }
        )
        vol_change_ind: None | bool = field(
            default=None,
            metadata={
                "name": "VolChangeInd",
                "type": "Attribute",
            }
        )

    @dataclass
    class VoluntaryRefunds:
        penalty: None | Penalty2 = field(
            default=None,
            metadata={
                "name": "Penalty",
                "type": "Element",
            }
        )
        vol_change_ind: None | bool = field(
            default=None,
            metadata={
                "name": "VolChangeInd",
                "type": "Attribute",
            }
        )
