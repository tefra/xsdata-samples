from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.openlr_area_location_reference import (
    OpenlrAreaLocationReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrExtendedArea:
    """
    Extension to provide Area information in openLR format.
    """

    openlr_area_location_reference: OpenlrAreaLocationReference | None = field(
        default=None,
        metadata={
            "name": "openlrAreaLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
