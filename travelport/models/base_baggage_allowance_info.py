from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.text_info import TextInfo
from travelport.models.urlinfo import Urlinfo

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass(kw_only=True)
class BaseBaggageAllowanceInfo:
    """
    This contains common elements that are used for Baggage Allowance info,
    carry-on allowance info and embargo Info.

    Supported providers are 1V/1G/1P.

    Parameters
    ----------
    urlinfo
        Contains the text and URL information as published by carrier.
    text_info
        Text information as published by carrier.
    origin
    destination
    carrier
    """

    urlinfo: list[Urlinfo] = field(
        default_factory=list,
        metadata={
            "name": "URLInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
        },
    )
    text_info: list[TextInfo] = field(
        default_factory=list,
        metadata={
            "name": "TextInfo",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/air_v52_0",
            "max_occurs": 999,
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
    carrier: None | str = field(
        default=None,
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "length": 2,
        },
    )
