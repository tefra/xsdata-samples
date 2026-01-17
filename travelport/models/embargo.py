from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Embargo:
    """
    Embargo details.

    Provider: 1G, 1V, 1P.

    Parameters
    ----------
    key
    carrier
    segment_ref
    name
        The commercial name of the optional service on which the embargo
        applies. Provider: 1G, 1V, 1P
    text
        Brief description of the embargo. Provider: 1G, 1V, 1P
    secondary_type
        The secondary type of the optional service on which the embargo
        applies.  Provider: 1G, 1V, 1P
    type_value
        The type of optional service on which the embargo applies.
        Provider: 1G, 1V, 1P
    url
        Website of the operating carrier. Provider: 1G, 1V, 1P
    service_sub_code
        The service sub code of the optional service on which the embargo
        applies.  Provider: 1G, 1V, 1P
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
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
    segment_ref: None | str = field(
        default=None,
        metadata={
            "name": "SegmentRef",
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "max_length": 30,
        },
    )
    text: None | str = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Attribute",
        },
    )
    secondary_type: None | str = field(
        default=None,
        metadata={
            "name": "SecondaryType",
            "type": "Attribute",
        },
    )
    type_value: None | str = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    url: None | str = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Attribute",
        },
    )
    service_sub_code: None | str = field(
        default=None,
        metadata={
            "name": "ServiceSubCode",
            "type": "Attribute",
            "max_length": 3,
        },
    )
