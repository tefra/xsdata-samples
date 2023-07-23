from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from travelport.models.type_mct_connection import TypeMctConnection

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass
class MctException:
    """
    MCT Exception details.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    time: None | int = field(
        default=None,
        metadata={
            "name": "Time",
            "type": "Attribute",
            "required": True,
        }
    )
    arrive_station: None | str = field(
        default=None,
        metadata={
            "name": "ArriveStation",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        }
    )
    depart_station: None | str = field(
        default=None,
        metadata={
            "name": "DepartStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    connection: None | TypeMctConnection = field(
        default=None,
        metadata={
            "name": "Connection",
            "type": "Attribute",
            "required": True,
        }
    )
    arrive_carrier: None | str = field(
        default=None,
        metadata={
            "name": "ArriveCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    depart_carrier: None | str = field(
        default=None,
        metadata={
            "name": "DepartCarrier",
            "type": "Attribute",
            "length": 2,
        }
    )
    arrive_flight_range_begin: None | str = field(
        default=None,
        metadata={
            "name": "ArriveFlightRangeBegin",
            "type": "Attribute",
        }
    )
    arrive_flight_range_end: None | str = field(
        default=None,
        metadata={
            "name": "ArriveFlightRangeEnd",
            "type": "Attribute",
        }
    )
    depart_flight_range_begin: None | str = field(
        default=None,
        metadata={
            "name": "DepartFlightRangeBegin",
            "type": "Attribute",
        }
    )
    depart_flight_range_end: None | str = field(
        default=None,
        metadata={
            "name": "DepartFlightRangeEnd",
            "type": "Attribute",
        }
    )
    arrive_equipment: None | str = field(
        default=None,
        metadata={
            "name": "ArriveEquipment",
            "type": "Attribute",
        }
    )
    depart_equipment: None | str = field(
        default=None,
        metadata={
            "name": "DepartEquipment",
            "type": "Attribute",
        }
    )
    previous_station: None | str = field(
        default=None,
        metadata={
            "name": "PreviousStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    next_station: None | str = field(
        default=None,
        metadata={
            "name": "NextStation",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        }
    )
    previous_country: None | str = field(
        default=None,
        metadata={
            "name": "PreviousCountry",
            "type": "Attribute",
            "length": 2,
        }
    )
    next_country: None | str = field(
        default=None,
        metadata={
            "name": "NextCountry",
            "type": "Attribute",
            "length": 2,
        }
    )
    previous_state: None | str = field(
        default=None,
        metadata={
            "name": "PreviousState",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    next_state: None | str = field(
        default=None,
        metadata={
            "name": "NextState",
            "type": "Attribute",
            "max_length": 6,
        }
    )
    arrive_terminal: None | str = field(
        default=None,
        metadata={
            "name": "ArriveTerminal",
            "type": "Attribute",
        }
    )
    depart_terminal: None | str = field(
        default=None,
        metadata={
            "name": "DepartTerminal",
            "type": "Attribute",
        }
    )
    effective_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "EffectiveDate",
            "type": "Attribute",
        }
    )
    discontinue_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DiscontinueDate",
            "type": "Attribute",
        }
    )
