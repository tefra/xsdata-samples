from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.fare_status_failure_info import FareStatusFailureInfo
from travelport.models.type_fare_status_code import TypeFareStatusCode

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FareStatus:
    """
    Denotes the status of a particular fare.

    Parameters
    ----------
    fare_status_failure_info
    code
        The status of the fare.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fare_status_failure_info: None | FareStatusFailureInfo = field(
        default=None,
        metadata={
            "name": "FareStatusFailureInfo",
            "type": "Element",
        },
    )
    code: None | TypeFareStatusCode = field(
        default=None,
        metadata={
            "name": "Code",
            "type": "Attribute",
            "required": True,
        },
    )
