from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class TpegDescriptor:
    """
    A collection of information providing descriptive references to locations using
    the TPEG-Loc location referencing approach.

    :ivar descriptor: A text string which describes or elaborates the
        location.
    :ivar tpeg_descriptor_extension:
    """

    descriptor: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    tpeg_descriptor_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "tpegDescriptorExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
