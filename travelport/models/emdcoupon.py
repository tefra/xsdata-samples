from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class Emdcoupon:
    """
    The coupon information for the EMD issued.

    Supported providers are 1G/1V/1P.

    Parameters
    ----------
    number
        Number of the EMD coupon
    status
        Status of the coupon. Possible values Open, Void, Refunded,
        Exchanged, Irregular Operations,Airport Control, Checked In,
        Flown/Used, Boarded/Lifted, Suspended, Unknown
    svc_description
        Description of the service related to the EMD Coupon
    consumed_at_issuance_ind
        Indicates if the EMD coupon has been considered used as soon as
        issued.
    rfic
        Reason For Issuance Code for the EMD coupon
    rfisc
        Reason For Issueance Sub code for the EMD coupon
    rfidescription
        Reason for Issueance Description for the EMD coupon
    origin
        Departure Airport Code for the flight with which the Coupon is
        associated
    destination
        Destination Airport Code for the flight with which the Coupon is
        associated
    flight_number
        Flight Number of the flight with which the coupon is associated.
    present_to
        Service provider to present the coupon to
    present_at
        Location of service provider where this coupon should be presented
        at
    non_refundable_ind
        Indicates whether the coupon is non-refundable
    marketing_carrier
        Marketing carrier associated with the coupon
    key
        System generated Key
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        name = "EMDCoupon"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    number: int = field(
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
        }
    )
    status: str = field(
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        }
    )
    svc_description: None | str = field(
        default=None,
        metadata={
            "name": "SvcDescription",
            "type": "Attribute",
        },
    )
    consumed_at_issuance_ind: None | bool = field(
        default=None,
        metadata={
            "name": "ConsumedAtIssuanceInd",
            "type": "Attribute",
        },
    )
    rfic: str = field(
        metadata={
            "name": "RFIC",
            "type": "Attribute",
            "required": True,
            "length": 1,
        }
    )
    rfisc: None | str = field(
        default=None,
        metadata={
            "name": "RFISC",
            "type": "Attribute",
        },
    )
    rfidescription: None | str = field(
        default=None,
        metadata={
            "name": "RFIDescription",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 86,
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    flight_number: None | str = field(
        default=None,
        metadata={
            "name": "FlightNumber",
            "type": "Attribute",
            "max_length": 5,
        },
    )
    present_to: None | str = field(
        default=None,
        metadata={
            "name": "PresentTo",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 71,
        },
    )
    present_at: None | str = field(
        default=None,
        metadata={
            "name": "PresentAt",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 71,
        },
    )
    non_refundable_ind: None | bool = field(
        default=None,
        metadata={
            "name": "NonRefundableInd",
            "type": "Attribute",
        },
    )
    marketing_carrier: None | str = field(
        default=None,
        metadata={
            "name": "MarketingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus1 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
