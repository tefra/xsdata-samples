from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.agency_payment_3 import AgencyPayment3
from travelport.models.agent_voucher_3 import AgentVoucher3
from travelport.models.certificate_3 import Certificate3
from travelport.models.check_3 import Check3
from travelport.models.credit_card_3 import CreditCard3
from travelport.models.debit_card_2 import DebitCard2
from travelport.models.direct_payment_3 import DirectPayment3
from travelport.models.enett_van_2 import EnettVan2
from travelport.models.misc_form_of_payment_3 import MiscFormOfPayment3
from travelport.models.payment_advice_3 import PaymentAdvice3
from travelport.models.requisition_3 import Requisition3
from travelport.models.ticket_number_3 import TicketNumber3
from travelport.models.type_element_status_3 import TypeElementStatus3
from travelport.models.type_form_of_payment_pnrreference_2 import (
    TypeFormOfPaymentPnrreference2,
)
from travelport.models.type_fulfillment_idtype_2 import TypeFulfillmentIdtype2
from travelport.models.type_general_reference_2 import TypeGeneralReference2
from travelport.models.united_nations_3 import UnitedNations3

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class FormOfPayment3:
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
        namespace = "http://www.travelport.com/schema/common_v32_0"

    credit_card: None | CreditCard3 = field(
        default=None,
        metadata={
            "name": "CreditCard",
            "type": "Element",
        },
    )
    debit_card: None | DebitCard2 = field(
        default=None,
        metadata={
            "name": "DebitCard",
            "type": "Element",
        },
    )
    enett_van: None | EnettVan2 = field(
        default=None,
        metadata={
            "name": "EnettVan",
            "type": "Element",
        },
    )
    certificate: None | Certificate3 = field(
        default=None,
        metadata={
            "name": "Certificate",
            "type": "Element",
        },
    )
    ticket_number: None | TicketNumber3 = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
        },
    )
    check: None | Check3 = field(
        default=None,
        metadata={
            "name": "Check",
            "type": "Element",
        },
    )
    requisition: None | Requisition3 = field(
        default=None,
        metadata={
            "name": "Requisition",
            "type": "Element",
        },
    )
    misc_form_of_payment: None | MiscFormOfPayment3 = field(
        default=None,
        metadata={
            "name": "MiscFormOfPayment",
            "type": "Element",
        },
    )
    agency_payment: None | AgencyPayment3 = field(
        default=None,
        metadata={
            "name": "AgencyPayment",
            "type": "Element",
        },
    )
    united_nations: None | UnitedNations3 = field(
        default=None,
        metadata={
            "name": "UnitedNations",
            "type": "Element",
        },
    )
    direct_payment: None | DirectPayment3 = field(
        default=None,
        metadata={
            "name": "DirectPayment",
            "type": "Element",
        },
    )
    agent_voucher: None | AgentVoucher3 = field(
        default=None,
        metadata={
            "name": "AgentVoucher",
            "type": "Element",
        },
    )
    payment_advice: None | PaymentAdvice3 = field(
        default=None,
        metadata={
            "name": "PaymentAdvice",
            "type": "Element",
        },
    )
    provider_reservation_info_ref: list[
        TypeFormOfPaymentPnrreference2
    ] = field(
        default_factory=list,
        metadata={
            "name": "ProviderReservationInfoRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    segment_ref: list[TypeGeneralReference2] = field(
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
    fulfillment_idtype: None | TypeFulfillmentIdtype2 = field(
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
    el_stat: None | TypeElementStatus3 = field(
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
