from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.travelport.com/schema/common_v32_0"


@dataclass
class Location2:
    """
    Used during search to specify an origin or destination location.
    """

    class Meta:
        name = "Location"
