from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.agency_payment_history_2 import AgencyPaymentHistory2
from travelport.models.agent_voucher_history_2 import AgentVoucherHistory2
from travelport.models.certificate_history_2 import CertificateHistory2
from travelport.models.check_5 import Check5
from travelport.models.direct_payment_5 import DirectPayment5
from travelport.models.misc_form_of_payment_history_2 import MiscFormOfPaymentHistory2
from travelport.models.requisition_5 import Requisition5
from travelport.models.type_credit_card_type_history_2 import TypeCreditCardTypeHistory2
from travelport.models.type_guarantee_information_history_2 import TypeGuaranteeInformationHistory2
from travelport.models.type_key_element_2 import TypeKeyElement2
from travelport.models.type_payment_card_history_2 import TypePaymentCardHistory2
from travelport.models.type_voucher_information_history_2 import TypeVoucherInformationHistory2
from travelport.models.united_nations_history_2 import UnitedNationsHistory2

__NAMESPACE__ = "http://www.travelport.com/schema/uprofile_v37_0"


@dataclass
class TypeFormOfPaymentHistory2(TypeKeyElement2):
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

    credit_card: None | TypeCreditCardTypeHistory2 = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    debit_card: None | TypePaymentCardHistory2 = field(
        default=None,
        metadata={
            "name": "DebitCard",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    certificate_history: None | CertificateHistory2 = field(
        default=None,
        metadata={
            "name": "CertificateHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    ticket_number_history: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumberHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
            "min_length": 0,
            "max_length": 13,
        }
    )
    check: None | Check5 = field(
        default=None,
        metadata={
            "name": "Check",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    requisition: None | Requisition5 = field(
        default=None,
        metadata={
            "name": "Requisition",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    misc_form_of_payment_history: None | MiscFormOfPaymentHistory2 = field(
        default=None,
        metadata={
            "name": "MiscFormOfPaymentHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    agency_payment_history: None | AgencyPaymentHistory2 = field(
        default=None,
        metadata={
            "name": "AgencyPaymentHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    united_nations_history: None | UnitedNationsHistory2 = field(
        default=None,
        metadata={
            "name": "UnitedNationsHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    direct_payment: None | DirectPayment5 = field(
        default=None,
        metadata={
            "name": "DirectPayment",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v37_0",
        }
    )
    agent_voucher_history: None | AgentVoucherHistory2 = field(
        default=None,
        metadata={
            "name": "AgentVoucherHistory",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    guarantee: None | TypeGuaranteeInformationHistory2 = field(
        default=None,
        metadata={
            "name": "Guarantee",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    voucher: None | TypeVoucherInformationHistory2 = field(
        default=None,
        metadata={
            "name": "Voucher",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    cash: None | str = field(
        default=None,
        metadata={
            "name": "Cash",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/uprofile_v37_0",
        }
    )
    type_value: None | object = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
        }
    )
    description: None | str = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 255,
        }
    )
    priority_order: None | int = field(
        default=None,
        metadata={
            "name": "PriorityOrder",
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )
    owner_id: None | int = field(
        default=None,
        metadata={
            "name": "OwnerID",
            "type": "Attribute",
        }
    )
