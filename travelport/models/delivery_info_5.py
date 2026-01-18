from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.email_5 import Email5
from travelport.models.general_remark_5 import GeneralRemark5
from travelport.models.phone_number_6 import PhoneNumber6
from travelport.models.provider_reservation_info_ref_6 import (
    ProviderReservationInfoRef6,
)
from travelport.models.type_structured_address_6 import TypeStructuredAddress6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v34_0"


@dataclass(kw_only=True)
class DeliveryInfo5:
    """
    Container to encapsulate all delivery related information.

    Parameters
    ----------
    shipping_address
    phone_number
    email
    general_remark
    provider_reservation_info_ref
        Tagging provider reservation info with Delivery Info.
    type_value
        An arbitrary identifier to categorize this delivery info
    signature_required
        Indicates whether a signature shoud be required in order to make the
        delivery.
    tracking_number
        The tracking number of the shipping company making the delivery.
    """

    class Meta:
        name = "DeliveryInfo"
        namespace = "http://www.travelport.com/schema/common_v34_0"

    shipping_address: None | TypeStructuredAddress6 = field(
        default=None,
        metadata={
            "name": "ShippingAddress",
            "type": "Element",
        },
    )
    phone_number: None | PhoneNumber6 = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
        },
    )
    email: None | Email5 = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
        },
    )
    general_remark: list[GeneralRemark5] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    provider_reservation_info_ref: list[ProviderReservationInfoRef6] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    signature_required: None | str = field(
        default=None,
        metadata={
            "name": "SignatureRequired",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    tracking_number: None | str = field(
        default=None,
        metadata={
            "name": "TrackingNumber",
            "type": "Attribute",
        },
    )
