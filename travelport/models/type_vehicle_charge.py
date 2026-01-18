from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_vehicle_charge_included_in_rate import (
    TypeVehicleChargeIncludedInRate,
)
from travelport.models.type_vehicle_charge_type import TypeVehicleChargeType

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class TypeVehicleCharge:
    """
    Charges associated with a vehicle rental.

    Parameters
    ----------
    amount
        The amount of the charge.
    percentage
        The amount of the charge in percentage.
    category
        The type of charge information for the vehicle rental.
    name
        Identifies the type of charge information for the category. For 1P ,
        when category is “Special”, Name attribute will have Special
        Equipment code enumeration, which can be used in booking vehicle on
        1P host.
    description
        Special Equipment Charge description text of the rental charge. 1P
        only.
    type_value
        Used to specify how a charge is applied, such as per rental, per
        day, etc.
    included_in_rate
        Specifies whether the charge is included in the rate and if it is,
        if it is in the base or total rate.
    """

    class Meta:
        name = "typeVehicleCharge"

    amount: None | str = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
        },
    )
    percentage: None | str = field(
        default=None,
        metadata={
            "name": "Percentage",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "pattern": r"([0-9]{1,2}|100)\.[0-9]{1,2}",
        },
    )
    category: str = field(
        metadata={
            "name": "Category",
            "type": "Attribute",
            "required": True,
        }
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
        },
    )
    type_value: None | TypeVehicleChargeType = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    included_in_rate: None | TypeVehicleChargeIncludedInRate = field(
        default=None,
        metadata={
            "name": "IncludedInRate",
            "type": "Attribute",
        },
    )
