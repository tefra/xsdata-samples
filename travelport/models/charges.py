from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass(kw_only=True)
class Charges:
    """
    Container for various Charges assocaited with the Cruise Booking.

    Parameters
    ----------
    air_charge
        Total Amount of Air Charges associated with Cruise
    optional_charge
        Total Amount of Optional Charges associated with Cruise
    waiver_charge
        Total Waiver/Insurance charges associated with Cruise
    waiver_charge_type
        Use to determine if the amount is Waiver Charges or Insurance
        Charges.(Values - Waiver/Insurance)
    port_charge
        Amount of Port tax associated with Cruise
    port_charge_description
        Text explaining Port charges
    penalty_charge
        Amount of penalty charged with Cruise
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    air_charge: None | str = field(
        default=None,
        metadata={
            "name": "AirCharge",
            "type": "Attribute",
        },
    )
    optional_charge: None | str = field(
        default=None,
        metadata={
            "name": "OptionalCharge",
            "type": "Attribute",
        },
    )
    waiver_charge: None | str = field(
        default=None,
        metadata={
            "name": "WaiverCharge",
            "type": "Attribute",
        },
    )
    waiver_charge_type: None | str = field(
        default=None,
        metadata={
            "name": "WaiverChargeType",
            "type": "Attribute",
            "length": 1,
        },
    )
    port_charge: None | str = field(
        default=None,
        metadata={
            "name": "PortCharge",
            "type": "Attribute",
        },
    )
    port_charge_description: None | str = field(
        default=None,
        metadata={
            "name": "PortChargeDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 13,
        },
    )
    penalty_charge: None | str = field(
        default=None,
        metadata={
            "name": "PenaltyCharge",
            "type": "Attribute",
        },
    )
