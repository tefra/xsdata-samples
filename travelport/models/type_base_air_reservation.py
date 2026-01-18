from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.air_exchange_bundle import AirExchangeBundle
from travelport.models.air_exchange_bundle_total import AirExchangeBundleTotal
from travelport.models.air_pricing_info import AirPricingInfo
from travelport.models.air_segment import AirSegment
from travelport.models.associated_remark_1 import AssociatedRemark1
from travelport.models.base_reservation_1 import BaseReservation1
from travelport.models.booking_traveler_ref_1 import BookingTravelerRef1
from travelport.models.credit_card_auth_1 import CreditCardAuth1
from travelport.models.document_info import DocumentInfo
from travelport.models.fare_note import FareNote
from travelport.models.fee_info import FeeInfo
from travelport.models.optional_services import OptionalServices
from travelport.models.payment_1 import Payment1
from travelport.models.pocket_itinerary_remark import PocketItineraryRemark
from travelport.models.provider_reservation_info_ref_1 import (
    ProviderReservationInfoRef1,
)
from travelport.models.supplier_locator_1 import SupplierLocator1
from travelport.models.svc_segment import SvcSegment
from travelport.models.third_party_information_1 import ThirdPartyInformation1
from travelport.models.ticketing_modifiers import TicketingModifiers
from travelport.models.type_tax_info_with_payment_ref import (
    TypeTaxInfoWithPaymentRef,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TypeBaseAirReservation(BaseReservation1):
    """
    Parent Container for Air Reservation.

    Parameters
    ----------
    optional_services
    supplier_locator
    third_party_information
    document_info
    booking_traveler_ref
    provider_reservation_info_ref
    air_segment
    svc_segment
        Service segment added to collect additional fee. 1P only
    air_pricing_info
    payment
    credit_card_auth
    fare_note
    fee_info
    tax_info
        Itinerary level taxes
    ticketing_modifiers
    associated_remark
    pocket_itinerary_remark
    air_exchange_bundle_total
    air_exchange_bundle
        Bundle exchange, pricing, and penalty information. Providers
        ACH/1G/1V/1P
    """

    class Meta:
        name = "typeBaseAirReservation"

    optional_services: None | OptionalServices = field(
        default=None,
        metadata={
            "name": "OptionalServices",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    supplier_locator: list[SupplierLocator1] = field(
        default_factory=list,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    third_party_information: list[ThirdPartyInformation1] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyInformation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    document_info: None | DocumentInfo = field(
        default=None,
        metadata={
            "name": "DocumentInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    booking_traveler_ref: list[BookingTravelerRef1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    provider_reservation_info_ref: list[ProviderReservationInfoRef1] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    air_segment: list[AirSegment] = field(
        default_factory=list,
        metadata={
            "name": "AirSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    svc_segment: list[SvcSegment] = field(
        default_factory=list,
        metadata={
            "name": "SvcSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    air_pricing_info: list[AirPricingInfo] = field(
        default_factory=list,
        metadata={
            "name": "AirPricingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    payment: list[Payment1] = field(
        default_factory=list,
        metadata={
            "name": "Payment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    credit_card_auth: list[CreditCardAuth1] = field(
        default_factory=list,
        metadata={
            "name": "CreditCardAuth",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    fare_note: list[FareNote] = field(
        default_factory=list,
        metadata={
            "name": "FareNote",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    fee_info: list[FeeInfo] = field(
        default_factory=list,
        metadata={
            "name": "FeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    tax_info: list[TypeTaxInfoWithPaymentRef] = field(
        default_factory=list,
        metadata={
            "name": "TaxInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    ticketing_modifiers: list[TicketingModifiers] = field(
        default_factory=list,
        metadata={
            "name": "TicketingModifiers",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    associated_remark: list[AssociatedRemark1] = field(
        default_factory=list,
        metadata={
            "name": "AssociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    pocket_itinerary_remark: list[PocketItineraryRemark] = field(
        default_factory=list,
        metadata={
            "name": "PocketItineraryRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    air_exchange_bundle_total: None | AirExchangeBundleTotal = field(
        default=None,
        metadata={
            "name": "AirExchangeBundleTotal",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
        },
    )
    air_exchange_bundle: list[AirExchangeBundle] = field(
        default_factory=list,
        metadata={
            "name": "AirExchangeBundle",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
