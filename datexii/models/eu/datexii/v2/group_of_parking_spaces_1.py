from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.dimension import Dimension
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.group_of_locations import GroupOfLocations
from datexii.models.eu.datexii.v2.group_of_parking_spaces_parking_space_index_parking_space import (
    GroupOfParkingSpacesParkingSpaceIndexParkingSpace,
)
from datexii.models.eu.datexii.v2.parking_space_basics import (
    ParkingSpaceBasics,
)
from datexii.models.eu.datexii.v2.parking_type_of_group import (
    ParkingTypeOfGroup,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class GroupOfParkingSpaces1(ParkingSpaceBasics):
    """
    A group of parking spaces.

    All information provided has to be identical for all places in this
    group. Can also be used just to give the number of lorry parkings, for
    example. 'GroupOfParkingSpaces' may be multiple defined or include each
    other.

    :ivar parking_number_of_spaces: Number of parking spaces (attribute
        is used for a parking record as well as for a group of parking
        spaces).
    :ivar parking_type_of_group: Defines the type of this group
        specification.
    :ivar identical_to_group: Points to another instance of
        'GroupOfParkingSpaces', which is identical from a local point of
        view. To be used when defining mixed parking areas with
        different time slots.
    :ivar real_subset_of_group: Points to another instance of
        'GroupOfParkingSpaces', which is a real superset from a local
        point of view. To be used when defining mixed parking areas with
        different time slots.
    :ivar minimum_parking_space_dimension: Lower dimension boundaries
        for all spaces within the group. Note that there must not exist
        a space with this dimension, but each space's dimension values
        must be equal or higher.
    :ivar dimension_of_group: Dimension of a virtual rectangle
        encapsulating the group of parking spaces. Use
        'dimensionUsableArea' to define the total space available for
        parking within this group. Do not use 'dimensionHeight'.
    :ivar maximum_parking_space_dimension: Dimension of the largest
        space within this group (i.e. there must be at least one space
        of this dimension). If the comparison of dimension values is not
        unique, the length is decisive.
    :ivar parking_space:
    :ivar group_of_locations:
    :ivar group_of_parking_spaces_extension:
    """

    class Meta:
        name = "GroupOfParkingSpaces"

    parking_number_of_spaces: int = field(
        metadata={
            "name": "parkingNumberOfSpaces",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    parking_type_of_group: ParkingTypeOfGroup = field(
        metadata={
            "name": "parkingTypeOfGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    identical_to_group: list[str] = field(
        default_factory=list,
        metadata={
            "name": "identicalToGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    real_subset_of_group: list[str] = field(
        default_factory=list,
        metadata={
            "name": "realSubsetOfGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    minimum_parking_space_dimension: None | Dimension = field(
        default=None,
        metadata={
            "name": "minimumParkingSpaceDimension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dimension_of_group: None | Dimension = field(
        default=None,
        metadata={
            "name": "dimensionOfGroup",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    maximum_parking_space_dimension: None | Dimension = field(
        default=None,
        metadata={
            "name": "maximumParkingSpaceDimension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    parking_space: list[GroupOfParkingSpacesParkingSpaceIndexParkingSpace] = (
        field(
            default_factory=list,
            metadata={
                "name": "parkingSpace",
                "type": "Element",
                "namespace": "http://datex2.eu/schema/2/2_0",
            },
        )
    )
    group_of_locations: None | GroupOfLocations = field(
        default=None,
        metadata={
            "name": "groupOfLocations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    group_of_parking_spaces_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "groupOfParkingSpacesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
