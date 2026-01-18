from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.travelport.com/schema/common_v38_0"


@dataclass(kw_only=True)
class Location6:
    """
    Used during search to specify an origin or destination location.
    """

    class Meta:
        name = "Location"
