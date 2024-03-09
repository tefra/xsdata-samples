from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate, XmlDateTime

from travelport.models.emd_availability_charge_indicator import (
    EmdAvailabilityChargeIndicator,
)
from travelport.models.emd_refund_reissue_indicator import (
    EmdRefundReissueIndicator,
)
from travelport.models.type_booking import TypeBooking
from travelport.models.type_display_category import TypeDisplayCategory

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Emd:
    """
    Parameters
    ----------
    fulfillment_type
        A one digit code specifying how the service must be fulfilled. See
        FulfillmentTypeDescription for the description of this value.
    fulfillment_type_description
        EMD description.
    associated_item
        The type of Optional Service.  The choices are Flight, Ticket,
        Merchandising, Rule Buster, Allowance, Chargeable Baggage, Carry On
        Baggage Allowance, Prepaid Baggage.  Provider: 1G, 1V, 1P
    availability_charge_indicator
        A one-letter code specifying whether the service is available or if
        there is a charge associated with it. X = Service not available F =
        No charge for service (free) and an EMD is not issued to reflect
        free service E = No charge for service (free) and an EMD is issued
        to reflect the free service. G = No charge for service (free),
        booking is not required and an EMD is not issued to reflect free
        service H = No charge for service (free), booking is not required,
        and an EMD is issued to reflect the free service. Blank = No
        application. Charges apply according to the data in the Service Fee
        fields.
    refund_reissue_indicator
        An attribute specifying whether the service is refundable or
        reissuable.
    commissionable
        True/False value to whether or not the service is comissionable.
    mileage_indicator
        True/False value to whether or not the service has miles.
    location
        3 letter location code where the service will be availed.
    date
        The date at which the service will be used.
    booking
        Holds the booking description for the service, e.g., SSR.
    display_category
        Describes when the service should be displayed.
    reusable
        Identifies if the service can be re-used towards a future purchase.
    """

    class Meta:
        name = "EMD"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    fulfillment_type: None | int = field(
        default=None,
        metadata={
            "name": "FulfillmentType",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 5,
        },
    )
    fulfillment_type_description: None | str = field(
        default=None,
        metadata={
            "name": "FulfillmentTypeDescription",
            "type": "Attribute",
        },
    )
    associated_item: None | str = field(
        default=None,
        metadata={
            "name": "AssociatedItem",
            "type": "Attribute",
        },
    )
    availability_charge_indicator: None | EmdAvailabilityChargeIndicator = (
        field(
            default=None,
            metadata={
                "name": "AvailabilityChargeIndicator",
                "type": "Attribute",
            },
        )
    )
    refund_reissue_indicator: None | EmdRefundReissueIndicator = field(
        default=None,
        metadata={
            "name": "RefundReissueIndicator",
            "type": "Attribute",
        },
    )
    commissionable: None | bool = field(
        default=None,
        metadata={
            "name": "Commissionable",
            "type": "Attribute",
        },
    )
    mileage_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "MileageIndicator",
            "type": "Attribute",
        },
    )
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Attribute",
        },
    )
    booking: None | TypeBooking = field(
        default=None,
        metadata={
            "name": "Booking",
            "type": "Attribute",
        },
    )
    display_category: None | TypeDisplayCategory = field(
        default=None,
        metadata={
            "name": "DisplayCategory",
            "type": "Attribute",
        },
    )
    reusable: None | bool = field(
        default=None,
        metadata={
            "name": "Reusable",
            "type": "Attribute",
        },
    )
