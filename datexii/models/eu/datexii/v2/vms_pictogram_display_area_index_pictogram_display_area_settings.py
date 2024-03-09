from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.pictogram_display_area_settings import (
    PictogramDisplayAreaSettings,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsPictogramDisplayAreaIndexPictogramDisplayAreaSettings:
    class Meta:
        name = "_VmsPictogramDisplayAreaIndexPictogramDisplayAreaSettings"

    pictogram_display_area_settings: Optional[PictogramDisplayAreaSettings] = (
        field(
            default=None,
            metadata={
                "name": "pictogramDisplayAreaSettings",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
                "required": True,
            },
        )
    )
    pictogram_display_area_index: Optional[int] = field(
        default=None,
        metadata={
            "name": "pictogramDisplayAreaIndex",
            "type": "Attribute",
            "required": True,
        },
    )
