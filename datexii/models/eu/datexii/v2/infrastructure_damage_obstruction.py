from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.infrastructure_damage_type_enum import (
    InfrastructureDamageTypeEnum,
)
from datexii.models.eu.datexii.v2.obstruction import Obstruction

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class InfrastructureDamageObstruction(Obstruction):
    """
    An obstruction on the road resulting from the failure or damage of
    infrastructure on, under, above or close to the road.

    :ivar infrastructure_damage_type: Characterization of an obstruction
        on the road resulting from the failure or damage of
        infrastructure on, under, above or close to the road.
    :ivar infrastructure_damage_obstruction_extension:
    """

    infrastructure_damage_type: InfrastructureDamageTypeEnum | None = field(
        default=None,
        metadata={
            "name": "infrastructureDamageType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    infrastructure_damage_obstruction_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "infrastructureDamageObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
