from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_area_descriptor import (
    TpegAreaDescriptor,
)
from datexii.models.eu.datexii.v2.tpeg_area_location import TpegAreaLocation

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegNamedOnlyArea(TpegAreaLocation):
    """
    An area defined by a well-known name.

    :ivar name: Name of area.
    :ivar tpeg_named_only_area_extension:
    """

    name: list[TpegAreaDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    tpeg_named_only_area_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "tpegNamedOnlyAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
