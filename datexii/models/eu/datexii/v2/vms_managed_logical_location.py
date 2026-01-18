from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.location import Location
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsManagedLogicalLocation:
    """
    The logical location (e.g. a car park, a section of road, a junction
    etc.) which a VMS contributes to the management of.

    :ivar managed_logical_location: Identification of the logical
        location (e.g. a car park, a section of road , a junction etc.)
        which this sign contributes to the management of.
    :ivar distance_from_logical_location: Distance in metres of the VMS
        from the logical location which this sign contributes to the
        management of.
    :ivar managed_location: The location which is managed by the
        variable message sign, such as the location of a junction or a
        car park.
    :ivar vms_managed_logical_location_extension:
    """

    managed_logical_location: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "managedLogicalLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    distance_from_logical_location: None | int = field(
        default=None,
        metadata={
            "name": "distanceFromLogicalLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    managed_location: None | Location = field(
        default=None,
        metadata={
            "name": "managedLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    vms_managed_logical_location_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "vmsManagedLogicalLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
