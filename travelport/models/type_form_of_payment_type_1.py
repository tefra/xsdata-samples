from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.agency_payment_2 import AgencyPayment2
from travelport.models.agent_voucher_2 import AgentVoucher2
from travelport.models.certificate_2 import Certificate2
from travelport.models.check_2 import Check2
from travelport.models.credit_card_2 import CreditCard2
from travelport.models.direct_payment_2 import DirectPayment2
from travelport.models.misc_form_of_payment_2 import MiscFormOfPayment2
from travelport.models.payment_advice_2 import PaymentAdvice2
from travelport.models.requisition_2 import Requisition2
from travelport.models.ticket_number_2 import TicketNumber2
from travelport.models.type_guarantee_information_2 import (
    TypeGuaranteeInformation2,
)
from travelport.models.type_key_tagged_element_1 import TypeKeyTaggedElement1
from travelport.models.type_payment_card_2 import TypePaymentCard2
from travelport.models.type_voucher_information_2 import (
    TypeVoucherInformation2,
)
from travelport.models.united_nations_2 import UnitedNations2

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass(kw_only=True)
class TypeFormOfPaymentType1(TypeKeyTaggedElement1):
    """
    Parameters
    ----------
    credit_card
    debit_card
    certificate
    ticket_number
    check
    requisition
    misc_form_of_payment
    agency_payment
    united_nations
    direct_payment
    agent_voucher
    payment_advice
    guarantee
    voucher
    cash
    type_value
        The code from the PAYMENT_FORMAT_TYPE_CD (CRECRD, DEBDRC, REQSTN…).
    description
        Description of the Payment
    priority_order
        Priority order associated with this PaymentDetails.
    owner_id
        Id of the profile who owns the Traveler's proprietary data.Should be
        the immediate parent id of the traveler.
    """

    class Meta:
        name = "typeFormOfPaymentType"

    credit_card: None | CreditCard2 = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    debit_card: None | TypePaymentCard2 = field(
        default=None,
        metadata={
            "name": "DebitCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    certificate: None | Certificate2 = field(
        default=None,
        metadata={
            "name": "Certificate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    ticket_number: None | TicketNumber2 = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    check: None | Check2 = field(
        default=None,
        metadata={
            "name": "Check",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    requisition: None | Requisition2 = field(
        default=None,
        metadata={
            "name": "Requisition",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    misc_form_of_payment: None | MiscFormOfPayment2 = field(
        default=None,
        metadata={
            "name": "MiscFormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    agency_payment: None | AgencyPayment2 = field(
        default=None,
        metadata={
            "name": "AgencyPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    united_nations: None | UnitedNations2 = field(
        default=None,
        metadata={
            "name": "UnitedNations",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    direct_payment: None | DirectPayment2 = field(
        default=None,
        metadata={
            "name": "DirectPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    agent_voucher: None | AgentVoucher2 = field(
        default=None,
        metadata={
            "name": "AgentVoucher",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    payment_advice: None | PaymentAdvice2 = field(
        default=None,
        metadata={
            "name": "PaymentAdvice",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofileCommon_v30_0",
        },
    )
    guarantee: None | TypeGuaranteeInformation2 = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    voucher: None | TypeVoucherInformation2 = field(
        default=None,
        metadata={
            "name": "Voucher",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    cash: None | str = field(
        default=None,
        metadata={
            "name": "Cash",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    type_value: None | object = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        },
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        },
    )
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        },
    )
