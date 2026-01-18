from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_loc03_ilc_point_descriptor_subtype_enum import (
    TpegLoc03IlcPointDescriptorSubtypeEnum,
)
from datexii.models.eu.datexii.v2.tpeg_point_descriptor import (
    TpegPointDescriptor,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegIlcPointDescriptor(TpegPointDescriptor):
    """
    A descriptor for describing a junction by defining the intersecting
    roads.

    :ivar tpeg_ilc_point_descriptor_type: The nature of the descriptor
        used to define the location under consideration (derived from
        the TPEG Loc table 03).
    :ivar tpeg_ilc_point_descriptor_extension:
    """

    tpeg_ilc_point_descriptor_type: TpegLoc03IlcPointDescriptorSubtypeEnum | None = field(
        default=None,
        metadata={
            "name": "tpegIlcPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    tpeg_ilc_point_descriptor_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "tpegIlcPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
