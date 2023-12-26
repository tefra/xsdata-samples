from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_loc03_junction_point_descriptor_subtype_enum import (
    TpegLoc03JunctionPointDescriptorSubtypeEnum,
)
from datexii.models.eu.datexii.v2.tpeg_point_descriptor import (
    TpegPointDescriptor,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegJunctionPointDescriptor(TpegPointDescriptor):
    """
    A descriptor for describing a point at a junction on a road network.

    :ivar tpeg_junction_point_descriptor_type: The nature of the
        descriptor used to define the location under consideration
        (derived from the TPEG Loc table 03).
    :ivar tpeg_junction_point_descriptor_extension:
    """

    tpeg_junction_point_descriptor_type: Optional[
        TpegLoc03JunctionPointDescriptorSubtypeEnum
    ] = field(
        default=None,
        metadata={
            "name": "tpegJunctionPointDescriptorType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    tpeg_junction_point_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegJunctionPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
