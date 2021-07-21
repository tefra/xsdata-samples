from dataclasses import dataclass, field
from typing import List
from .authority import Authority
from .containment_aggregation_structure import ContainmentAggregationStructure
from .general_organisation import GeneralOrganisation
from .management_agent import ManagementAgent
from .operator import Operator
from .organisation_1 import Organisation1
from .organisation_2 import Organisation2
from .other_organisation import OtherOrganisation
from .retail_consortium import RetailConsortium
from .serviced_organisation import ServicedOrganisation
from .transport_organisation import TransportOrganisation
from .travel_agent import TravelAgent

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
        }
    )
    authority: List[Authority] = field(
        default_factory=list,
        metadata={
            "name": "Authority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator: List[Operator] = field(
        default_factory=list,
        metadata={
            "name": "Operator",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_organisation: List[TransportOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "TransportOrganisation_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    serviced_organisation: List[ServicedOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "ServicedOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_organisation: List[GeneralOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "GeneralOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    management_agent: List[ManagementAgent] = field(
        default_factory=list,
        metadata={
            "name": "ManagementAgent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    travel_agent: List[TravelAgent] = field(
        default_factory=list,
        metadata={
            "name": "TravelAgent",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    other_organisation: List[OtherOrganisation] = field(
        default_factory=list,
        metadata={
            "name": "OtherOrganisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    organisation: List[Organisation1] = field(
        default_factory=list,
        metadata={
            "name": "Organisation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_organisation: List[Organisation2] = field(
        default_factory=list,
        metadata={
            "name": "Organisation_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
