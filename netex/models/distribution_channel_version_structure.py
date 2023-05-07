from dataclasses import dataclass, field
from typing import List, Optional
from .alternative_names_rel_structure import AlternativeNamesRelStructure
from .authority_ref import AuthorityRef
from .contact_structure import ContactStructure
from .distribution_channel_type_enumeration import DistributionChannelTypeEnumeration
from .distribution_rights_enumeration import DistributionRightsEnumeration
from .general_group_of_entities_ref_structure import GeneralGroupOfEntitiesRefStructure
from .general_organisation_ref import GeneralOrganisationRef
from .management_agent_ref import ManagementAgentRef
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .payment_method_enumeration import PaymentMethodEnumeration
from .point_refs_rel_structure import PointRefsRelStructure
from .retail_consortium_ref import RetailConsortiumRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .travel_agent_ref import TravelAgentRef
from .type_of_payment_method_refs_rel_structure import TypeOfPaymentMethodRefsRelStructure
from .type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistributionChannelVersionStructure(TypeOfValueVersionStructure):
    class Meta:
        name = "DistributionChannel_VersionStructure"

    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_channel_type: Optional[DistributionChannelTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DistributionChannelType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_obligatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsObligatory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    requires_email_address: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresEmailAddress",
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
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    types_of_payment_method: Optional[TypeOfPaymentMethodRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_rights: List[DistributionRightsEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DistributionRights",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    distribution_points_or_distribution_group_ref: Optional[object] = field(
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
        }
    )
