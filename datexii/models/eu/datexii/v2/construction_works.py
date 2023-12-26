from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.construction_work_type_enum import (
    ConstructionWorkTypeEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.roadworks import Roadworks

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ConstructionWorks(Roadworks):
    """
    Roadworks involving the construction of new infrastructure.

    :ivar construction_work_type: The type of construction work being
        performed.
    :ivar construction_works_extension:
    """

    construction_work_type: Optional[ConstructionWorkTypeEnum] = field(
        default=None,
        metadata={
            "name": "constructionWorkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    construction_works_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "constructionWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
