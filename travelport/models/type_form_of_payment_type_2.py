from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.agency_payment_5 import AgencyPayment5
from travelport.models.agent_voucher_5 import AgentVoucher5
from travelport.models.certificate_5 import Certificate5
from travelport.models.check_5 import Check5
from travelport.models.credit_card_6 import CreditCard6
from travelport.models.direct_payment_5 import DirectPayment5
from travelport.models.misc_form_of_payment_5 import MiscFormOfPayment5
from travelport.models.payment_advice_5 import PaymentAdvice5
from travelport.models.requisition_5 import Requisition5
from travelport.models.type_guarantee_information_5 import (
    TypeGuaranteeInformation5,
)
from travelport.models.type_key_tagged_element_2 import TypeKeyTaggedElement2
from travelport.models.type_payment_card_5 import TypePaymentCard5
from travelport.models.type_voucher_information_5 import (
    TypeVoucherInformation5,
)
from travelport.models.united_nations_5 import UnitedNations5

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeFormOfPaymentType2(TypeKeyTaggedElement2):
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

    credit_card: None | CreditCard6 = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    debit_card: None | TypePaymentCard5 = field(
        default=None,
        metadata={
            "name": "DebitCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    certificate: None | Certificate5 = field(
        default=None,
        metadata={
            "name": "Certificate",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
            "min_length": 1,
            "max_length": 13,
        },
    )
    check: None | Check5 = field(
        default=None,
        metadata={
            "name": "Check",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    requisition: None | Requisition5 = field(
        default=None,
        metadata={
            "name": "Requisition",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    misc_form_of_payment: None | MiscFormOfPayment5 = field(
        default=None,
        metadata={
            "name": "MiscFormOfPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    agency_payment: None | AgencyPayment5 = field(
        default=None,
        metadata={
            "name": "AgencyPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    united_nations: None | UnitedNations5 = field(
        default=None,
        metadata={
            "name": "UnitedNations",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    direct_payment: None | DirectPayment5 = field(
        default=None,
        metadata={
            "name": "DirectPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    agent_voucher: None | AgentVoucher5 = field(
        default=None,
        metadata={
            "name": "AgentVoucher",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    payment_advice: None | PaymentAdvice5 = field(
        default=None,
        metadata={
            "name": "PaymentAdvice",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        },
    )
    guarantee: None | TypeGuaranteeInformation5 = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    voucher: None | TypeVoucherInformation5 = field(
        default=None,
        metadata={
            "name": "Voucher",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        },
    )
    cash: None | str = field(
        default=None,
        metadata={
            "name": "Cash",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
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
