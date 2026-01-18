from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.vms_pictogram_display_area import (
    VmsPictogramDisplayArea,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class VmsMessagePictogramDisplayAreaIndexVmsPictogramDisplayArea:
    class Meta:
        name = "_VmsMessagePictogramDisplayAreaIndexVmsPictogramDisplayArea"

    vms_pictogram_display_area: VmsPictogramDisplayArea = field(
        metadata={
            "name": "vmsPictogramDisplayArea",
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
