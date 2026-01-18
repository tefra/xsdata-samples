from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.commission_1 import Commission1
from travelport.models.destination_purpose_code import DestinationPurposeCode
from travelport.models.document_options import DocumentOptions
from travelport.models.document_select import DocumentSelect
from travelport.models.exempt_obfee import ExemptObfee
from travelport.models.land_charges import LandCharges
from travelport.models.language_option import LanguageOption
from travelport.models.print_blank_form_itinerary import (
    PrintBlankFormItinerary,
)
from travelport.models.segment_modifiers import SegmentModifiers
from travelport.models.segment_select import SegmentSelect
from travelport.models.supplier_locator_1 import SupplierLocator1
from travelport.models.ticket_endorsement import TicketEndorsement
from travelport.models.tour_code import TourCode
from travelport.models.type_bulk_ticket_modifier_type import (
    TypeBulkTicketModifierType,
)
from travelport.models.type_element_status_1 import TypeElementStatus1
from travelport.models.type_ticket_modifier_accounting_type import (
    TypeTicketModifierAccountingType,
)
from travelport.models.type_ticket_modifier_amount_type import (
    TypeTicketModifierAmountType,
)
from travelport.models.type_ticket_modifier_value_type import (
    TypeTicketModifierValueType,
)

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class TicketingModifiers:
    """
    A container to identify individual ticketing modifiers.

    Parameters
    ----------
    booking_traveler_ref
        Reference to a booking traveler for which ticketing modifier is
        applied.
    net_remit
        Allows an agency to override the net remittance amount - varies by
        BSP agreement
    net_fare
        Net Fare amount for a ticketed fare
    actual_selling_fare
        Allows an agency to report an Actual Selling Fare as part of the net
        remittance BSP agreement
    invoice_fare
        Allows an agency to report an Invoice Fare as part of the net
        remittance BSP agreement
    corporate_discount
        Allows an agency to add a corporate discount to the itinerary to be
        ticketed
    accounting_info
        Allows an agency to report Accounting Information as part of the net
        remittance BSP agreement
    bulk_ticket
        Allows an agency to update the fare as a Bulk ticket - Optional
        SuppressOnFareCalc attribute will control how fare calculation is
        printed on the ticket
    group_tour
        Allows an agency to update the fare as a Group Tour (inclusive tour)
        ticket - Optional SuppressOnFareCalc attribute will control how fare
        calculation is printed on the ticket
    commission
        Allows an agency to update the commission to a new or different
        commission rate which will be applied at time of ticketing. The
        commission Modifier allows the user specify how the commission
        change is to applied
    tour_code
        Allows an agency to modify the tour code information on the ticket
    ticket_endorsement
        Allows an agency to add user defined ticketing endorsements the
        ticket
    value_modifier
        Allows an agency to modify value or commission of the ticket. The
        modifier is generic and depends on the specific GDS and BSP
        implementation
    document_select
    document_options
    segment_select
    segment_modifiers
    supplier_locator
    destination_purpose_code
    language_option
    land_charges
    print_blank_form_itinerary
    exempt_obfee
    is_primary_di
        Indicates if the DI is Primary DI. 1P only
    document_instruction_number
        The Document Instruction line number. 1P only
    reference
        Identifies if TicketingModifiers contains DI line information. 1P
        only.
    status
        DI line status - ex:Ticketed
    free_text
        DI line information shown as free text as in Host. 1P only
    name_number
        Host Name Number
    ticket_record
        Ticket Record Number
    plating_carrier
        Allows an agency to specify the Plating Carrier for ticketing
    exempt_vat
        Allows an agency to update if VAT is Exemtped on the fare.
    net_remit_applied
        Indicator to the BSP net remittance scheme applies to ticketed fare.
    free_ticket
        Indicates free ticket.
    currency_override_code
        This modifier allows an agency to specify the currency like L for
        Local, E for Euro, U for USD, C for CAD (Canadian dollars).
    key
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
        namespace = "http://www.travelport.com/schema/air_v52_0"

    booking_traveler_ref: list[str] = field(
        default_factory=list,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    net_remit: None | TypeTicketModifierAmountType = field(
        default=None,
        metadata={
            "name": "NetRemit",
            "type": "Element",
        },
    )
    net_fare: None | TypeTicketModifierAmountType = field(
        default=None,
        metadata={
            "name": "NetFare",
            "type": "Element",
        },
    )
    actual_selling_fare: None | TypeTicketModifierAmountType = field(
        default=None,
        metadata={
            "name": "ActualSellingFare",
            "type": "Element",
        },
    )
    invoice_fare: None | TypeTicketModifierAccountingType = field(
        default=None,
        metadata={
            "name": "InvoiceFare",
            "type": "Element",
        },
    )
    corporate_discount: None | TypeTicketModifierAccountingType = field(
        default=None,
        metadata={
            "name": "CorporateDiscount",
            "type": "Element",
        },
    )
    accounting_info: None | TypeTicketModifierAccountingType = field(
        default=None,
        metadata={
            "name": "AccountingInfo",
            "type": "Element",
        },
    )
    bulk_ticket: None | TicketingModifiers.BulkTicket = field(
        default=None,
        metadata={
            "name": "BulkTicket",
            "type": "Element",
        },
    )
    group_tour: None | TypeBulkTicketModifierType = field(
        default=None,
        metadata={
            "name": "GroupTour",
            "type": "Element",
        },
    )
    commission: None | Commission1 = field(
        default=None,
        metadata={
            "name": "Commission",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    tour_code: None | TourCode = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Element",
        },
    )
    ticket_endorsement: list[TicketEndorsement] = field(
        default_factory=list,
        metadata={
            "name": "TicketEndorsement",
            "type": "Element",
            "max_occurs": 3,
        },
    )
    value_modifier: None | TypeTicketModifierValueType = field(
        default=None,
        metadata={
            "name": "ValueModifier",
            "type": "Element",
        },
    )
    document_select: None | DocumentSelect = field(
        default=None,
        metadata={
            "name": "DocumentSelect",
            "type": "Element",
        },
    )
    document_options: None | DocumentOptions = field(
        default=None,
        metadata={
            "name": "DocumentOptions",
            "type": "Element",
        },
    )
    segment_select: None | SegmentSelect = field(
        default=None,
        metadata={
            "name": "SegmentSelect",
            "type": "Element",
        },
    )
    segment_modifiers: list[SegmentModifiers] = field(
        default_factory=list,
        metadata={
            "name": "SegmentModifiers",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    supplier_locator: None | SupplierLocator1 = field(
        default=None,
        metadata={
            "name": "SupplierLocator",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
        },
    )
    destination_purpose_code: None | DestinationPurposeCode = field(
        default=None,
        metadata={
            "name": "DestinationPurposeCode",
            "type": "Element",
        },
    )
    language_option: list[LanguageOption] = field(
        default_factory=list,
        metadata={
            "name": "LanguageOption",
            "type": "Element",
            "max_occurs": 2,
        },
    )
    land_charges: None | LandCharges = field(
        default=None,
        metadata={
            "name": "LandCharges",
            "type": "Element",
        },
    )
    print_blank_form_itinerary: None | PrintBlankFormItinerary = field(
        default=None,
        metadata={
            "name": "PrintBlankFormItinerary",
            "type": "Element",
        },
    )
    exempt_obfee: None | ExemptObfee = field(
        default=None,
        metadata={
            "name": "ExemptOBFee",
            "type": "Element",
        },
    )
    is_primary_di: bool = field(
        default=False,
        metadata={
            "name": "IsPrimaryDI",
            "type": "Attribute",
        },
    )
    document_instruction_number: None | str = field(
        default=None,
        metadata={
            "name": "DocumentInstructionNumber",
            "type": "Attribute",
        },
    )
    reference: None | str = field(
        default=None,
        metadata={
            "name": "Reference",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
            "max_length": 30,
        },
    )
    free_text: None | str = field(
        default=None,
        metadata={
            "name": "FreeText",
            "type": "Attribute",
            "max_length": 756,
        },
    )
    name_number: None | str = field(
        default=None,
        metadata={
            "name": "NameNumber",
            "type": "Attribute",
        },
    )
    ticket_record: None | str = field(
        default=None,
        metadata={
            "name": "TicketRecord",
            "type": "Attribute",
        },
    )
    plating_carrier: None | str = field(
        default=None,
        metadata={
            "name": "PlatingCarrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    exempt_vat: None | bool = field(
        default=None,
        metadata={
            "name": "ExemptVAT",
            "type": "Attribute",
        },
    )
    net_remit_applied: None | bool = field(
        default=None,
        metadata={
            "name": "NetRemitApplied",
            "type": "Attribute",
        },
    )
    free_ticket: None | bool = field(
        default=None,
        metadata={
            "name": "FreeTicket",
            "type": "Attribute",
        },
    )
    currency_override_code: None | str = field(
        default=None,
        metadata={
            "name": "CurrencyOverrideCode",
            "type": "Attribute",
            "length": 1,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    el_stat: None | TypeElementStatus1 = field(
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

    @dataclass(kw_only=True)
    class BulkTicket(TypeBulkTicketModifierType):
        """
        Parameters
        ----------
        non_refundable
            Indicates bulk ticket being non-refundable
        """

        non_refundable: None | bool = field(
            default=None,
            metadata={
                "name": "NonRefundable",
                "type": "Attribute",
            },
        )
