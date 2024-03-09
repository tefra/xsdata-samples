from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass
class AppliedProfileCriteria:
    """
    Traveler Applied Profile Id for Searching misc traveler information.

    Parameters
    ----------
    traveler_profile_id
        Search with Traveler Applied Profile Id
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    traveler_profile_id: None | int = field(
        default=None,
        metadata={
            "name": "TravelerProfileId",
            "type": "Attribute",
        },
    )
