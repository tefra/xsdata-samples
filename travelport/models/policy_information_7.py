from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.remark_8 import Remark8
from travelport.models.type_policy_6 import TypePolicy6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class PolicyInformation7:
    """
    Policy Information required for File Finishing.

    Parameters
    ----------
    reason_code
        Reason Code
    type_value
        Policy Type - Air, Hotel, Car, Rail, Ticketing
    name
        Policy Name
    out_of_policy
        In Policy / Out of Policy Indicator
    segment_ref
    """

    class Meta:
        name = "PolicyInformation"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    reason_code: None | PolicyInformation7.ReasonCode = field(
        default=None,
        metadata={
            "name": "ReasonCode",
            "type": "Element",
        },
    )
    type_value: None | TypePolicy6 = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        },
    )
    name: None | object = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    out_of_policy: None | bool = field(
        default=None,
        metadata={
            "name": "OutOfPolicy",
            "type": "Attribute",
        },
    )
    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        },
    )

    @dataclass
    class ReasonCode:
        """
        Parameters
        ----------
        out_of_policy
            Reason Code - Out of Policy
        purpose_of_trip
            Reason Code -Purpose of Trip
        remark
        """

        out_of_policy: None | str = field(
            default=None,
            metadata={
                "name": "OutOfPolicy",
                "type": "Element",
            },
        )
        purpose_of_trip: None | str = field(
            default=None,
            metadata={
                "name": "PurposeOfTrip",
                "type": "Element",
            },
        )
        remark: None | Remark8 = field(
            default=None,
            metadata={
                "name": "Remark",
                "type": "Element",
            },
        )
