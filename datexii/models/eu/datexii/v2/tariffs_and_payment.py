from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from xsdata.models.datatype import XmlDateTime

from datexii.models.eu.datexii.v2.accepted_payment_cards import (
    AcceptedPaymentCards,
)
from datexii.models.eu.datexii.v2.charge_band import ChargeBand
from datexii.models.eu.datexii.v2.charge_band_by_reference import (
    ChargeBandByReference,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.means_of_payment_enum import (
    MeansOfPaymentEnum,
)
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.parking_payment_mode_enum import (
    ParkingPaymentModeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TariffsAndPayment:
    """
    A table of charges under various conditions, primary used for parking.

    :ivar last_updated: The date/time at which this information was last
        updated.
    :ivar accepted_means_of_payment: Method(s) by which the user can
        make payments. In case of 'paymentCard' use AcceptedPaymentCards
        to specify more details.
    :ivar payment_mode: Modes how to realize the payment
        ('payAndDisplay', 'payByPrepaidToken', ...).
    :ivar payment_additional_description: Additional description, for
        instance instructions or telephone number for paying by SMS.
    :ivar free_of_charge: No fee at all. In this case, no further
        elements of the tariffs structure are needed.
    :ivar reservation_fee: A fee for reservation, if this is uniform for
        all situations. Can also be 0 to indicate free reservations.
        This attribute does not indicate if reservation is available at
        all and/or mandatory.
    :ivar url_link_address: A Uniform Resource Locator (URL) address
        pointing to a resource available on the Internet from where
        further relevant information may be obtained.
    :ivar charge_band:
    :ivar charge_band_by_reference:
    :ivar accepted_payment_cards:
    :ivar tariffs_and_payment_extension:
    """

    last_updated: XmlDateTime | None = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    accepted_means_of_payment: list[MeansOfPaymentEnum] = field(
        default_factory=list,
        metadata={
            "name": "acceptedMeansOfPayment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    payment_mode: list[ParkingPaymentModeEnum] = field(
        default_factory=list,
        metadata={
            "name": "paymentMode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    payment_additional_description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "paymentAdditionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    free_of_charge: bool | None = field(
        default=None,
        metadata={
            "name": "freeOfCharge",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    reservation_fee: Decimal | None = field(
        default=None,
        metadata={
            "name": "reservationFee",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "total_digits": 8,
            "fraction_digits": 2,
        },
    )
    url_link_address: str | None = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    charge_band: list[ChargeBand] = field(
        default_factory=list,
        metadata={
            "name": "chargeBand",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    charge_band_by_reference: list[ChargeBandByReference] = field(
        default_factory=list,
        metadata={
            "name": "chargeBandByReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    accepted_payment_cards: AcceptedPaymentCards | None = field(
        default=None,
        metadata={
            "name": "acceptedPaymentCards",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    tariffs_and_payment_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "tariffsAndPaymentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
