from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.animal_presence_type_enum import (
    AnimalPresenceTypeEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.obstruction import Obstruction

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class AnimalPresenceObstruction(Obstruction):
    """
    An obstruction on the road resulting from the presence of animals.

    :ivar alive: Indicates whether the identified animals are dead
        (immobile) or alive (potentially mobile).
    :ivar animal_presence_type: Indicates the nature of animals present
        on or near the roadway.
    :ivar animal_presence_obstruction_extension:
    """

    alive: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    animal_presence_type: AnimalPresenceTypeEnum | None = field(
        default=None,
        metadata={
            "name": "animalPresenceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    animal_presence_obstruction_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "animalPresenceObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
