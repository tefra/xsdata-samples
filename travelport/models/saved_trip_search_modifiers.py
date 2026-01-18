from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.base_search_modifiers import BaseSearchModifiers

__NAMESPACE__ = "http://www.travelport.com/schema/universal_v52_0"


@dataclass(kw_only=True)
class SavedTripSearchModifiers(BaseSearchModifiers):
    """
    Controls and switches for the SavedTrip Search request.

    Parameters
    ----------
    saved_trip_name
        Represents name of a savedTrip.
    exclude_urassociated
        Exclude SavedTrips associated with a UniversalRecord.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/universal_v52_0"

    saved_trip_name: None | str = field(
        default=None,
        metadata={
            "name": "SavedTripName",
            "type": "Attribute",
        },
    )
    exclude_urassociated: bool = field(
        default=True,
        metadata={
            "name": "ExcludeURAssociated",
            "type": "Attribute",
        },
    )
