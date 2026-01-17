from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

from travelport.models.advtype import Advtype
from travelport.models.chgtype import Chgtype
from travelport.models.maxtype import Maxtype
from travelport.models.mintype import Mintype
from travelport.models.othtype import Othtype

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareRulesFilter:
    """
    Fare Rules Filter about this fare component.

    Applicable Providers are 1P,1G,1V.

    Parameters
    ----------
    refundability
        Refundability/Penalty Fare Rules about this fare component.
    latest_ticketing_time
        For Future Use
    chg
        For Penalties
    min
        For Minimum Stay
    max
        For Maximum Stay
    adv
        For Advance Res/Tkt
    oth
        Other
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    refundability: None | FareRulesFilter.Refundability = field(
        default=None,
        metadata={
            "name": "Refundability",
            "type": "Element",
        },
    )
    latest_ticketing_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "LatestTicketingTime",
            "type": "Element",
        },
    )
    chg: None | Chgtype = field(
        default=None,
        metadata={
            "name": "CHG",
            "type": "Element",
        },
    )
    min: None | Mintype = field(
        default=None,
        metadata={
            "name": "MIN",
            "type": "Element",
        },
    )
    max: None | Maxtype = field(
        default=None,
        metadata={
            "name": "MAX",
            "type": "Element",
        },
    )
    adv: None | Advtype = field(
        default=None,
        metadata={
            "name": "ADV",
            "type": "Element",
        },
    )
    oth: None | Othtype = field(
        default=None,
        metadata={
            "name": "OTH",
            "type": "Element",
        },
    )

    @dataclass
    class Refundability:
        """
        Parameters
        ----------
        value
            Currently returned: FullyRefundable (1G,1V),
            RefundableWithPenalty (1G,1V), Refundable (1P),  NonRefundable
            (1G,1V,1P).Refundable.
        """

        value: None | str = field(
            default=None,
            metadata={
                "name": "Value",
                "type": "Attribute",
                "required": True,
            },
        )
