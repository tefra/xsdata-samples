from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.header_information import HeaderInformation
from datexii.models.eu.datexii.v2.payload_publication import PayloadPublication
from datexii.models.eu.datexii.v2.predefined_location_container import (
    PredefinedLocationContainer,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PredefinedLocationsPublication(PayloadPublication):
    """
    A publication containing one or more groups of predefined locations
    organised either as litineraries, non ordered groups or as individual
    locations.
    """

    header_information: HeaderInformation | None = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    predefined_location_container: list[PredefinedLocationContainer] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocationContainer",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    predefined_locations_publication_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "predefinedLocationsPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
