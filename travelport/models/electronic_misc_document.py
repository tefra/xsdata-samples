from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from travelport.models.emdcoupon import Emdcoupon
from travelport.models.type_element_status_1 import TypeElementStatus1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class ElectronicMiscDocument:
    """
    Electronic miscellaneous document.

    Supported providers are 1G/1V/1P.

    Parameters
    ----------
    emdcoupon
        The coupon information for the EMD issued.
    number
        EMD Number
    primary_document_indicator
        Indicates whether the EMD is a primary EMD.
    in_conjunction_with
        Returns the number of the Primary EMD, if this EMD is a conjunctive
        EMD
    associated_ticket_number
        This number indicates the e-Ticket number associated with this EMD
    plating_carrier
        Plating carrier code for which this EMD is issued
    issue_date
        Issue Date for this EMD
    status
        Status of the EMD calculated on the basis of coupon status. Possible
        values Open, Void, Refunded, Exchanged, Irregular Operations,Airport
        Control, Checked In, Flown/Used, Boarded/Lifted, Suspended, Unknown
    key
        System generated Key
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

    emdcoupon: list[Emdcoupon] = field(
        default_factory=list,
        metadata={
            "name": "EMDCoupon",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    number: str = field(
        metadata={
            "name": "Number",
            "type": "Attribute",
            "required": True,
            "length": 13,
        }
    )
    primary_document_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "PrimaryDocumentIndicator",
            "type": "Attribute",
        },
    )
    in_conjunction_with: None | str = field(
        default=None,
        metadata={
            "name": "InConjunctionWith",
            "type": "Attribute",
            "length": 13,
        },
    )
    associated_ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "AssociatedTicketNumber",
            "type": "Attribute",
            "length": 13,
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
    issue_date: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "IssueDate",
            "type": "Attribute",
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
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
