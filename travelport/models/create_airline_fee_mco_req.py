from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.accounting_remark_1 import AccountingRemark1
from travelport.models.base_req_1 import BaseReq1
from travelport.models.endorsement_1 import Endorsement1
from travelport.models.form_of_payment_1 import FormOfPayment1
from travelport.models.form_of_payment_ref_1 import FormOfPaymentRef1
from travelport.models.general_remark_1 import GeneralRemark1
from travelport.models.name_1 import Name1

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class CreateAirlineFeeMcoReq(BaseReq1):
    """
    Manually create an Airline Fee MCO.

    Parameters
    ----------
    name
    form_of_payment
    form_of_payment_ref
    general_remark
    accounting_remark
    endorsement
    amount
    location_code
        The airport code where the MCO will be accepted, or the City code
        where the requesting agency resides. If not entered, the default
        location of the agency will be selected.
    locator_code
        The locator code of the PNR that the MCO is created for.
    ticket_number
        The ticket that this MCO was issued in connection with. Could be the
        ticket that caused the fee, a residual from an exchange, or an
        airline service fee.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    name: Name1 = field(
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        }
    )
    form_of_payment: None | FormOfPayment1 = field(
        default=None,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    form_of_payment_ref: None | FormOfPaymentRef1 = field(
        default=None,
        metadata={
            "name": "FormOfPaymentRef",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
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
    endorsement: list[Endorsement1] = field(
        default_factory=list,
        metadata={
            "name": "Endorsement",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "max_occurs": 999,
        },
    )
    amount: str = field(
        metadata={
            "name": "Amount",
            "type": "Attribute",
            "required": True,
        }
    )
    location_code: str = field(
        metadata={
            "name": "LocationCode",
            "type": "Attribute",
            "required": True,
            "length": 3,
        }
    )
    locator_code: str = field(
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "required": True,
            "max_length": 8,
        }
    )
    ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
        },
    )
