from __future__ import annotations

from dataclasses import dataclass, field

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
    The specification of a location on a network (as a point or a linear
    location).
    """

    supplementary_positional_description: (
        None | SupplementaryPositionalDescription
    ) = field(
        default=None,
        metadata={
            "name": "supplementaryPositionalDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    destination: None | Destination = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    network_location_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "networkLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
