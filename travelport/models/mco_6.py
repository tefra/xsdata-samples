from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate, XmlDateTime
from travelport.models.endorsement_6 import Endorsement6
from travelport.models.form_of_payment_8 import FormOfPayment8
from travelport.models.mcoexchange_info_6 import McoexchangeInfo6
from travelport.models.mcofee_info_6 import McofeeInfo6
from travelport.models.mcoinformation_6 import Mcoinformation6
from travelport.models.mcoprice_data_6 import McopriceData6
from travelport.models.mcoremark_6 import Mcoremark6
from travelport.models.mcotext_6 import Mcotext6
from travelport.models.stock_control_6 import StockControl6

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass
class Mco6(Mcoinformation6):
    """
    Parameters
    ----------
    form_of_payment
    endorsement
    mcoexchange_info
    mcofee_info
    mcoremark
    mcoprice_data
    stock_control
    mcotext
    ticket_type
        Ticket issue indicator. Possible values "Pre-paid ticket advice",
        "Ticket on departure" and "Other" .
    ticket_number
        The ticket that this MCO was issued in connection with. Could be the
        ticket that caused the fee, a residual from an exchange, or an
        airline service fee.
    mcoissued
        Set to true when the MCO is to be issued and set to false if it is
        stored for issue at a later time.
    mcoissue_date
        Date and time in which the MCO was issued.
    mcodoc_num
        MCO document number.
    issue_reason_code
        MCO issuing reason code. Possible Values (List): A - Air
        transportation, B - Surface transportation C - Bag shipped as cargo,
        D - Land arrgs for it, E - Car hire, F - Sleeper / berth G - Up-
        grading, H - Under collections, I - Taxes/fees/charges, J - Deposits
        down payments K - Refundable Balances, L - Hotel accommodations, M -
        Sundry charges, N - Cancellation fee O - Other, P thru Z - airline
        specific, 1 thru 9 - market specific
    plating_carrier
        The Plating Carrier for this MCO
    tour_operator
        Tour Operator - name of honoring carrier or operator.
    location
        Location of honoring carrier or operator.
    tour_code
        The Tour Code of the MCO.
    provider_code
        Contains the Provider Code of the provider that houses this MCO.
    provider_locator_code
        Contains the Provider Locator Code of the Provider Reservation that
        houses this MCO.
    pseudo_city_code
        The PCC in the host system.
    expiry_date
        E-Voucher’s Expiry Date. This expiry date is specific to Rail
        product
    """

    class Meta:
        name = "MCO"
        namespace = "http://www.travelport.com/schema/common_v38_0"

    form_of_payment: list[FormOfPayment8] = field(
        default_factory=list,
        metadata={
            "name": "FormOfPayment",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    endorsement: None | Endorsement6 = field(
        default=None,
        metadata={
            "name": "Endorsement",
            "type": "Element",
        },
    )
    mcoexchange_info: None | McoexchangeInfo6 = field(
        default=None,
        metadata={
            "name": "MCOExchangeInfo",
            "type": "Element",
        },
    )
    mcofee_info: None | McofeeInfo6 = field(
        default=None,
        metadata={
            "name": "MCOFeeInfo",
            "type": "Element",
        },
    )
    mcoremark: list[Mcoremark6] = field(
        default_factory=list,
        metadata={
            "name": "MCORemark",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    mcoprice_data: None | McopriceData6 = field(
        default=None,
        metadata={
            "name": "MCOPriceData",
            "type": "Element",
        },
    )
    stock_control: list[StockControl6] = field(
        default_factory=list,
        metadata={
            "name": "StockControl",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    mcotext: list[Mcotext6] = field(
        default_factory=list,
        metadata={
            "name": "MCOText",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    ticket_type: None | str = field(
        default=None,
        metadata={
            "name": "TicketType",
            "type": "Attribute",
        },
    )
    ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Attribute",
        },
    )
    mcoissued: None | bool = field(
        default=None,
        metadata={
            "name": "MCOIssued",
            "type": "Attribute",
            "required": True,
        },
    )
    mcoissue_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "MCOIssueDate",
            "type": "Attribute",
        },
    )
    mcodoc_num: None | str = field(
        default=None,
        metadata={
            "name": "MCODocNum",
            "type": "Attribute",
        },
    )
    issue_reason_code: None | str = field(
        default=None,
        metadata={
            "name": "IssueReasonCode",
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
    tour_operator: None | str = field(
        default=None,
        metadata={
            "name": "TourOperator",
            "type": "Attribute",
        },
    )
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
        },
    )
    tour_code: None | str = field(
        default=None,
        metadata={
            "name": "TourCode",
            "type": "Attribute",
        },
    )
    provider_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 5,
        },
    )
    provider_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "ProviderLocatorCode",
            "type": "Attribute",
            "max_length": 15,
        },
    )
    pseudo_city_code: None | str = field(
        default=None,
        metadata={
            "name": "PseudoCityCode",
            "type": "Attribute",
            "min_length": 2,
            "max_length": 10,
        },
    )
    expiry_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "ExpiryDate",
            "type": "Attribute",
        },
    )
