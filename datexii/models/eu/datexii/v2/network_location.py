from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.destination import Destination
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location import Location
from datexii.models.eu.datexii.v2.supplementary_positional_description import (
    SupplementaryPositionalDescription,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class NetworkLocation(Location):
    """
    The specification of a location on a network (as a point or a linear location).
    """

    supplementary_positional_description: Optional[
        SupplementaryPositionalDescription
    ] = field(
        default=None,
        metadata={
            "name": "supplementaryPositionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    destination: Optional[Destination] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    network_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "networkLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
