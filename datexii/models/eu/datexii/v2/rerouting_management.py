from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.itinerary import Itinerary
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.network_management import NetworkManagement
from datexii.models.eu.datexii.v2.rerouting_management_type_enum import (
    ReroutingManagementTypeEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class ReroutingManagement(NetworkManagement):
    """
    Rerouting management action that is issued by the network/road operator.

    :ivar rerouting_management_type: Type of rerouting management action
        instigated by operator.
    :ivar rerouting_itinerary_description: A description of the
        rerouting itinerary.
    :ivar signed_rerouting: Indication of whether the rerouting is
        signed.
    :ivar entry: The specified entry on to another road at which the
        alternative route commences.
    :ivar exit: The specified exit from the normal route/road at which
        the alternative route commences.
    :ivar road_or_junction_number: The intersecting road or the junction
        at which the alternative route commences.
    :ivar alternative_route: The definition of the alternative route
        (rerouting) specified as an ordered set of locations (itinerary)
        which may be specific to one or more defined destinations.
    :ivar rerouting_management_extension:
    """

    rerouting_management_type: list[ReroutingManagementTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "reroutingManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "min_occurs": 1,
        },
    )
    rerouting_itinerary_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reroutingItineraryDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    signed_rerouting: Optional[bool] = field(
        default=None,
        metadata={
            "name": "signedRerouting",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    entry: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    exit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    road_or_junction_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "roadOrJunctionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    alternative_route: list[Itinerary] = field(
        default_factory=list,
        metadata={
            "name": "alternativeRoute",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    rerouting_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "reroutingManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
