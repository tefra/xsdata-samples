from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.mcoinformation_1 import Mcoinformation1
from travelport.models.tcrinfo import Tcrinfo
from travelport.models.ticket_info import TicketInfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class DocumentInfo:
    """
    Container for the document information summary line.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    ticket_info: list[TicketInfo] = field(
        default_factory=list,
        metadata={
            "name": "TicketInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    mcoinfo: list[Mcoinformation1] = field(
        default_factory=list,
        metadata={
            "name": "MCOInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
    tcrinfo: list[Tcrinfo] = field(
        default_factory=list,
        metadata={
            "name": "TCRInfo",
            "type": "Element",
            "max_occurs": 999,
        },
    )
