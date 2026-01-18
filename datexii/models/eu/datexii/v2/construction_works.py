from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.construction_work_type_enum import (
    ConstructionWorkTypeEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.roadworks import Roadworks

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class ConstructionWorks(Roadworks):
    """
    Roadworks involving the construction of new infrastructure.

    :ivar construction_work_type: The type of construction work being
        performed.
    :ivar construction_works_extension:
    """

    construction_work_type: None | ConstructionWorkTypeEnum = field(
        default=None,
        metadata={
            "name": "constructionWorkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    construction_works_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "constructionWorksExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
