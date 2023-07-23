from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.add_pnr_element import AddPnrElement
from travelport.models.booking_base_req import BookingBaseReq
from travelport.models.delete_pnr_element import DeletePnrElement
from travelport.models.update_pnr_element import UpdatePnrElement

__NAMESPACE__ = "http://www.travelport.com/schema/sharedBooking_v52_0"


@dataclass
class BookingPnrElementReq(BookingBaseReq):
    """
    Adds, Modifies PNR elemnts like OSI, FOP, review booking, remarks, and action
    status.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/sharedBooking_v52_0"

    add_pnr_element: None | AddPnrElement = field(
        default=None,
        metadata={
            "name": "AddPnrElement",
            "type": "Element",
        }
    )
    update_pnr_element: None | UpdatePnrElement = field(
        default=None,
        metadata={
            "name": "UpdatePnrElement",
            "type": "Element",
        }
    )
    delete_pnr_element: None | DeletePnrElement = field(
        default=None,
        metadata={
            "name": "DeletePnrElement",
            "type": "Element",
        }
    )
