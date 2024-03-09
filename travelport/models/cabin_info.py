from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/cruise_v52_0"


@dataclass
class CabinInfo:
    """
    Cruise Cabin Details.

    Parameters
    ----------
    category
        Vendor defined Cabin category
    number
        Vendor defined cabin designator Or Cabin Number
    location
        Cabin Category , can be of the following values : ''I' - Inside
        Cabins, 'O' - Outside Cabins, 'M' - Inside and Outside Cabins
        (mixed)
    relative_location
        Position of the cabin relative to the layout of the ship, e.g.
        OUT,AFT,PORT
    deck_name
        Ship's deck on which cabin resides.
    bed_configuration
        Description of the cabin bed configuration e.g. TWIN BEDS
    smoking_indicator
        Whether user has specified his smoking preference.Can be of the
        following values : true' - Smoking' 'false' - Non-smoking
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/cruise_v52_0"

    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 3,
        },
    )
    number: None | str = field(
        default=None,
        metadata={
            "name": "Number",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 5,
        },
    )
    location: None | str = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Attribute",
            "length": 1,
        },
    )
    relative_location: None | str = field(
        default=None,
        metadata={
            "name": "RelativeLocation",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 12,
        },
    )
    deck_name: None | str = field(
        default=None,
        metadata={
            "name": "DeckName",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 15,
        },
    )
    bed_configuration: None | str = field(
        default=None,
        metadata={
            "name": "BedConfiguration",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 10,
        },
    )
    smoking_indicator: None | bool = field(
        default=None,
        metadata={
            "name": "SmokingIndicator",
            "type": "Attribute",
        },
    )
