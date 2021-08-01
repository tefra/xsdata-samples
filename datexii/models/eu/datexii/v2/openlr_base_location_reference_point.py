from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_line_attributes import OpenlrLineAttributes
from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrBaseLocationReferencePoint:
    """
    Base class used to hold data about a reference point.
    """
    openlr_coordinate: Optional[PointCoordinates] = field(
        default=None,
        metadata={
            "name": "openlrCoordinate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_line_attributes: Optional[OpenlrLineAttributes] = field(
        default=None,
        metadata={
            "name": "openlrLineAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_base_location_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrBaseLocationReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
