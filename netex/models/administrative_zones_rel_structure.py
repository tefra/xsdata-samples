from dataclasses import dataclass, field
from typing import List, Optional, Type, Union
from .administrative_zone_ref import AdministrativeZoneRef
from .all_modes_enumeration import AllModesEnumeration
from .authority_ref import AuthorityRef
from .codespace_assignments_rel_structure import (
    CodespaceAssignmentsRelStructure,
)
from .containment_aggregation_structure import ContainmentAggregationStructure
from .general_organisation_ref import GeneralOrganisationRef
from .management_agent_ref import ManagementAgentRef
from .online_service_operator_ref import OnlineServiceOperatorRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .private_code_structure import PrivateCodeStructure
from .responsibility_sets_rel_structure import ResponsibilitySetsRelStructure
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .travel_agent_ref import TravelAgentRef
from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AdministrativeZonesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "administrativeZones_RelStructure"

    administrative_zone_ref_or_transport_administrative_zone_or_administrative_zone: List[
        Union[
            AdministrativeZoneRef,
            "TransportAdministrativeZone",
            "AdministrativeZone1",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AdministrativeZoneRef",
                    "type": AdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZone",
                    "type": Type["TransportAdministrativeZone"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZone",
                    "type": Type["AdministrativeZone1"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass
class AdministrativeZoneVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "AdministrativeZone_VersionStructure"

    public_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    organisation_ref_or_other_organisation_ref_or_transport_organisation_ref: Optional[
        Union[
            RetailConsortiumRef,
            OnlineServiceOperatorRef,
            GeneralOrganisationRef,
            ManagementAgentRef,
            ServicedOrganisationRef,
            TravelAgentRef,
            OtherOrganisationRef,
            AuthorityRef,
            OperatorRef,
            OrganisationRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OnlineServiceOperatorRef",
                    "type": OnlineServiceOperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisationRef",
                    "type": GeneralOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgentRef",
                    "type": ManagementAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisationRef",
                    "type": ServicedOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgentRef",
                    "type": TravelAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisationRef",
                    "type": OtherOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    responsibilities: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    codespace_assignments: Optional[CodespaceAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "codespaceAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    subzones: Optional[AdministrativeZonesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class AdministrativeZone1(AdministrativeZoneVersionStructure):
    class Meta:
        name = "AdministrativeZone"
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class TransportAdministrativeZoneVersionStructure(
    AdministrativeZoneVersionStructure
):
    class Meta:
        name = "TransportAdministrativeZone_VersionStructure"

    vehicle_modes: List[AllModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )


@dataclass
class TransportAdministrativeZone(TransportAdministrativeZoneVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
