from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.general_network_management_type_enum import (
    GeneralNetworkManagementTypeEnum,
)
from datexii.models.eu.datexii.v2.network_management import NetworkManagement
from datexii.models.eu.datexii.v2.person_category_enum import (
    PersonCategoryEnum,
)

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class GeneralNetworkManagement(NetworkManagement):
    """
    Network management action that is instigated either manually or
    automatically by the network/road operator.

    Compliance with any resulting control may be advisory or mandatory.

    :ivar general_network_management_type: The type of traffic
        management action instigated by the network/road operator.
    :ivar traffic_manually_directed_by: Type of person that is manually
        directing traffic (applicable if generalNetworkManagementType is
        set to "trafficBeingManuallyDirected").
    :ivar general_network_management_extension:
    """

    general_network_management_type: GeneralNetworkManagementTypeEnum = field(
        metadata={
            "name": "generalNetworkManagementType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    traffic_manually_directed_by: None | PersonCategoryEnum = field(
        default=None,
        metadata={
            "name": "trafficManuallyDirectedBy",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    general_network_management_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "generalNetworkManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
