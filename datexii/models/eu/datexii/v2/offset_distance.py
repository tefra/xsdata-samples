from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OffsetDistance:
    """
    The non negative offset distance from the ALERT-C referenced point to
    the actual point.

    :ivar offset_distance: The non negative offset distance from the
        ALERT-C referenced point to the actual point. The ALERT-C
        locations in the Primary and Secondary locations must always
        encompass the linear section being specified, thus Offset
        Distance is towards the other point.
    :ivar offset_distance_extension:
    """

    offset_distance: int | None = field(
        default=None,
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    offset_distance_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "offsetDistanceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
