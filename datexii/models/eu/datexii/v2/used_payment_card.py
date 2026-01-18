from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.payment_card_brands_enum import (
    PaymentCardBrandsEnum,
)
from datexii.models.eu.datexii.v2.payment_card_types_enum import (
    PaymentCardTypesEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class UsedPaymentCard:
    """
    The used payment card for this parking vehicle.

    :ivar payment_card: Use this class to describe details in case
        usedMeansOfPayment is set to 'paymentCard'.
    :ivar other_payment_card: The payment card used for this parking
        vehicle in case the paymentCard attribute is set to 'other'.
    :ivar payment_card_brand: The payment card brand used for this
        parking vehicle.
    :ivar other_payment_card_brand: The payment card brand used for this
        parking vehicle in case the paymentCardBrand attribute is set to
        'other'.
    :ivar used_payment_card_extension:
    """

    payment_card: PaymentCardTypesEnum | None = field(
        default=None,
        metadata={
            "name": "paymentCard",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    other_payment_card: str | None = field(
        default=None,
        metadata={
            "name": "otherPaymentCard",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    payment_card_brand: PaymentCardBrandsEnum | None = field(
        default=None,
        metadata={
            "name": "paymentCardBrand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    other_payment_card_brand: str | None = field(
        default=None,
        metadata={
            "name": "otherPaymentCardBrand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    used_payment_card_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "usedPaymentCardExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
