from dataclasses import dataclass, field
from typing import List, Optional

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

    name: List[TpegAreaDescriptor] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    tpeg_named_only_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegNamedOnlyAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
