from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_area_location_reference import (
    OpenlrAreaLocationReference,
)
from datexii.models.eu.datexii.v2.openlr_line_attributes import (
    OpenlrLineAttributes,
)
from datexii.models.eu.datexii.v2.openlr_location_reference_point import (
    OpenlrLocationReferencePoint,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrClosedLineLocationReference(OpenlrAreaLocationReference):
    """
    the openLR method of areadefinition by providing a closed path (i.e. a
    circuit) in the road network.

    The boundary always consists of road segments.
    """

    openlr_location_reference_point: list[OpenlrLocationReferencePoint] = (
        field(
            default_factory=list,
            metadata={
                "name": "openlrLocationReferencePoint",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
                "min_occurs": 1,
            },
        )
    )
    openlr_last_line: OpenlrLineAttributes | None = field(
        default=None,
        metadata={
            "name": "openlrLastLine",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_closed_line_location_reference_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "openlrClosedLineLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
