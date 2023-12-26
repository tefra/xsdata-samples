from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.agency_payment_7 import AgencyPayment7
from travelport.models.agent_voucher_7 import AgentVoucher7
from travelport.models.certificate_7 import Certificate7
from travelport.models.check_7 import Check7
from travelport.models.credit_card_8 import CreditCard8
from travelport.models.debit_card_6 import DebitCard6
from travelport.models.direct_payment_7 import DirectPayment7
from travelport.models.enett_van_6 import EnettVan6
from travelport.models.misc_form_of_payment_7 import MiscFormOfPayment7
from travelport.models.payment_advice_7 import PaymentAdvice7
from travelport.models.requisition_7 import Requisition7
from travelport.models.type_element_status_7 import TypeElementStatus7
from travelport.models.type_form_of_payment_pnrreference_6 import (
    TypeFormOfPaymentPnrreference6,
)
from travelport.models.type_fulfillment_idtype_6 import TypeFulfillmentIdtype6
from travelport.models.type_general_reference_6 import TypeGeneralReference6
from travelport.models.united_nations_7 import UnitedNations7

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class FormOfPayment8:
    """
    A Form of Payment used to purchase all or part of a booking.

    Parameters
    ----------
    credit_card
    debit_card
    enett_van
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
    provider_reservation_info_ref
    segment_ref
    key
    type_value
    fulfillment_type
        Defines how the client wishes to receive travel documents. Type does
        not define where or how payment is made. The supported values are
        "Ticket on Departure", "Travel Agency", "Courier", "Standard Mail",
        "Ticketless", "Ticket Office", "Express Mail", "Corporate Kiosk",
        "Train Station Service Desk", "Direct Printing of Ticket", "Ticket
        by Email", "Digital Printing of Ticket at Home", "Retrieve Ticket at
        Eurostar in London" Collect booking ticket at a Kiosk, print in
        agency.
    fulfillment_location
        Information about the location of the printer.
    fulfillment_idtype
        Identification type, e.g. credit card, to define how the customer
        will identify himself when collecting the ticket
    fulfillment_idnumber
        Identification number, e.g. card number, to define how the customer
        will identify himself when collecting the ticket
    is_agent_type
        If this is true then FormOfPayment mention in Type is anAgent type
        FormOfPayment.
    agent_text
        This is only relevent when IsAgentType is specified as true.
        Otherwise this will be ignored.
    reuse_fop
        Key of the FOP Key to be reused as this Form of Payment.Only Credit
        and Debit Card will be supported for FOP Reuse.
    external_reference
    reusable
        Indicates whether the form of payment can be reused or not.
        Currently applicable for Credit and Debit form of payment
    profile_id
        The unique ID of the profile that contains the payment details to
        use.
    profile_key
        The Key assigned to the payment details value from the specified
        profile.
    el_stat
        This attribute is used to show the action results of an element.
        Possible values are "A" (when elements have been added to the UR)
        and "M" (when existing elements have been modified). Response only.
    key_override
        If a duplicate key is found where we are adding elements in some
        cases like URAdd, then instead of erroring out set this attribute to
        true.
    """

    class Meta:
        name = "FormOfPayment"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    credit_card: None | CreditCard8 = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
        },
    )
    debit_card: None | DebitCard6 = field(
        default=None,
        metadata={
            "name": "DebitCard",
            "type": "Element",
        },
    )
    enett_van: None | EnettVan6 = field(
        default=None,
        metadata={
            "name": "EnettVan",
            "type": "Element",
        },
    )
    certificate: None | Certificate7 = field(
        default=None,
        metadata={
            "name": "Certificate",
            "type": "Element",
        },
    )
    ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "min_length": 1,
            "max_length": 13,
        },
    )
    check: None | Check7 = field(
        default=None,
        metadata={
            "name": "Check",
            "type": "Element",
        },
    )
    requisition: None | Requisition7 = field(
        default=None,
        metadata={
            "name": "Requisition",
            "type": "Element",
        },
    )
    misc_form_of_payment: None | MiscFormOfPayment7 = field(
        default=None,
        metadata={
            "name": "MiscFormOfPayment",
            "type": "Element",
        },
    )
    agency_payment: None | AgencyPayment7 = field(
        default=None,
        metadata={
            "name": "AgencyPayment",
            "type": "Element",
        },
    )
    united_nations: None | UnitedNations7 = field(
        default=None,
        metadata={
            "name": "UnitedNations",
            "type": "Element",
        },
    )
    direct_payment: None | DirectPayment7 = field(
        default=None,
        metadata={
            "name": "DirectPayment",
            "type": "Element",
        },
    )
    agent_voucher: None | AgentVoucher7 = field(
        default=None,
        metadata={
            "name": "AgentVoucher",
            "type": "Element",
        },
    )
    payment_advice: None | PaymentAdvice7 = field(
        default=None,
        metadata={
            "name": "PaymentAdvice",
            "type": "Element",
        },
    )
    provider_reservation_info_ref: list[
        TypeFormOfPaymentPnrreference6
    ] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    segment_ref: list[TypeGeneralReference6] = field(
        default_factory=list,
        metadata={
            "name": "SegmentRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
            "max_length": 25,
        },
    )
    fulfillment_type: None | str = field(
        default=None,
        metadata={
            "name": "FulfillmentType",
            "type": "Attribute",
        },
    )
    fulfillment_location: None | str = field(
        default=None,
        metadata={
            "name": "FulfillmentLocation",
            "type": "Attribute",
        },
    )
    fulfillment_idtype: None | TypeFulfillmentIdtype6 = field(
        default=None,
        metadata={
            "name": "FulfillmentIDType",
            "type": "Attribute",
        },
    )
    fulfillment_idnumber: None | str = field(
        default=None,
        metadata={
            "name": "FulfillmentIDNumber",
            "type": "Attribute",
        },
    )
    is_agent_type: bool = field(
        default=False,
        metadata={
            "name": "IsAgentType",
            "type": "Attribute",
        },
    )
    agent_text: None | str = field(
        default=None,
        metadata={
            "name": "AgentText",
            "type": "Attribute",
        },
    )
    reuse_fop: None | str = field(
        default=None,
        metadata={
            "name": "ReuseFOP",
            "type": "Attribute",
        },
    )
    external_reference: None | str = field(
        default=None,
        metadata={
            "name": "ExternalReference",
            "type": "Attribute",
            "max_length": 32,
        },
    )
    reusable: bool = field(
        default=False,
        metadata={
            "name": "Reusable",
            "type": "Attribute",
        },
    )
    profile_id: None | str = field(
        default=None,
        metadata={
            "name": "ProfileID",
            "type": "Attribute",
        },
    )
    profile_key: None | str = field(
        default=None,
        metadata={
            "name": "ProfileKey",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus7 = field(
        default=None,
        metadata={
            "name": "ElStat",
            "type": "Attribute",
        },
    )
    key_override: None | bool = field(
        default=None,
        metadata={
            "name": "KeyOverride",
            "type": "Attribute",
        },
    )
