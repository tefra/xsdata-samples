from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.alternative_names_rel_structure import AlternativeNamesRelStructure
from netex.models.authority_ref import AuthorityRef
from netex.models.contact_structure import ContactStructure
from netex.models.distribution_channel_type_enumeration import DistributionChannelTypeEnumeration
from netex.models.distribution_rights_enumeration import DistributionRightsEnumeration
from netex.models.general_group_of_entities_ref_structure import GeneralGroupOfEntitiesRefStructure
from netex.models.general_organisation_ref import GeneralOrganisationRef
from netex.models.management_agent_ref import ManagementAgentRef
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_ref import OrganisationRef
from netex.models.other_organisation_ref import OtherOrganisationRef
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.point_refs_rel_structure import PointRefsRelStructure
from netex.models.retail_consortium_ref import RetailConsortiumRef
from netex.models.serviced_organisation_ref import ServicedOrganisationRef
from netex.models.transport_organisation_ref import TransportOrganisationRef
from netex.models.travel_agent_ref import TravelAgentRef
from netex.models.type_of_payment_method_refs_rel_structure import TypeOfPaymentMethodRefsRelStructure
from netex.models.type_of_value_version_structure import TypeOfValueVersionStructure

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
    distribution_points: Optional[PointRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "distributionPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_group_ref: Optional[GeneralGroupOfEntitiesRefStructure] = field(
        default=None,
        metadata={
            "name": "DistributionGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
