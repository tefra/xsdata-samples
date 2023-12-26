from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.flight_criteria import FlightCriteria

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class FindEmployeesOnFlightReq(BaseReq1):
    """
    Request to retrieve the number of employees in a flight.

    Parameters
    ----------
    flight_criteria
    account_id
        Identifier of the account owner of the employees
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    flight_criteria: list[FlightCriteria] = field(
        default_factory=list,
        metadata={
            "name": "FlightCriteria",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    account_id: None | int = field(
        default=None,
        metadata={
            "name": "AccountID",
            "type": "Attribute",
            "required": True,
        },
    )
