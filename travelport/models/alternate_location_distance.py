from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.distance_1 import Distance1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AlternateLocationDistance:
    """
    Information about the Original Search Airport to Alternate Search Airport.

    Parameters
    ----------
    distance
    key
    search_location
        The Searching City or Airport specified in the Request.
    alternate_location
        The nearby Alternate City or Airport to SearchLocation.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    distance: None | Distance1 = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.travelport.com/schema/common_v52_0",
            "required": True,
        },
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
            "required": True,
        },
    )
    search_location: None | str = field(
        default=None,
        metadata={
            "name": "SearchLocation",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
    alternate_location: None | str = field(
        default=None,
        metadata={
            "name": "AlternateLocation",
            "type": "Attribute",
            "required": True,
            "length": 3,
            "white_space": "collapse",
        },
    )
