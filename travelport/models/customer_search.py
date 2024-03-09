from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class CustomerSearch:
    """
    Detailed customer information for searching pre pay profiles.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"
