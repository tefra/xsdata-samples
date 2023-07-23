from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.passenger_info_4 import PassengerInfo4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass
class Mcoinformation4:
    """
    Parameters
    ----------
    passenger_info
    mconumber
        The unique MCO number
    status
        Current status of the MCO
    mcotype
        The Type of MCO. Once of Agency Fee, Airline Service Fee, or
        Residual value from an Exchange.
    """
    class Meta:
        name = "MCOInformation"

    passenger_info: list[PassengerInfo4] = field(
        default_factory=list,
        metadata={
            "name": "PassengerInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        }
    )
    mconumber: None | str = field(
        default=None,
        metadata={
            "name": "MCONumber",
            "type": "Attribute",
        }
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        }
    )
    mcotype: None | str = field(
        default=None,
        metadata={
            "name": "MCOType",
            "type": "Attribute",
        }
    )
