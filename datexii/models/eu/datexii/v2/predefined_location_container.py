from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PredefinedLocationContainer:
    """
    A container which may comprise the definition of a predefined
    itinerary, non ordered group of locations or single location.
    """

    predefined_location_container_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "predefinedLocationContainerExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
