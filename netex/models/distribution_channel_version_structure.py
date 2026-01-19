from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .authority_ref import AuthorityRef
from .contact_structure import ContactStructure
from .distribution_channel_type_enumeration import (
    DistributionChannelTypeEnumeration,
)
from .distribution_rights_enumeration import DistributionRightsEnumeration
from .general_group_of_entities_ref_structure import (
    GeneralGroupOfEntitiesRefStructure,
)
from .general_organisation_ref import GeneralOrganisationRef
from .management_agent_ref import ManagementAgentRef
from .online_service_operator_ref import OnlineServiceOperatorRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .payment_method_enumeration import PaymentMethodEnumeration
from .point_refs_rel_structure import PointRefsRelStructure
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .travel_agent_ref import TravelAgentRef
from .type_of_payment_method_refs_rel_structure import (
    TypeOfPaymentMethodRefsRelStructure,
)
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistributionChannelVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "DistributionChannel_VersionStructure"

    alternative_names: None | AlternativeNamesRelStructure = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_channel_type: None | DistributionChannelTypeEnumeration = (
        field(
            default=None,
            metadata={
                "name": "DistributionChannelType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    is_obligatory: None | bool = field(
        default=None,
        metadata={
            "name": "IsObligatory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    requires_email_address: None | bool = field(
        default=None,
        metadata={
            "name": "RequiresEmailAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contact_details: None | ContactStructure = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    organisation_ref_or_other_organisation_ref_or_transport_organisation_ref: (
        None
        | RetailConsortiumRef
        | OnlineServiceOperatorRef
        | GeneralOrganisationRef
        | ManagementAgentRef
        | ServicedOrganisationRef
        | TravelAgentRef
        | OtherOrganisationRef
        | AuthorityRef
        | OperatorRef
        | OrganisationRef
    ) = field(
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
    payment_methods: Sequence[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_payment_method: None | TypeOfPaymentMethodRefsRelStructure = (
        field(
            default=None,
            metadata={
                "name": "typesOfPaymentMethod",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    distribution_rights: Sequence[DistributionRightsEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DistributionRights",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    distribution_points_or_distribution_group_ref: (
        None | PointRefsRelStructure | GeneralGroupOfEntitiesRefStructure
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "distributionPoints",
                    "type": PointRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionGroupRef",
                    "type": GeneralGroupOfEntitiesRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
