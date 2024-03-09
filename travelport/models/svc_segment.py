from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SvcSegment:
    """Service segment added to collect additional fee.

    1P only

    Parameters
    ----------
    key
        The Key of SVC Segment.
    carrier
        The platting carrier
    status
    number_of_items
    origin
        Origin location - Airport code. 1P only.
    destination
        Destination location - Airport code. 1P only.
    start_date
        Start date of the segment. Generally it is the next date after the
        last air segment. 1P only
    travel_order
        To identify the appropriate travel sequence for
        Air/Car/Hotel/Passive segments/reservations based on travel dates.
        This ordering is applicable across the UR not provider or traveler
        specific
    booking_traveler_ref
    rfic
        1P - Reason for issuance
    rfisc
        1P - Resaon for issuance sub-code
    svc_description
        1P - SVC fee description
    fee
        The fee to be collected using SVC segment
    emdnumber
        Generated EMD number, if EMD is issued on the SVC
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        },
    )
    status: None | str = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Attribute",
        },
    )
    number_of_items: None | int = field(
        default=None,
        metadata={
            "name": "NumberOfItems",
            "type": "Attribute",
        },
    )
    origin: None | str = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    destination: None | str = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Attribute",
            "length": 3,
            "white_space": "collapse",
        },
    )
    start_date: None | XmlDate = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Attribute",
        },
    )
    travel_order: None | int = field(
        default=None,
        metadata={
            "name": "TravelOrder",
            "type": "Attribute",
        },
    )
    booking_traveler_ref: None | str = field(
        default=None,
        metadata={
            "name": "BookingTravelerRef",
            "type": "Attribute",
        },
    )
    rfic: None | str = field(
        default=None,
        metadata={
            "name": "RFIC",
            "type": "Attribute",
        },
    )
    rfisc: None | str = field(
        default=None,
        metadata={
            "name": "RFISC",
            "type": "Attribute",
        },
    )
    svc_description: None | str = field(
        default=None,
        metadata={
            "name": "SvcDescription",
            "type": "Attribute",
        },
    )
    fee: None | str = field(
        default=None,
        metadata={
            "name": "Fee",
            "type": "Attribute",
        },
    )
    emdnumber: None | str = field(
        default=None,
        metadata={
            "name": "EMDNumber",
            "type": "Attribute",
            "length": 13,
        },
    )
