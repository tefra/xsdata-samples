from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.travelport.com/schema/common_v33_0"


@dataclass
class Location3:
    """
    Used during search to specify an origin or destination location.
    """

    class Meta:
        name = "Location"
