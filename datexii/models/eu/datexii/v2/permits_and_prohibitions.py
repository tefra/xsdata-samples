from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.regulation_enum import RegulationEnum
from datexii.models.eu.datexii.v2.rest_area_activity_enum import (
    RestAreaActivityEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PermitsAndProhibitions:
    """
    Defines sets of action and regulations to specify permitted and
    prohibited issues.

    :ivar activity: An activity, which is regulated.
    :ivar regulation: Regulation for the specified activity.
    :ivar permits_and_prohibitions_extension:
    """

    activity: RestAreaActivityEnum | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    regulation: RegulationEnum | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    permits_and_prohibitions_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "permitsAndProhibitionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
