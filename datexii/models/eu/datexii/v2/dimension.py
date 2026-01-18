from dataclasses import dataclass, field

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

    dimension_length: float | None = field(
        default=None,
        metadata={
            "name": "dimensionLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dimension_width: float | None = field(
        default=None,
        metadata={
            "name": "dimensionWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dimension_height: float | None = field(
        default=None,
        metadata={
            "name": "dimensionHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dimension_usable_area: int | None = field(
        default=None,
        metadata={
            "name": "dimensionUsableArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dimension_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "dimensionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
