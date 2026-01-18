from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.vms_pictogram_display_characteristics import (
    VmsPictogramDisplayCharacteristics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class VmsRecordPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics:
    class Meta:
        name = "_VmsRecordPictogramDisplayAreaIndexVmsPictogramDisplayCharacteristics"

    vms_pictogram_display_characteristics: VmsPictogramDisplayCharacteristics = field(
        metadata={
            "name": "vmsPictogramDisplayCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    pictogram_display_area_index: int = field(
        metadata={
            "name": "pictogramDisplayAreaIndex",
            "type": "Attribute",
            "required": True,
        }
    )
