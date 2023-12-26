from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location import Location
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.predefined_location_container import (
    PredefinedLocationContainer,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PredefinedLocation(PredefinedLocationContainer):
    """
    An identifiable versioned instance of a single predefined location.

    :ivar predefined_location_name: A name assigned to the predefined
        location (e.g. extracted out of the network operator's
        gazetteer).
    :ivar location:
    :ivar predefined_location_extension:
    :ivar id:
    :ivar version:
    """

    predefined_location_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "predefinedLocationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    location: Optional[Location] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    predefined_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "predefinedLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
