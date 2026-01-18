from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.vms_pictogram_display_characteristics import (
    VmsPictogramDisplayCharacteristics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsDynamicCharacteristicsPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics:
    class Meta:
        name = "_VmsDynamicCharacteristicsPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics"

    vms_pictogram_display_characteristics: (
        VmsPictogramDisplayCharacteristics | None
    ) = field(
        default=None,
        metadata={
            "name": "vmsPictogramDisplayCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    pictogram_display_area_index: int | None = field(
        default=None,
        metadata={
            "name": "pictogramDisplayAreaIndex",
            "type": "Attribute",
            "required": True,
        },
    )
