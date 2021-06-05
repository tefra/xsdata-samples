from dataclasses import dataclass, field
from typing import List
from netex.models.authority import Authority
from netex.models.containment_aggregation_structure import ContainmentAggregationStructure
from netex.models.general_organisation import GeneralOrganisation
from netex.models.management_agent import ManagementAgent
from netex.models.operator import Operator
from netex.models.organisation_1 import Organisation1
from netex.models.organisation_2 import Organisation2
from netex.models.other_organisation import OtherOrganisation
from netex.models.retail_consortium import RetailConsortium
from netex.models.serviced_organisation import ServicedOrganisation
from netex.models.transport_organisation import TransportOrganisation
from netex.models.travel_agent import TravelAgent

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "organisationsInFrame_RelStructure"

    retail_consortium: List[RetailConsortium] = field(
        default_factory=list,
        metadata={
            "name": "RetailConsortium",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    authority: List[Authority] = field(
        default_factory=list,
        metadata={
            "name": "Authority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    operator: List[Operator] = field(
        default_factory=list,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    transport_organisation: List[TransportOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "TransportOrganisation_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    serviced_organisation: List[ServicedOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "ServicedOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    general_organisation: List[GeneralOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "GeneralOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    management_agent: List[ManagementAgent] = field(
        default_factory=list,
        metadata={
            "name": "ManagementAgent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    travel_agent: List[TravelAgent] = field(
        default_factory=list,
        metadata={
            "name": "TravelAgent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    other_organisation: List[OtherOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "OtherOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    organisation: List[Organisation1] = field(
        default_factory=list,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
    netex_org_uk_netex_organisation: List[Organisation2] = field(
        default_factory=list,
        metadata={
            "name": "Organisation_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
