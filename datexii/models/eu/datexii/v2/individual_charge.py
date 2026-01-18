from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from datexii.models.eu.datexii.v2.charge_band_versioned_reference import (
    ChargeBandVersionedReference,
)
from datexii.models.eu.datexii.v2.currency_enum import CurrencyEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.means_of_payment_enum import (
    MeansOfPaymentEnum,
)
from datexii.models.eu.datexii.v2.used_payment_card import UsedPaymentCard

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class IndividualCharge:
    """
    Information on the individual charge for parking the specified vehicle.

    :ivar charge_band_reference: A reference to a charge band.
    :ivar charge_paid: The charge paid for this vehicle. If the vehicle
        is still parking, it's the charge amount accumulated so far.
    :ivar charge_currency: A three-character code according to ISO 4217
        for the currency in which the parking charge is specified (e.g.
        EUR, GBP, SEK, CZK).
    :ivar used_means_of_payment: The payment method used to pay for this
        parking vehicle. If it is 'paymentCard', use 'UsedPaymentCard'
        to specify more details.
    :ivar with_reservation: Specifies, whether there was a reservation
        made for this vehicle.
    :ivar used_payment_card:
    :ivar individual_charge_extension:
    """

    charge_band_reference: ChargeBandVersionedReference | None = field(
        default=None,
        metadata={
            "name": "chargeBandReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    charge_paid: Decimal | None = field(
        default=None,
        metadata={
            "name": "chargePaid",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    charge_currency: CurrencyEnum | None = field(
        default=None,
        metadata={
            "name": "chargeCurrency",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    used_means_of_payment: MeansOfPaymentEnum | None = field(
        default=None,
        metadata={
            "name": "usedMeansOfPayment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    with_reservation: bool | None = field(
        default=None,
        metadata={
            "name": "withReservation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    used_payment_card: UsedPaymentCard | None = field(
        default=None,
        metadata={
            "name": "usedPaymentCard",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    individual_charge_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "individualChargeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
