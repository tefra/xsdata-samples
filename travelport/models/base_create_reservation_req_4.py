from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.accounting_remark_4 import AccountingRemark4
from travelport.models.agency_contact_info_4 import AgencyContactInfo4
from travelport.models.base_req_5 import BaseReq5
from travelport.models.booking_traveler_4 import BookingTraveler4
from travelport.models.commission_remark_4 import CommissionRemark4
from travelport.models.consolidator_remark_4 import ConsolidatorRemark4
from travelport.models.continuity_check_override_4 import (
    ContinuityCheckOverride4,
)
from travelport.models.customer_id_4 import CustomerId4
from travelport.models.email_notification_4 import EmailNotification4
from travelport.models.file_finishing_info_4 import FileFinishingInfo4
from travelport.models.general_remark_4 import GeneralRemark4
from travelport.models.invoice_remark_4 import InvoiceRemark4
from travelport.models.linked_universal_record_4 import LinkedUniversalRecord4
from travelport.models.osi_4 import Osi4
from travelport.models.passive_info_4 import PassiveInfo4
from travelport.models.postscript_4 import Postscript4
from travelport.models.queue_place_4 import QueuePlace4
from travelport.models.ssr_4 import Ssr4
from travelport.models.unassociated_remark_4 import UnassociatedRemark4
from travelport.models.xmlremark_4 import Xmlremark4

__NAMESPACE__ = "http://www.travelport.com/schema/common_v37_0"


@dataclass(kw_only=True)
class BaseCreateReservationReq4(BaseReq5):
    """
    Parameters
    ----------
    linked_universal_record
    booking_traveler
    osi
    accounting_remark
    general_remark
    xmlremark
    unassociated_remark
    postscript
    passive_info
    continuity_check_override
        This element will be used if user wants to override segment
        continuity check.
    agency_contact_info
    customer_id
    file_finishing_info
    commission_remark
    consolidator_remark
    invoice_remark
    ssr
        SSR element outside Booking Traveler without any Segment Ref or
        Booking Traveler Ref.
    email_notification
    queue_place
        Allow queue placement of a PNR at the time of booking in
        AirCreateReservationReq,HotelCreateReservationReq,PassiveCreateReservationReq
        and VehicleCreateReservationReq for providers 1G,1V,1P and 1J.
    rule_name
        This attribute is meant to attach a mandatory custom check rule name
        to a PNR. A non-mandatory custom check rule too can be attached to a
        PNR.
    universal_record_locator_code
        Which UniversalRecord should this new reservation be applied to.  If
        blank, then a new one is created.
    provider_locator_code
        Which Provider reservation does this reservation get added to.
    provider_code
        To be used with ProviderLocatorCode, which host the reservation
        being added to belongs to.
    customer_number
        Optional client centric customer identifier
    version
    """

    class Meta:
        name = "BaseCreateReservationReq"

    linked_universal_record: list[LinkedUniversalRecord4] = field(
        default_factory=list,
        metadata={
            "name": "LinkedUniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    booking_traveler: list[BookingTraveler4] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    osi: list[Osi4] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    accounting_remark: list[AccountingRemark4] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    general_remark: list[GeneralRemark4] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    xmlremark: list[Xmlremark4] = field(
        default_factory=list,
        metadata={
            "name": "XMLRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    unassociated_remark: list[UnassociatedRemark4] = field(
        default_factory=list,
        metadata={
            "name": "UnassociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    postscript: None | Postscript4 = field(
        default=None,
        metadata={
            "name": "Postscript",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    passive_info: None | PassiveInfo4 = field(
        default=None,
        metadata={
            "name": "PassiveInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    continuity_check_override: None | ContinuityCheckOverride4 = field(
        default=None,
        metadata={
            "name": "ContinuityCheckOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    agency_contact_info: None | AgencyContactInfo4 = field(
        default=None,
        metadata={
            "name": "AgencyContactInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    customer_id: None | CustomerId4 = field(
        default=None,
        metadata={
            "name": "CustomerID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    file_finishing_info: None | FileFinishingInfo4 = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    commission_remark: None | CommissionRemark4 = field(
        default=None,
        metadata={
            "name": "CommissionRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    consolidator_remark: None | ConsolidatorRemark4 = field(
        default=None,
        metadata={
            "name": "ConsolidatorRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    invoice_remark: list[InvoiceRemark4] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    ssr: list[Ssr4] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "max_occurs": 999,
        },
    )
    email_notification: None | EmailNotification4 = field(
        default=None,
        metadata={
            "name": "EmailNotification",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    queue_place: None | QueuePlace4 = field(
        default=None,
        metadata={
            "name": "QueuePlace",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    rule_name: None | str = field(
        default=None,
        metadata={
            "name": "RuleName",
            "type": "Attribute",
            "max_length": 10,
        },
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
        },
    )
    customer_number: None | str = field(
        default=None,
        metadata={
            "name": "CustomerNumber",
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
