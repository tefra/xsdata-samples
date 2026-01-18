from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.activity import Activity
from datexii.models.eu.datexii.v2.disturbance_activity_type_enum import (
    DisturbanceActivityTypeEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class DisturbanceActivity(Activity):
    """
    Deliberate human action of either a public disorder nature or of a
    situation alert type which could disrupt traffic.

    :ivar disturbance_activity_type: Includes all situations of a public
        disorder type or of an alert type, with potential to disrupt
        traffic.
    :ivar disturbance_activity_extension:
    """

    disturbance_activity_type: DisturbanceActivityTypeEnum | None = field(
        default=None,
        metadata={
            "name": "disturbanceActivityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    disturbance_activity_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "disturbanceActivityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
