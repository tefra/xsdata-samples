from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.email_3 import Email3
from travelport.models.general_remark_3 import GeneralRemark3
from travelport.models.phone_number_4 import PhoneNumber4
from travelport.models.provider_reservation_info_ref_4 import (
    ProviderReservationInfoRef4,
)
from travelport.models.type_structured_address_4 import TypeStructuredAddress4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass(kw_only=True)
class DeliveryInfo3:
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
        namespace = "http://www.travelport.com/schema/common_v33_0"

    shipping_address: None | TypeStructuredAddress4 = field(
        default=None,
        metadata={
            "name": "ShippingAddress",
            "type": "Element",
        },
    )
    phone_number: None | PhoneNumber4 = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
        },
    )
    email: None | Email3 = field(
        default=None,
        metadata={
            "name": "Email",
            "type": "Element",
        },
    )
    general_remark: list[GeneralRemark3] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    provider_reservation_info_ref: list[ProviderReservationInfoRef4] = field(
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
