from dataclasses import dataclass, field
from typing import List, Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_people_involved import (
    GroupOfPeopleInvolved,
)
from datexii.models.eu.datexii.v2.obstruction import Obstruction
from datexii.models.eu.datexii.v2.obstruction_type_enum import (
    ObstructionTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class GeneralObstruction(Obstruction):
    """
    Any stationary or moving obstacle of a physical nature, other than of an
    animal, vehicle, environmental, or damaged equipment nature.

    :ivar obstruction_type: Characterization of the type of general
        obstruction.
    :ivar group_of_people_involved:
    :ivar general_obstruction_extension:
    """

    obstruction_type: List[ObstructionTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "obstructionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    group_of_people_involved: List[GroupOfPeopleInvolved] = field(
        default_factory=list,
        metadata={
            "name": "groupOfPeopleInvolved",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    general_obstruction_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "generalObstructionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
