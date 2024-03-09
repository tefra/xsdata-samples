from dataclasses import dataclass, field
from typing import Optional

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
    The openLR method of areadefinition by providing repeating rectangles.
    """

    openlr_rectangle: Optional[OpenlrRectangle] = field(
        default=None,
        metadata={
            "name": "openlrRectangle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_grid_attributes: Optional[OpenlrGridAttributes] = field(
        default=None,
        metadata={
            "name": "openlrGridAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_grid_location_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrGridLocationReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
