from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.non_ordered_locations import (
    NonOrderedLocations,
)
from datexii.models.eu.datexii.v2.predefined_non_ordered_location_group_versioned_reference import (
    PredefinedNonOrderedLocationGroupVersionedReference,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class NonOrderedLocationGroupByReference(NonOrderedLocations):
    """
    A group of (i.e. more than one) physically separate locations which
    have no specific order that are defined by reference to a predefined
    non ordered location group.

    :ivar predefined_non_ordered_location_group_reference: A reference
        to a versioned instance of a predefined non ordered location
        group as specified in a PredefinedLocationsPublication.
    :ivar non_ordered_location_group_by_reference_extension:
    """

    predefined_non_ordered_location_group_reference: (
        None | PredefinedNonOrderedLocationGroupVersionedReference
    ) = field(
        default=None,
        metadata={
            "name": "predefinedNonOrderedLocationGroupReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    non_ordered_location_group_by_reference_extension: None | ExtensionType = (
        field(
            default=None,
            metadata={
                "name": "nonOrderedLocationGroupByReferenceExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
