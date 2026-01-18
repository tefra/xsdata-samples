from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/vehicle_v52_0"


@dataclass(kw_only=True)
class VehicleSearchId:
    """
    A container for Vehicle Media Links Search Id.

    Parameters
    ----------
    media_links_search_id
        The search id  from VehicleSearchAvailabilityRsp to be used to
        retrieve the media links.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/vehicle_v52_0"

    media_links_search_id: str = field(
        metadata={
            "name": "MediaLinksSearchId",
            "type": "Attribute",
            "required": True,
        }
    )
