from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.administrative_zone_version_structure import AdministrativeZonesRelStructure
from netex.models.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.models.authority_ref import AuthorityRef
from netex.models.contact_structure import ContactStructure
from netex.models.general_organisation_ref import GeneralOrganisationRef
from netex.models.location_structure_2 import LocationStructure2
from netex.models.management_agent_ref import ManagementAgentRef
from netex.models.multilingual_string import MultilingualString
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_ref import OrganisationRef
from netex.models.organisation_refs_rel_structure import OrganisationRefsRelStructure
from netex.models.other_organisation_ref import OtherOrganisationRef
from netex.models.private_code import PrivateCode
from netex.models.private_code_structure import PrivateCodeStructure
from netex.models.responsibility_sets_rel_structure import ResponsibilitySetsRelStructure
from netex.models.retail_consortium_ref import RetailConsortiumRef
from netex.models.serviced_organisation_ref import ServicedOrganisationRef
from netex.models.transport_organisation_ref import TransportOrganisationRef
from netex.models.travel_agent_ref import TravelAgentRef
from netex.models.type_of_organisation_part_ref import TypeOfOrganisationPartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationPartVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "OrganisationPart_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    location: Optional[LocationStructure2] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    retail_consortium_ref: List[RetailConsortiumRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailConsortiumRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    authority_ref: List[AuthorityRef] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    operator_ref: List[OperatorRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    transport_organisation_ref: List[TransportOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "TransportOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    general_organisation_ref: List[GeneralOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    management_agent_ref: List[ManagementAgentRef] = field(
        default_factory=list,
        metadata={
            "name": "ManagementAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    serviced_organisation_ref: List[ServicedOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "ServicedOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    travel_agent_ref: List[TravelAgentRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    other_organisation_ref: List[OtherOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "OtherOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
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
    type_of_organisation_part_ref: Optional[TypeOfOrganisationPartRef] = field(
        default=None,
        metadata={
            "name": "TypeOfOrganisationPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    administrative_zones: Optional[AdministrativeZonesRelStructure] = field(
        default=None,
        metadata={
            "name": "administrativeZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    own_responsibility_sets: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "name": "ownResponsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    delegated_responsibility_sets: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "name": "delegatedResponsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    delegated_from: Optional[OrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "delegatedFrom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
