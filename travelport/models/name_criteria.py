from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class NameCriteria:
    """
    Traveler First Name and Last Name for Searching misc traveler information.

    Parameters
    ----------
    first_name
        Search with Traveler First Name
    last_name
        Search with Traveler Last Name
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    first_name: None | str = field(
        default=None,
        metadata={
            "name": "FirstName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        },
    )
    last_name: None | str = field(
        default=None,
        metadata={
            "name": "LastName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 30,
        },
    )
