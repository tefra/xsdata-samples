from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class PersonNameSearch:
    """
    Customer name field.

    Parameters
    ----------
    last
        Person Last Name to be searched for Flight Pass content.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    last: None | str = field(
        default=None,
        metadata={
            "name": "Last",
            "type": "Attribute",
            "required": True,
            "min_length": 1,
            "max_length": 64,
        },
    )
