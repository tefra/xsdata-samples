from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.compliance_option_enum import (
    ComplianceOptionEnum,
)
from datexii.models.eu.datexii.v2.direction_enum import DirectionEnum
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.operator_action import OperatorAction
from datexii.models.eu.datexii.v2.places_enum import PlacesEnum
from datexii.models.eu.datexii.v2.traffic_type_enum import TrafficTypeEnum
from datexii.models.eu.datexii.v2.vehicle_characteristics import (
    VehicleCharacteristics,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class NetworkManagement(OperatorAction):
    """
    Network management action which is applicable to the road network and
    its users.

    :ivar compliance_option: Defines whether the network management
        instruction or the control resulting from a network management
        action is advisory or mandatory.
    :ivar applicable_for_traffic_direction: The ultimate traffic
        direction to which the network management is applicable.
    :ivar applicable_for_traffic_type: The type of traffic to which the
        network management is applicable.
    :ivar places_at_which_applicable: Places, in generic terms, at which
        the network management applies.
    :ivar automatically_initiated: Defines whether the network
        management is initiated by an automatic system.
    :ivar for_vehicles_with_characteristics_of: The characteristics of
        those vehicles for which the network management is applicable.
    :ivar network_management_extension:
    """

    compliance_option: ComplianceOptionEnum = field(
        metadata={
            "name": "complianceOption",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    applicable_for_traffic_direction: list[DirectionEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    applicable_for_traffic_type: list[TrafficTypeEnum] = field(
        default_factory=list,
        metadata={
            "name": "applicableForTrafficType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    places_at_which_applicable: list[PlacesEnum] = field(
        default_factory=list,
        metadata={
            "name": "placesAtWhichApplicable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    automatically_initiated: None | bool = field(
        default=None,
        metadata={
            "name": "automaticallyInitiated",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    for_vehicles_with_characteristics_of: list[VehicleCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "forVehiclesWithCharacteristicsOf",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    network_management_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "networkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
