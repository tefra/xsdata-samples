from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class EmdtravelerInfo:
    """
    EMD traveler information.

    Supported providers are 1G/1V/1P.

    Parameters
    ----------
    name_info
        Name information of the EMD traveler.
    traveler_type
        Defines the type of traveler used for booking which could be a non-
        defining type (Companion, Web-fare, etc), or a standard type (Adult,
        Child, etc).
    age
        Age of the traveler
    """

    class Meta:
        name = "EMDTravelerInfo"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    name_info: None | EmdtravelerInfo.NameInfo = field(
        default=None,
        metadata={
            "name": "NameInfo",
            "type": "Element",
            "required": True,
        },
    )
    traveler_type: None | str = field(
        default=None,
        metadata={
            "name": "TravelerType",
            "type": "Attribute",
            "min_length": 3,
            "max_length": 5,
        },
    )
    age: None | int = field(
        default=None,
        metadata={
            "name": "Age",
            "type": "Attribute",
        },
    )

    @dataclass
    class NameInfo:
        """
        Parameters
        ----------
        prefix
            Name prefix.
        first
            First Name.
        middle
            Midle name.
        last
            Last Name.
        suffix
            Name suffix.
        """

        prefix: None | str = field(
            default=None,
            metadata={
                "name": "Prefix",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 20,
            },
        )
        first: None | str = field(
            default=None,
            metadata={
                "name": "First",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 256,
            },
        )
        middle: None | str = field(
            default=None,
            metadata={
                "name": "Middle",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 256,
            },
        )
        last: None | str = field(
            default=None,
            metadata={
                "name": "Last",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 256,
            },
        )
        suffix: None | str = field(
            default=None,
            metadata={
                "name": "Suffix",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 256,
            },
        )
