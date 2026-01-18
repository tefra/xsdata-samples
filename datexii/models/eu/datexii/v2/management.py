from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.filter_exit_management import (
    FilterExitManagement,
)
from datexii.models.eu.datexii.v2.life_cycle_management import (
    LifeCycleManagement,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Management:
    """
    Information relating to the management of the situation record.
    """

    life_cycle_management: None | LifeCycleManagement = field(
        default=None,
        metadata={
            "name": "lifeCycleManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    filter_exit_management: None | FilterExitManagement = field(
        default=None,
        metadata={
            "name": "filterExitManagement",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    management_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "managementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
