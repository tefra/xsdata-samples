from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.predefined_location import PredefinedLocation
from datexii.models.eu.datexii.v2.predefined_location_container import (
    PredefinedLocationContainer,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class PredefinedNonOrderedLocationGroup(PredefinedLocationContainer):
    """
    An identifiable versioned instance of a predefined group of non ordered
    locations (i.e. more than one).

    :ivar predefined_non_ordered_location_group_name: A name assigned to
        the predefined group of non ordered locations.
    :ivar predefined_location:
    :ivar predefined_non_ordered_location_group_extension:
    :ivar id:
    :ivar version:
    """

    predefined_non_ordered_location_group_name: MultilingualString | None = (
        field(
            default=None,
            metadata={
                "name": "predefinedNonOrderedLocationGroupName",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    predefined_location: list[PredefinedLocation] = field(
        default_factory=list,
        metadata={
            "name": "predefinedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 2,
        },
    )
    predefined_non_ordered_location_group_extension: ExtensionType | None = (
        field(
            default=None,
            metadata={
                "name": "predefinedNonOrderedLocationGroupExtension",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    version: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
