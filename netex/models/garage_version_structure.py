from dataclasses import dataclass, field
from typing import List, Optional
from .addressable_place_version_structure import AddressablePlaceVersionStructure
from .authority_ref import AuthorityRef
from .contact_structure import ContactStructure
from .crew_base_refs_rel_structure import CrewBaseRefsRelStructure
from .garage_points_rel_structure import GaragePointsRelStructure
from .general_organisation_ref import GeneralOrganisationRef
from .management_agent_ref import ManagementAgentRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .transport_organisation_ref import TransportOrganisationRef
from .transport_organisation_refs_rel_structure import TransportOrganisationRefsRelStructure
from .travel_agent_ref import TravelAgentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GarageVersionStructure(AddressablePlaceVersionStructure):
    class Meta:
        name = "Garage_VersionStructure"

    contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
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
                    "name": "TransportOrganisationRef",
                    "type": TransportOrganisationRef,
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
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "operators",
                    "type": TransportOrganisationRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "garagePoints",
                    "type": GaragePointsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "crewBases",
                    "type": CrewBaseRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 24,
        }
    )
