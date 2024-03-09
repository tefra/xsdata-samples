from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_req_1 import BaseReq1

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class SavedTripRetrieveReq(BaseReq1):
    """
    Request to Retrieve saved Trip based on locatorcode.

    Parameters
    ----------
    locator_code
        Represents a valid Saved Trip locatorcode.
    traveler_last_name
        Match Traveler Last Name.
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
    traveler_last_name: None | str = field(
        default=None,
        metadata={
            "name": "TravelerLastName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 256,
        },
    )
