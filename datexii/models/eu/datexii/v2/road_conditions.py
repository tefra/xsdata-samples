from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.conditions import Conditions
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class RoadConditions(Conditions):
    """
    Conditions of the road surface which may affect driving conditions.

    These may be related to the weather (e.g. ice, snow etc.) or to other
    conditions (e.g. oil, mud, leaves etc. on the road).
    """

    road_conditions_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "roadConditionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
