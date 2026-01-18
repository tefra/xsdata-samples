from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_distance import TypeDistance

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class TypeRateInfo:
    """
    Additional information for extra days or hours.

    Parameters
    ----------
    rate_for_period
        The rate for the period
    number_of_periods
        Define how many periods (e.g. number of days or weeks)
    unlimited_mileage
        True if unlimited miles allowed. Not set if unknown
    mileage_allowance
        Number of miles or kilometers allowed for rate if not unlimited
    units
        Describes distance units for MileageAllowance or ExtraMileageCharge
    extra_mileage_charge
        Cost per mile or kilometer over allowance for rate
    """

    class Meta:
        name = "typeRateInfo"

    rate_for_period: None | str = field(
        default=None,
        metadata={
            "name": "RateForPeriod",
            "type": "Attribute",
        },
    )
    number_of_periods: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfPeriods",
            "type": "Attribute",
        },
    )
    unlimited_mileage: None | bool = field(
        default=None,
        metadata={
            "name": "UnlimitedMileage",
            "type": "Attribute",
        },
    )
    mileage_allowance: None | int = field(
        default=None,
        metadata={
            "name": "MileageAllowance",
            "type": "Attribute",
        },
    )
    units: None | TypeDistance = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Attribute",
        },
    )
    extra_mileage_charge: None | str = field(
        default=None,
        metadata={
            "name": "ExtraMileageCharge",
            "type": "Attribute",
        },
    )
