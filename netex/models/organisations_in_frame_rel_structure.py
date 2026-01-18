from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from .authority import Authority
from .containment_aggregation_structure import ContainmentAggregationStructure
from .general_organisation import GeneralOrganisation
from .management_agent import ManagementAgent
from .online_service_operator import OnlineServiceOperator
from .operator import Operator
from .other_organisation import OtherOrganisation
from .retail_consortium import RetailConsortium
from .serviced_organisation import ServicedOrganisation
from .travel_agent import TravelAgent

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationsInFrameRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "organisationsInFrame_RelStructure"

    organisation_or_transport_organisation: Iterable[
        RetailConsortium
        | ServicedOrganisation
        | GeneralOrganisation
        | ManagementAgent
        | TravelAgent
        | OtherOrganisation
        | OnlineServiceOperator
        | Authority
        | Operator
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
                {
                    "name": "OnlineServiceOperator",
                    "type": OnlineServiceOperator,
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
            ),
        },
    )
