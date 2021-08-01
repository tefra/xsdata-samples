from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_last_location_reference_point import OpenlrLastLocationReferencePoint
from datexii.models.eu.datexii.v2.openlr_location_reference_point import OpenlrLocationReferencePoint
from datexii.models.eu.datexii.v2.openlr_offsets import OpenlrOffsets

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrLineLocationReference:
    """
    A LineLocationReference is defined by an ordered sequence of location
    reference points and a terminating last location reference point.
    """
    openlr_location_reference_point: List[OpenlrLocationReferencePoint] = field(
        default_factory=list,
        metadata={
            "name": "openlrLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        }
    )
    openlr_last_location_reference_point: Optional[OpenlrLastLocationReferencePoint] = field(
        default=None,
        metadata={
            "name": "openlrLastLocationReferencePoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_offsets: Optional[OpenlrOffsets] = field(
        default=None,
        metadata={
            "name": "openlrOffsets",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    openlr_line_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrLineLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
