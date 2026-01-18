from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_area_location_reference import (
    OpenlrAreaLocationReference,
)
from datexii.models.eu.datexii.v2.openlr_grid_attributes import (
    OpenlrGridAttributes,
)
from datexii.models.eu.datexii.v2.openlr_rectangle import OpenlrRectangle

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrGridLocationReference(OpenlrAreaLocationReference):
    """
    the openLR method of areadefinition by providing repeating rectangles.
    """

    openlr_rectangle: OpenlrRectangle | None = field(
        default=None,
        metadata={
            "name": "openlrRectangle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_grid_attributes: OpenlrGridAttributes | None = field(
        default=None,
        metadata={
            "name": "openlrGridAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_grid_location_reference_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "openlrGridLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
