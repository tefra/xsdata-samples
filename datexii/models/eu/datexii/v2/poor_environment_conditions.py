from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.conditions import Conditions
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.humidity import Humidity
from datexii.models.eu.datexii.v2.pollution import Pollution
from datexii.models.eu.datexii.v2.poor_environment_type_enum import (
    PoorEnvironmentTypeEnum,
)
from datexii.models.eu.datexii.v2.precipitation_detail import (
    PrecipitationDetail,
)
from datexii.models.eu.datexii.v2.temperature import Temperature
from datexii.models.eu.datexii.v2.visibility import Visibility
from datexii.models.eu.datexii.v2.wind import Wind

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PoorEnvironmentConditions(Conditions):
    """
    Any environmental conditions which may be affecting the driving
    conditions on the road.

    :ivar poor_environment_type: The type of environment condition which
        is affecting driving conditions.
    :ivar precipitation_detail:
    :ivar visibility:
    :ivar pollution:
    :ivar temperature:
    :ivar wind:
    :ivar humidity:
    :ivar poor_environment_conditions_extension:
    """

    poor_environment_type: list[PoorEnvironmentTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "poorEnvironmentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    precipitation_detail: PrecipitationDetail | None = field(
        default=None,
        metadata={
            "name": "precipitationDetail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    visibility: Visibility | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    pollution: Pollution | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    temperature: Temperature | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    wind: Wind | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    humidity: Humidity | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    poor_environment_conditions_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "poorEnvironmentConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
