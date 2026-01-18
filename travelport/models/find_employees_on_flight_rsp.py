from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

from travelport.models.base_rsp_1 import BaseRsp1
from travelport.models.name_1 import Name1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class FindEmployeesOnFlightRsp(BaseRsp1):
    """
    Response to retrieve the number of employees in a flight.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    employees_on_flight: list[FindEmployeesOnFlightRsp.EmployeesOnFlight] = (
        field(
            default_factory=list,
            metadata={
                "name": "EmployeesOnFlight",
                "type": "Element",
                "max_occurs": 999,
            },
        )
    )

    @dataclass(kw_only=True)
    class EmployeesOnFlight:
        """
        Parameters
        ----------
        name
        universal_record_locator
            UniversalRecord Locator
        destination
            Airsegment Destination
        origin
            Airsegment Origin
        departure_date
            Airsegment departure date
        flight_number
            Air segment flight number
        carrier
            Air Segment Carrier
        """

        name: list[Name1] = field(
            default_factory=list,
            metadata={
                "name": "Name",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
                "min_occurs": 1,
                "max_occurs": 999,
            },
        )
        universal_record_locator: str = field(
            metadata={
                "name": "UniversalRecordLocator",
                "type": "Attribute",
                "required": True,
                "min_length": 5,
                "max_length": 8,
            }
        )
        destination: str = field(
            metadata={
                "name": "Destination",
                "type": "Attribute",
                "required": True,
                "length": 3,
                "white_space": "collapse",
            }
        )
        origin: str = field(
            metadata={
                "name": "Origin",
                "type": "Attribute",
                "required": True,
                "length": 3,
                "white_space": "collapse",
            }
        )
        departure_date: XmlDate = field(
            metadata={
                "name": "DepartureDate",
                "type": "Attribute",
                "required": True,
            }
        )
        flight_number: str = field(
            metadata={
                "name": "FlightNumber",
                "type": "Attribute",
                "required": True,
            }
        )
        carrier: str = field(
            metadata={
                "name": "Carrier",
                "type": "Attribute",
                "required": True,
                "length": 2,
            }
        )
