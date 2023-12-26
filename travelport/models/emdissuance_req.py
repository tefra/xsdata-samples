from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1
from travelport.models.issuance_modifiers import IssuanceModifiers
from travelport.models.provider_reservation_detail_1 import (
    ProviderReservationDetail1,
)
from travelport.models.selection_modifiers import SelectionModifiers

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class EmdissuanceReq(BaseReq1):
    """
    Electronic Miscellaneous Document issuance request.Supported providers are
    1V/1G/1P.

    Parameters
    ----------
    provider_reservation_detail
        PNR information for which EMD is going to be issued.
    ticket_number
        Ticket number for which EMD is going to be issued.Required for EMD-A
        issuance.
    issuance_modifiers
        General modifiers related to EMD issuance.
    selection_modifiers
        Modifiers related to selection of services during EMD issuance.
    universal_record_locator_code
        Represents a valid Universal Record locator code.
    show_details
        This attribute gives the control to request for complete information
        on Issued EMDs or minimal information.Requesting complete
        information leads to possible multiple supplier calls for fetching
        all the details.
    issue_all_open_svc
        Issues EMDS to all SVC segments. If it is true, TicketNumber and SVC
        segment reference need not be provided. Supported provider 1P.
    """

    class Meta:
        name = "EMDIssuanceReq"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    provider_reservation_detail: None | ProviderReservationDetail1 = field(
        default=None,
        metadata={
            "name": "ProviderReservationDetail",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        },
    )
    ticket_number: None | str = field(
        default=None,
        metadata={
            "name": "TicketNumber",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "min_length": 1,
            "max_length": 13,
        },
    )
    issuance_modifiers: None | IssuanceModifiers = field(
        default=None,
        metadata={
            "name": "IssuanceModifiers",
            "type": "Element",
        },
    )
    selection_modifiers: None | SelectionModifiers = field(
        default=None,
        metadata={
            "name": "SelectionModifiers",
            "type": "Element",
        },
    )
    universal_record_locator_code: None | str = field(
        default=None,
        metadata={
            "name": "UniversalRecordLocatorCode",
            "type": "Attribute",
            "required": True,
            "min_length": 5,
            "max_length": 8,
        },
    )
    show_details: bool = field(
        default=False,
        metadata={
            "name": "ShowDetails",
            "type": "Attribute",
        },
    )
    issue_all_open_svc: bool = field(
        default=False,
        metadata={
            "name": "IssueAllOpenSVC",
            "type": "Attribute",
        },
    )
