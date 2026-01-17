from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Dimension:
    """
    A component that provides dimension information.

    The product of width and height must not be necessarily be the square
    footage (e.g. in multi-storey buildings or when some zones are not part
    of the square footage).

    :ivar dimension_length: Length.
    :ivar dimension_width: Width.
    :ivar dimension_height: Height.
    :ivar dimension_usable_area: The area measured in square metres,
        that is available for some specific purpose.
    :ivar dimension_extension:
    """

    dimension_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "dimensionLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dimension_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "dimensionWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dimension_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "dimensionHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dimension_usable_area: Optional[int] = field(
        default=None,
        metadata={
            "name": "dimensionUsableArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dimension_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dimensionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
