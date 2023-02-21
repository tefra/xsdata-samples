from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.openlr_base_location_reference_point import OpenlrBaseLocationReferencePoint
from datexii.models.eu.datexii.v2.openlr_path_attributes import OpenlrPathAttributes

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrLocationReferencePoint(OpenlrBaseLocationReferencePoint):
    """
    The basis of a location reference is a sequence of location reference points
    (LRPs).
    """
    openlr_path_attributes: Optional[OpenlrPathAttributes] = field(
        default=None,
        metadata={
            "name": "openlrPathAttributes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    openlr_location_reference_point_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "openlrLocationReferencePointExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
