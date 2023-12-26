from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.micrograms_concentration_value import (
    MicrogramsConcentrationValue,
)
from datexii.models.eu.datexii.v2.pollutant_type_enum import PollutantTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Pollution:
    """
    Details of atmospheric pollution.

    :ivar pollutant_type: The type of pollutant in the air.
    :ivar pollutant_concentration: The average concentration of the
        pollutant in the air.
    :ivar pollution_extension:
    """

    pollutant_type: Optional[PollutantTypeEnum] = field(
        default=None,
        metadata={
            "name": "pollutantType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    pollutant_concentration: Optional[MicrogramsConcentrationValue] = field(
        default=None,
        metadata={
            "name": "pollutantConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pollution_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "pollutionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
