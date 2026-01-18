from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location import Location
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.predefined_location_container import (
    PredefinedLocationContainer,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
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

    predefined_location_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "predefinedLocationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    location: Location = field(
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    predefined_location_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "predefinedLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
