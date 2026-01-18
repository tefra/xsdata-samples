from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.accounting_remark_1 import AccountingRemark1
from travelport.models.action_status_1 import ActionStatus1
from travelport.models.agency_contact_info_1 import AgencyContactInfo1
from travelport.models.booking_traveler_info_1 import BookingTravelerInfo1
from travelport.models.commission_remark_1 import CommissionRemark1
from travelport.models.consolidator_remark_1 import ConsolidatorRemark1
from travelport.models.customer_id_1 import CustomerId1
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.general_remark_1 import GeneralRemark1
from travelport.models.invoice_remark_1 import InvoiceRemark1
from travelport.models.linked_universal_record_1 import LinkedUniversalRecord1
from travelport.models.osi_1 import Osi1
from travelport.models.postscript_1 import Postscript1
from travelport.models.review_booking_1 import ReviewBooking1
from travelport.models.service_fee_info_1 import ServiceFeeInfo1
from travelport.models.unassociated_remark_1 import UnassociatedRemark1
from travelport.models.xmlremark_1 import Xmlremark1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class UniversalAdd:
    """
    Parameters
    ----------
    accounting_remark
    general_remark
    osi
    unassociated_remark
    xmlremark
    postscript
    booking_traveler_info
    service_fee_info
    linked_universal_record
    agency_contact_info
    customer_id
    commission_remark
    consolidator_remark
    invoice_remark
    action_status
    review_booking
        Element to add Review booking to a PNR .
    form_of_payment
        Provider:1G,1V,1P,ACH,SDK.Product:Air,Hotel,Vehicle,Cruise
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    accounting_remark: list[AccountingRemark1] = field(
        default_factory=list,
        metadata={
            "name": "AccountingRemark",
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
    osi: list[Osi1] = field(
        default_factory=list,
        metadata={
            "name": "OSI",
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
    xmlremark: list[Xmlremark1] = field(
        default_factory=list,
        metadata={
            "name": "XMLRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    postscript: None | Postscript1 = field(
        default=None,
        metadata={
            "name": "Postscript",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    booking_traveler_info: None | BookingTravelerInfo1 = field(
        default=None,
        metadata={
            "name": "BookingTravelerInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    linked_universal_record: list[LinkedUniversalRecord1] = field(
        default_factory=list,
        metadata={
            "name": "LinkedUniversalRecord",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
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
    customer_id: None | CustomerId1 = field(
        default=None,
        metadata={
            "name": "CustomerID",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    commission_remark: None | CommissionRemark1 = field(
        default=None,
        metadata={
            "name": "CommissionRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    consolidator_remark: None | ConsolidatorRemark1 = field(
        default=None,
        metadata={
            "name": "ConsolidatorRemark",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    action_status: None | ActionStatus1 = field(
        default=None,
        metadata={
            "name": "ActionStatus",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    form_of_payment: list[FormOfPayment1] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
