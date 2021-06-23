from dataclasses import dataclass, field
from typing import List, Optional
from .administrative_zone_2 import AdministrativeZone2
from .administrative_zone_ref import AdministrativeZoneRef
from .all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from .authority_ref import AuthorityRef
from .codespace_assignments_rel_structure import CodespaceAssignmentsRelStructure
from .containment_aggregation_structure import ContainmentAggregationStructure
from .general_organisation_ref import GeneralOrganisationRef
from .management_agent_ref import ManagementAgentRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .private_code_structure import PrivateCodeStructure
from .responsibility_sets_rel_structure import ResponsibilitySetsRelStructure
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .transport_organisation_ref import TransportOrganisationRef
from .travel_agent_ref import TravelAgentRef
from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


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
        }
    )
    retail_consortium_ref: Optional[RetailConsortiumRef] = field(
        default=None,
        metadata={
            "name": "RetailConsortiumRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_ref: Optional[AuthorityRef] = field(
        default=None,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_organisation_ref: Optional[TransportOrganisationRef] = field(
        default=None,
        metadata={
            "name": "TransportOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_organisation_ref: Optional[GeneralOrganisationRef] = field(
        default=None,
        metadata={
            "name": "GeneralOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    management_agent_ref: Optional[ManagementAgentRef] = field(
        default=None,
        metadata={
            "name": "ManagementAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    serviced_organisation_ref: Optional[ServicedOrganisationRef] = field(
        default=None,
        metadata={
            "name": "ServicedOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_agent_ref: Optional[TravelAgentRef] = field(
        default=None,
        metadata={
            "name": "TravelAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    other_organisation_ref: Optional[OtherOrganisationRef] = field(
        default=None,
        metadata={
            "name": "OtherOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation_ref: Optional[OrganisationRef] = field(
        default=None,
        metadata={
            "name": "OrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibilities: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    codespace_assignments: Optional[CodespaceAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "codespaceAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    subzones: Optional["AdministrativeZonesRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class AdministrativeZone1(AdministrativeZoneVersionStructure):
    class Meta:
        name = "AdministrativeZone"
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class TransportAdministrativeZoneVersionStructure(AdministrativeZoneVersionStructure):
    class Meta:
        name = "TransportAdministrativeZone_VersionStructure"

    vehicle_modes: List[AllVehicleModesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )


@dataclass
class TransportAdministrativeZone(TransportAdministrativeZoneVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class AdministrativeZonesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "administrativeZones_RelStructure"

    choice: List[object] = field(
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
                    "type": TransportAdministrativeZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZone",
                    "type": AdministrativeZone1,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZone_",
                    "type": AdministrativeZone2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
