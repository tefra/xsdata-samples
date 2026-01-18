from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_rental_period_rental_unit import (
    TypeRentalPeriodRentalUnit,
)

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class TypeRentalPeriod:
    """
    Rental period information concerning minimum and max rental periods.

    Parameters
    ----------
    rental_unit
        The rental unit period, such as days or hours.
    length
        The number of rental units.
    requirement_passed
        If true, the rental period requirements have been met.
    """

    class Meta:
        name = "typeRentalPeriod"

    rental_unit: TypeRentalPeriodRentalUnit = field(
        metadata={
            "name": "RentalUnit",
            "type": "Attribute",
            "required": True,
        }
    )
    length: int = field(
        metadata={
            "name": "Length",
            "type": "Attribute",
            "required": True,
        }
    )
    requirement_passed: None | bool = field(
        default=None,
        metadata={
            "name": "RequirementPassed",
            "type": "Attribute",
        },
    )
