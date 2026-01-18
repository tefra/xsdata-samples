from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.accounting_remark_1 import AccountingRemark1
from travelport.models.action_status_1 import ActionStatus1
from travelport.models.agency_contact_info_1 import AgencyContactInfo1
from travelport.models.agency_info_1 import AgencyInfo1
from travelport.models.air_reservation import AirReservation
from travelport.models.applied_profile_1 import AppliedProfile1
from travelport.models.booking_traveler_1 import BookingTraveler1
from travelport.models.commission_remark_1 import CommissionRemark1
from travelport.models.consolidator_remark_1 import ConsolidatorRemark1
from travelport.models.cruise_reservation import CruiseReservation
from travelport.models.customer_id_1 import CustomerId1
from travelport.models.emdsummary_info import EmdsummaryInfo
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.general_remark_1 import GeneralRemark1
from travelport.models.group_1 import Group1
from travelport.models.hotel_reservation import HotelReservation
from travelport.models.invoice_data_1 import InvoiceData1
from travelport.models.invoice_remark_1 import InvoiceRemark1
from travelport.models.linked_universal_record_1 import LinkedUniversalRecord1
from travelport.models.osi_1 import Osi1
from travelport.models.passive_reservation import PassiveReservation
from travelport.models.postscript_1 import Postscript1
from travelport.models.provider_arnksegment_1 import ProviderArnksegment1
from travelport.models.provider_reservation_info import ProviderReservationInfo
from travelport.models.rail_reservation import RailReservation
from travelport.models.review_booking_1 import ReviewBooking1
from travelport.models.segment_continuity_info import SegmentContinuityInfo
from travelport.models.service_fee_info_1 import ServiceFeeInfo1
from travelport.models.ssr_1 import Ssr1
from travelport.models.unassociated_remark_1 import UnassociatedRemark1
from travelport.models.vehicle_reservation import VehicleReservation
from travelport.models.xmlremark_1 import Xmlremark1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class UniversalRecord:
    """
    Universal Record holds one or more provider reservations.

    Parameters
    ----------
    linked_universal_record
    group
    booking_traveler
    service_fee_info
        Travel Agency Service Fees (TASF) are charged by the agency through
        BSP or Airline Reporting Corporation (ARC). FOP will appear directly
        inside UniversalRecord
    osi
    action_status
    provider_reservation_info
    air_reservation
    hotel_reservation
    vehicle_reservation
    passive_reservation
    rail_reservation
    cruise_reservation
        The parent container for all cruise booking data. Supported
        Providers :1V
    emdsummary_info
        List of EMDs to be shown as part of UR. Supported providers are
        1V/1G/1P
    provider_arnksegment
    segment_continuity_info
    xmlremark
    general_remark
    accounting_remark
    unassociated_remark
    postscript
    agency_info
    applied_profile
    agency_contact_info
    customer_id
    commission_remark
    consolidator_remark
    invoice_remark
    review_booking
        Review Booking or Queue Minders is to add the reminders in the
        Provider Reservation along with the date time and Queue details. On
        the date time defined in reminders, the message along with the PNR
        goes to the desired Queue.
    ssr
        SSR's having no bookingTravelerRef need to add at
        providerReservation level outside bookingTraveler
    invoice_data
    form_of_payment
        Provider: 1G,1V,1P,ACH,SDK.Product:Air,Hotel,Vehicle,Cruise
    locator_code
        Unique Identifier of a Universal Record. If this is ViewOnly UR then
        Locator Code is '999999'.
    saved_trip_locator_code
    lock_reason
        The reason for which the reservation is currently locked for
        modifications
    create_date
        The date and time that this reservation was created.
    version
    status
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    linked_universal_record: list[LinkedUniversalRecord1] = field(
        default_factory=list,
        metadata={
            "name": "LinkedUniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    group: None | Group1 = field(
        default=None,
        metadata={
            "name": "Group",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    booking_traveler: list[BookingTraveler1] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    service_fee_info: list[ServiceFeeInfo1] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeeInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    osi: list[Osi1] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    action_status: list[ActionStatus1] = field(
        default_factory=list,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    provider_reservation_info: list[ProviderReservationInfo] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    air_reservation: list[AirReservation] = field(
        default_factory=list,
        metadata={
            "name": "AirReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    hotel_reservation: list[HotelReservation] = field(
        default_factory=list,
        metadata={
            "name": "HotelReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/hotel_v52_0",
            "max_occurs": 999,
        },
    )
    vehicle_reservation: list[VehicleReservation] = field(
        default_factory=list,
        metadata={
            "name": "VehicleReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/vehicle_v52_0",
            "max_occurs": 999,
        },
    )
    passive_reservation: list[PassiveReservation] = field(
        default_factory=list,
        metadata={
            "name": "PassiveReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/passive_v52_0",
            "max_occurs": 999,
        },
    )
    rail_reservation: list[RailReservation] = field(
        default_factory=list,
        metadata={
            "name": "RailReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/rail_v52_0",
            "max_occurs": 999,
        },
    )
    cruise_reservation: list[CruiseReservation] = field(
        default_factory=list,
        metadata={
            "name": "CruiseReservation",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/cruise_v52_0",
            "max_occurs": 999,
        },
    )
    emdsummary_info: list[EmdsummaryInfo] = field(
        default_factory=list,
        metadata={
            "name": "EMDSummaryInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    provider_arnksegment: list[ProviderArnksegment1] = field(
        default_factory=list,
        metadata={
            "name": "ProviderARNKSegment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    segment_continuity_info: None | SegmentContinuityInfo = field(
        default=None,
        metadata={
            "name": "SegmentContinuityInfo",
            "type": "Element",
        },
    )
    xmlremark: list[Xmlremark1] = field(
        default_factory=list,
        metadata={
            "name": "XMLRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    general_remark: list[GeneralRemark1] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    accounting_remark: list[AccountingRemark1] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    unassociated_remark: list[UnassociatedRemark1] = field(
        default_factory=list,
        metadata={
            "name": "UnassociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    postscript: list[Postscript1] = field(
        default_factory=list,
        metadata={
            "name": "Postscript",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    agency_info: None | AgencyInfo1 = field(
        default=None,
        metadata={
            "name": "AgencyInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    applied_profile: None | AppliedProfile1 = field(
        default=None,
        metadata={
            "name": "AppliedProfile",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    agency_contact_info: None | AgencyContactInfo1 = field(
        default=None,
        metadata={
            "name": "AgencyContactInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    customer_id: list[CustomerId1] = field(
        default_factory=list,
        metadata={
            "name": "CustomerID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    commission_remark: list[CommissionRemark1] = field(
        default_factory=list,
        metadata={
            "name": "CommissionRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    consolidator_remark: list[ConsolidatorRemark1] = field(
        default_factory=list,
        metadata={
            "name": "ConsolidatorRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    invoice_remark: list[InvoiceRemark1] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    review_booking: list[ReviewBooking1] = field(
        default_factory=list,
        metadata={
            "name": "ReviewBooking",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    ssr: list[Ssr1] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    invoice_data: list[InvoiceData1] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceData",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    saved_trip_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "SavedTripLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    lock_reason: None | str = field(
        default=None,
        metadata={
            "name": "LockReason",
            "type": "Attribute",
        },
    )
    create_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "CreateDate",
            "type": "Attribute",
        },
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "required": True,
        },
    )
