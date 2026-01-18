from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_loc03_other_point_descriptor_subtype_enum import (
    TpegLoc03OtherPointDescriptorSubtypeEnum,
)
from datexii.models.eu.datexii.v2.tpeg_point_descriptor import (
    TpegPointDescriptor,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegOtherPointDescriptor(TpegPointDescriptor):
    """
    General descriptor for describing a point.

    :ivar tpeg_other_point_descriptor_type: The nature of the descriptor
        used to define the location under consideration (derived from
        the TPEG Loc table 03).
    :ivar tpeg_other_point_descriptor_extension:
    """

    tpeg_other_point_descriptor_type: (
        TpegLoc03OtherPointDescriptorSubtypeEnum | None
    ) = field(
        default=None,
        metadata={
            "name": "tpegOtherPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    tpeg_other_point_descriptor_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "tpegOtherPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
