from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_base_location_reference_point import (
    OpenlrBaseLocationReferencePoint,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrLastLocationReferencePoint(OpenlrBaseLocationReferencePoint):
    """
    The sequence of location reference points is terminated by a last location
    reference point.
    """

    openlr_last_location_reference_point_extension: Optional[ExtensionType] = (
        field(
            default=None,
            metadata={
                "name": "openlrLastLocationReferencePointExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
