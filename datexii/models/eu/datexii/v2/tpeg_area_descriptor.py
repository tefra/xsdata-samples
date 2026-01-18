from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_descriptor import TpegDescriptor
from datexii.models.eu.datexii.v2.tpeg_loc03_area_descriptor_subtype_enum import (
    TpegLoc03AreaDescriptorSubtypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegAreaDescriptor(TpegDescriptor):
    """
    A descriptor for describing an area location.

    :ivar tpeg_area_descriptor_type: The nature of the descriptor used
        to define the location under consideration (derived from the
        TPEG Loc table 03).
    :ivar tpeg_area_descriptor_extension:
    """

    tpeg_area_descriptor_type: TpegLoc03AreaDescriptorSubtypeEnum | None = (
        field(
            default=None,
            metadata={
                "name": "tpegAreaDescriptorType",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
                "required": True,
            },
        )
    )
    tpeg_area_descriptor_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "tpegAreaDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
