from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SavedTripDeleteReq(BaseReq1):
    """
    Request to delete saved Trip.

    Parameters
    ----------
    locator_code
        Represents a valid Saved Trip locator code
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    locator_code: None | str = field(
        default=None,
        metadata={
            "name": "LocatorCode",
            "type": "Attribute",
            "min_length": 5,
            "max_length": 8,
        },
    )
