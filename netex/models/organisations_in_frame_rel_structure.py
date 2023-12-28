from dataclasses import dataclass, field
from typing import List, Union
from .authority import Authority
from .containment_aggregation_structure import ContainmentAggregationStructure
from .general_organisation import GeneralOrganisation
from .management_agent import ManagementAgent
from .operator import Operator
from .other_organisation import OtherOrganisation
from .retail_consortium import RetailConsortium
from .serviced_organisation import ServicedOrganisation
from .travel_agent import TravelAgent

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OrganisationsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "organisationsInFrame_RelStructure"

    organisation_or_transport_organisation: List[
        Union[
            RetailConsortium,
            Authority,
            Operator,
            ServicedOrganisation,
            GeneralOrganisation,
            ManagementAgent,
            TravelAgent,
            OtherOrganisation,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortium",
                    "type": RetailConsortium,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Authority",
                    "type": Authority,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Operator",
                    "type": Operator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisation",
                    "type": ServicedOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisation",
                    "type": GeneralOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgent",
                    "type": ManagementAgent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgent",
                    "type": TravelAgent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisation",
                    "type": OtherOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
