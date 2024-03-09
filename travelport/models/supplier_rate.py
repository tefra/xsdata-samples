from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_vehicle_rates import TypeVehicleRates

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass
class SupplierRate(TypeVehicleRates):
    """
    Parameters
    ----------
    discount_amount
        Discount Amount 1P only
    mandatory_charge_total
        Total Mandatory Charges, which may include taxes, surcharges, and
        fees. 1P only.
    approximate_total
        The total sum of all mandatory, optional and conditional charges
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    discount_amount: None | str = field(
        default=None,
        metadata={
            "name": "DiscountAmount",
            "type": "Attribute",
        },
    )
    mandatory_charge_total: None | str = field(
        default=None,
        metadata={
            "name": "MandatoryChargeTotal",
            "type": "Attribute",
        },
    )
    approximate_total: None | str = field(
        default=None,
        metadata={
            "name": "ApproximateTotal",
            "type": "Attribute",
        },
    )
