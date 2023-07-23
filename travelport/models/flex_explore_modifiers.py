from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.flex_explore_modifiers_type import FlexExploreModifiersType

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlexExploreModifiers:
    """This is the container for a set of modifiers which allow the user to perform
    a special kind of low fare search, depicted as flex explore, based on different
    parameters like Area, Zone, Country, State, Specific locations, Distance around
    the actual destination of the itinerary.

    Applicable for providers 1G,1V,1P

    Parameters
    ----------
    destination
        List of specific destinations for performing flex explore.
        Applicable only with flex explore type - Destination
    type_value
        Type of flex explore to be performed
    radius
        Radius around the destination of actual itinerary in which the
        search would be performed. Supported only with types -
        DistanceInMiles and DistanceInKilometers
    group_name
        Group name for a set of destinations to be searched.  Use with
        Type=Group. Group names are defined in the Search Control Console.
        Supported Providers:  1G/1V/1P
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    destination: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Destination",
            "type": "Element",
            "max_occurs": 59,
            "length": 3,
            "white_space": "collapse",
        }
    )
    type_value: None | FlexExploreModifiersType = field(
        default=None,
        metadata={
            "name": "Type",
            "type": "Attribute",
            "required": True,
        }
    )
    radius: None | int = field(
        default=None,
        metadata={
            "name": "Radius",
            "type": "Attribute",
        }
    )
    group_name: None | str = field(
        default=None,
        metadata={
            "name": "GroupName",
            "type": "Attribute",
            "max_length": 15,
        }
    )
