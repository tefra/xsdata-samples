from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.accounting_remark_3 import AccountingRemark3
from travelport.models.agency_contact_info_3 import AgencyContactInfo3
from travelport.models.base_req_4 import BaseReq4
from travelport.models.booking_traveler_3 import BookingTraveler3
from travelport.models.commission_remark_3 import CommissionRemark3
from travelport.models.consolidator_remark_3 import ConsolidatorRemark3
from travelport.models.continuity_check_override_3 import ContinuityCheckOverride3
from travelport.models.customer_id_3 import CustomerId3
from travelport.models.email_notification_3 import EmailNotification3
from travelport.models.file_finishing_info_3 import FileFinishingInfo3
from travelport.models.general_remark_3 import GeneralRemark3
from travelport.models.invoice_remark_3 import InvoiceRemark3
from travelport.models.linked_universal_record_3 import LinkedUniversalRecord3
from travelport.models.osi_3 import Osi3
from travelport.models.passive_info_3 import PassiveInfo3
from travelport.models.postscript_3 import Postscript3
from travelport.models.queue_place_3 import QueuePlace3
from travelport.models.ssr_3 import Ssr3
from travelport.models.unassociated_remark_3 import UnassociatedRemark3
from travelport.models.xmlremark_3 import Xmlremark3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class BaseCreateReservationReq3(BaseReq4):
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

    linked_universal_record: list[LinkedUniversalRecord3] = field(
        default_factory=list,
        metadata={
            "name": "LinkedUniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        }
    )
    booking_traveler: list[BookingTraveler3] = field(
        default_factory=list,
        metadata={
            "name": "BookingTraveler",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        }
    )
    osi: list[Osi3] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        }
    )
    accounting_remark: list[AccountingRemark3] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        }
    )
    general_remark: list[GeneralRemark3] = field(
        default_factory=list,
        metadata={
            "name": "GeneralRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        }
    )
    xmlremark: list[Xmlremark3] = field(
        default_factory=list,
        metadata={
            "name": "XMLRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        }
    )
    unassociated_remark: list[UnassociatedRemark3] = field(
        default_factory=list,
        metadata={
            "name": "UnassociatedRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        }
    )
    postscript: None | Postscript3 = field(
        default=None,
        metadata={
            "name": "Postscript",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        }
    )
    passive_info: None | PassiveInfo3 = field(
        default=None,
        metadata={
            "name": "PassiveInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        }
    )
    continuity_check_override: None | ContinuityCheckOverride3 = field(
        default=None,
        metadata={
            "name": "ContinuityCheckOverride",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        }
    )
    agency_contact_info: None | AgencyContactInfo3 = field(
        default=None,
        metadata={
            "name": "AgencyContactInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        }
    )
    customer_id: None | CustomerId3 = field(
        default=None,
        metadata={
            "name": "CustomerID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        }
    )
    file_finishing_info: None | FileFinishingInfo3 = field(
        default=None,
        metadata={
            "name": "FileFinishingInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        }
    )
    commission_remark: None | CommissionRemark3 = field(
        default=None,
        metadata={
            "name": "CommissionRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        }
    )
    consolidator_remark: None | ConsolidatorRemark3 = field(
        default=None,
        metadata={
            "name": "ConsolidatorRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        }
    )
    invoice_remark: list[InvoiceRemark3] = field(
        default_factory=list,
        metadata={
            "name": "InvoiceRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        }
    )
    ssr: list[Ssr3] = field(
        default_factory=list,
        metadata={
            "name": "SSR",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
            "max_occurs": 999,
        }
    )
    email_notification: None | EmailNotification3 = field(
        default=None,
        metadata={
            "name": "EmailNotification",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        }
    )
    queue_place: None | QueuePlace3 = field(
        default=None,
        metadata={
            "name": "QueuePlace",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v33_0",
        }
    )
    rule_name: None | str = field(
        default=None,
        metadata={
            "name": "RuleName",
            "type": "Attribute",
            "max_length": 10,
        }
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        }
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
        }
    )
    customer_number: None | str = field(
        default=None,
        metadata={
            "name": "CustomerNumber",
            "type": "Attribute",
        }
    )
    version: None | int = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Attribute",
        }
    )
