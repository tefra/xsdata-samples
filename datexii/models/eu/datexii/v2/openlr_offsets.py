from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrOffsets:
    """
    Offsets are used to locate the start and end of a location more precisely than
    bounding to the nodes in a network.

    :ivar openlr_positive_offset: The positive offset along the line of
        the location.
    :ivar openlr_negative_offset: The negative offset along the line of
        the location.
    :ivar openlr_offsets_extension:
    """
    openlr_positive_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrPositiveOffset",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    openlr_negative_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "openlrNegativeOffset",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    openlr_offsets_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrOffsetsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
