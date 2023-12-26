from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location import Location
from datexii.models.eu.datexii.v2.predefined_location_versioned_reference import (
    PredefinedLocationVersionedReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LocationByReference(Location):
    """
    A location defined by reference to a predefined location.

    :ivar predefined_location_reference: A reference to a versioned
        predefined location.
    :ivar location_by_reference_extension:
    """

    predefined_location_reference: Optional[
        PredefinedLocationVersionedReference
    ] = field(
        default=None,
        metadata={
            "name": "predefinedLocationReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    location_by_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "locationByReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
