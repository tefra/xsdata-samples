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


@dataclass(kw_only=True)
class AcceptedPaymentCards:
    """
    Use this class to describe details in case acceptedMeansOfPayment is
    set to 'paymentCard'.

    :ivar payment_cards: List of accepted payment cards.
    :ivar other_payment_cards: Further accepted payment cards.
    :ivar payment_card_brands: List of accepted brands for payment
        cards.
    :ivar other_payment_card_brands: Further accepted brands of payment
        cards.
    :ivar accepted_payment_cards_extension:
    """

    payment_cards: list[PaymentCardTypesEnum] = field(
        default_factory=list,
        metadata={
            "name": "paymentCards",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    other_payment_cards: list[str] = field(
        default_factory=list,
        metadata={
            "name": "otherPaymentCards",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    payment_card_brands: list[PaymentCardBrandsEnum] = field(
        default_factory=list,
        metadata={
            "name": "paymentCardBrands",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    other_payment_card_brands: list[str] = field(
        default_factory=list,
        metadata={
            "name": "otherPaymentCardBrands",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    accepted_payment_cards_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "acceptedPaymentCardsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
