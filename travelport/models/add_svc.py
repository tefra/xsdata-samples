from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.travelport.com/schema/common_v52_0"


@dataclass
class AddSvc:
    """
    1P - Add SVC segments to collect additional fee.

    Parameters
    ----------
    rfic
        1P - Reason for issuance
    rfisc
        1P - Resaon for issuance sub-code
    svc_description
        1P - SVC fee description
    origin
        Origin location - Airport code. If this value not provided, the last
        air segment arrival location is taken as default. 1P only.
    destination
        Destination location - Airport code.
    start_date
        The start date of the SVC segment. If the value not specified, the
        default value is set as the date next to the last airsegment arrival
        date. 1P only
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/common_v52_0"

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
