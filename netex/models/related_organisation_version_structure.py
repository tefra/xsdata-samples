from dataclasses import dataclass, field
from typing import Optional, Union

from .authority_ref import AuthorityRef
from .entity_in_version_structure import VersionedChildStructure
from .general_organisation_ref import GeneralOrganisationRef
from .management_agent_ref import ManagementAgentRef
from .multilingual_string import MultilingualString
from .online_service_operator_ref import OnlineServiceOperatorRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .organisation_role_enumeration import OrganisationRoleEnumeration
from .other_organisation_ref import OtherOrganisationRef
from .responsibility_role_ref import ResponsibilityRoleRef
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .travel_agent_ref import TravelAgentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class RelatedOrganisationVersionStructure(VersionedChildStructure):
    class Meta:
        name = "RelatedOrganisation_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    organisation_ref_or_other_organisation_ref_or_transport_organisation_ref: RetailConsortiumRef | OnlineServiceOperatorRef | GeneralOrganisationRef | ManagementAgentRef | ServicedOrganisationRef | TravelAgentRef | OtherOrganisationRef | AuthorityRef | OperatorRef | OrganisationRef | None = field(
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
    organisation_role_type: OrganisationRoleEnumeration | None = field(
        default=None,
        metadata={
            "name": "OrganisationRoleType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    responsibility_role_ref: ResponsibilityRoleRef | None = field(
        default=None,
        metadata={
            "name": "ResponsibilityRoleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
