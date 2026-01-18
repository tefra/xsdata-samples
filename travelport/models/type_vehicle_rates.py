from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class TypeVehicleRates:
    """
    Parameters
    ----------
    estimated_total_amount
        The estimated total amount
    base_rate
        Rate for the entire rent without the required charges
    rate_for_period
        The rate for the period
    drop_off_charge
        The additional fee for dropping off a vehicle at a different
        location.
    young_driver_charge
        The additional amount charged for young drivers
    senior_driver_charge
        The additional amount charged for senior drivers
    fuel_surcharge
        The additional amount charged for fuel
    extra_mileage_charge
        Cost per mile over allowance for rate
    pay_now
        Pay Now is added for Future Functionality
    pay_later
        Pay later is added for Future Functionality
    """

    class Meta:
        name = "typeVehicleRates"

    estimated_total_amount: None | str = field(
        default=None,
        metadata={
            "name": "EstimatedTotalAmount",
            "type": "Attribute",
        },
    )
    base_rate: None | str = field(
        default=None,
        metadata={
            "name": "BaseRate",
            "type": "Attribute",
        },
    )
    rate_for_period: None | str = field(
        default=None,
        metadata={
            "name": "RateForPeriod",
            "type": "Attribute",
        },
    )
    drop_off_charge: None | str = field(
        default=None,
        metadata={
            "name": "DropOffCharge",
            "type": "Attribute",
        },
    )
    young_driver_charge: None | str = field(
        default=None,
        metadata={
            "name": "YoungDriverCharge",
            "type": "Attribute",
        },
    )
    senior_driver_charge: None | str = field(
        default=None,
        metadata={
            "name": "SeniorDriverCharge",
            "type": "Attribute",
        },
    )
    fuel_surcharge: None | str = field(
        default=None,
        metadata={
            "name": "FuelSurcharge",
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
    pay_now: None | str = field(
        default=None,
        metadata={
            "name": "PayNow",
            "type": "Attribute",
        },
    )
    pay_later: None | str = field(
        default=None,
        metadata={
            "name": "PayLater",
            "type": "Attribute",
        },
    )
