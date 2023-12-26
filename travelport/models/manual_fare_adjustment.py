from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from travelport.models.type_adjustment_target import TypeAdjustmentTarget
from travelport.models.type_adjustment_type import TypeAdjustmentType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ManualFareAdjustment:
    """
    Parameters
    ----------
    applied_on
        Represents pricing component upon which manual increment/discount to
        be applied. Presently supported values are Base and Total. Other is
        present as a future place holder but presently no request processing
        logic is available for value Other
    adjustment_type
        Represents process used for applying manual discount/increment.
        Presently supported values are Flat, Percentage.
    value
        Represents value of increment/discount applied. Negative value is
        considered as discount whereas positive value represents increment
    passenger_ref
        Represents passenger association.
    ticket_designator
        Providers: 1p
    fare_type
        Providers: 1p
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    applied_on: None | TypeAdjustmentTarget = field(
        default=None,
        metadata={
            "name": "AppliedOn",
            "type": "Attribute",
            "required": True,
        },
    )
    adjustment_type: None | TypeAdjustmentType = field(
        default=None,
        metadata={
            "name": "AdjustmentType",
            "type": "Attribute",
            "required": True,
        },
    )
    value: None | Decimal = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Attribute",
            "required": True,
        },
    )
    passenger_ref: None | str = field(
        default=None,
        metadata={
            "name": "PassengerRef",
            "type": "Attribute",
        },
    )
    ticket_designator: None | str = field(
        default=None,
        metadata={
            "name": "TicketDesignator",
            "type": "Attribute",
            "min_length": 0,
            "max_length": 20,
        },
    )
    fare_type: None | str = field(
        default=None,
        metadata={
            "name": "FareType",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
