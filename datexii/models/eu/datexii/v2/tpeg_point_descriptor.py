from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.tpeg_descriptor import TpegDescriptor

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegPointDescriptor(TpegDescriptor):
    """
    A descriptor for describing a point location.
    """

    tpeg_point_descriptor_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "tpegPointDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
