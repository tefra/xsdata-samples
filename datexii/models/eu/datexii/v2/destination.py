from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Destination:
    """
    The specification a destination.

    This may be either a point location or an area location.
    """

    destination_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "destinationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
