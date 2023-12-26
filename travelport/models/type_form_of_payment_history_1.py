from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.agency_payment_history_1 import AgencyPaymentHistory1
from travelport.models.agent_voucher_history_1 import AgentVoucherHistory1
from travelport.models.certificate_history_1 import CertificateHistory1
from travelport.models.check_2 import Check2
from travelport.models.direct_payment_2 import DirectPayment2
from travelport.models.misc_form_of_payment_history_1 import (
    MiscFormOfPaymentHistory1,
)
from travelport.models.requisition_2 import Requisition2
from travelport.models.type_credit_card_type_history_1 import (
    TypeCreditCardTypeHistory1,
)
from travelport.models.type_guarantee_information_history_1 import (
    TypeGuaranteeInformationHistory1,
)
from travelport.models.type_key_element_1 import TypeKeyElement1
from travelport.models.type_payment_card_history_1 import (
    TypePaymentCardHistory1,
)
from travelport.models.type_voucher_information_history_1 import (
    TypeVoucherInformationHistory1,
)
from travelport.models.united_nations_history_1 import UnitedNationsHistory1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TypeFormOfPaymentHistory1(TypeKeyElement1):
    """
    Parameters
    ----------
    credit_card
    debit_card
    certificate_history
    ticket_number_history
    check
    requisition
    misc_form_of_payment_history
    agency_payment_history
    united_nations_history
    direct_payment
    agent_voucher_history
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
        name = "typeFormOfPaymentHistory"

    credit_card: None | TypeCreditCardTypeHistory1 = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    debit_card: None | TypePaymentCardHistory1 = field(
        default=None,
        metadata={
            "name": "DebitCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    certificate_history: None | CertificateHistory1 = field(
        default=None,
        metadata={
            "name": "CertificateHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    ticket_number_history: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumberHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
            "min_length": 0,
            "max_length": 13,
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
    misc_form_of_payment_history: None | MiscFormOfPaymentHistory1 = field(
        default=None,
        metadata={
            "name": "MiscFormOfPaymentHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    agency_payment_history: None | AgencyPaymentHistory1 = field(
        default=None,
        metadata={
            "name": "AgencyPaymentHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    united_nations_history: None | UnitedNationsHistory1 = field(
        default=None,
        metadata={
            "name": "UnitedNationsHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
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
    agent_voucher_history: None | AgentVoucherHistory1 = field(
        default=None,
        metadata={
            "name": "AgentVoucherHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    guarantee: None | TypeGuaranteeInformationHistory1 = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/sharedUprofile_v20_0",
        },
    )
    voucher: None | TypeVoucherInformationHistory1 = field(
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
