from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.co2_emission import Co2Emission

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class Co2Emissions:
    """
    The carbon emissions produced by the journey.

    Parameters
    ----------
    co2_emission
    total_value
        The total CO2 emission value for the journey
    unit
        The unit used in the TotalValue attribute
    category
        The category name of the type of cabin, either Economy or Premium.
        Premium is any cabin that is not considered Economy
    source
        The source responsible for the values
    """

    class Meta:
        name = "CO2Emissions"
        namespace = "http://www.travelport.com/schema/air_v52_0"

    co2_emission: list[Co2Emission] = field(
        default_factory=list,
        metadata={
            "name": "CO2Emission",
            "type": "Element",
            "max_occurs": 99,
        },
    )
    total_value: None | float = field(
        default=None,
        metadata={
            "name": "TotalValue",
            "type": "Attribute",
        },
    )
    unit: None | str = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        },
    )
    category: None | str = field(
        default=None,
        metadata={
            "name": "Category",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        },
    )
    source: None | str = field(
        default=None,
        metadata={
            "name": "Source",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 64,
        },
    )
