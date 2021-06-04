from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.all_authorities_ref import AllAuthoritiesRef
from netex.models.all_countries_ref import AllCountriesRef
from netex.models.all_distribution_channels_ref import AllDistributionChannelsRef
from netex.models.all_operators_ref import AllOperatorsRef
from netex.models.all_organisations_ref import AllOrganisationsRef
from netex.models.all_transport_organisations_ref import AllTransportOrganisationsRef
from netex.models.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.models.assignment_version_structure_1 import AssignmentVersionStructure1
from netex.models.authority_ref import AuthorityRef
from netex.models.capped_discount_right_ref import CappedDiscountRightRef
from netex.models.country_ref import CountryRef
from netex.models.distribution_channel_ref import DistributionChannelRef
from netex.models.distribution_channel_type_enumeration import DistributionChannelTypeEnumeration
from netex.models.distribution_rights_enumeration import DistributionRightsEnumeration
from netex.models.entitlement_product_ref import EntitlementProductRef
from netex.models.fare_product_ref import FareProductRef
from netex.models.fulfilment_method_ref import FulfilmentMethodRef
from netex.models.general_organisation_ref import GeneralOrganisationRef
from netex.models.group_of_distribution_channels_ref import GroupOfDistributionChannelsRef
from netex.models.group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from netex.models.management_agent_ref import ManagementAgentRef
from netex.models.notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from netex.models.operator_ref import OperatorRef
from netex.models.organisation_ref import OrganisationRef
from netex.models.other_organisation_ref import OtherOrganisationRef
from netex.models.payment_method_enumeration import PaymentMethodEnumeration
from netex.models.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.models.responsibility_set_ref import ResponsibilitySetRef
from netex.models.retail_consortium_ref import RetailConsortiumRef
from netex.models.sale_discount_right_ref import SaleDiscountRightRef
from netex.models.sales_offer_package_ref import SalesOfferPackageRef
from netex.models.service_access_right_ref import ServiceAccessRightRef
from netex.models.serviced_organisation_ref import ServicedOrganisationRef
from netex.models.supplement_product_ref import SupplementProductRef
from netex.models.third_party_product_ref import ThirdPartyProductRef
from netex.models.ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from netex.models.topographic_place_ref import TopographicPlaceRef
from netex.models.transport_organisation_ref import TransportOrganisationRef
from netex.models.travel_agent_ref import TravelAgentRef
from netex.models.usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistributionAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "DistributionAssignment_VersionStructure"

    entitlement_product_ref: List[EntitlementProductRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    supplement_product_ref: List[SupplementProductRef] = field(
        default_factory=list,
        metadata={
            "name": "SupplementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    preassigned_fare_product_ref: List[PreassignedFareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "PreassignedFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    amount_of_price_unit_product_ref: List[AmountOfPriceUnitProductRef] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfPriceUnitProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    usage_discount_right_ref: List[UsageDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    third_party_product_ref: List[ThirdPartyProductRef] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    capped_discount_right_ref: List[CappedDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    sale_discount_right_ref: List[SaleDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "SaleDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 6,
            "sequential": True,
        }
    )
    fare_product_ref: List[FareProductRef] = field(
        default_factory=list,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_access_right_ref: Optional[ServiceAccessRightRef] = field(
        default=None,
        metadata={
            "name": "ServiceAccessRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_sales_offer_packages_ref: Optional[GroupOfSalesOfferPackagesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
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
    all_countries_ref: Optional[AllCountriesRef] = field(
        default=None,
        metadata={
            "name": "AllCountriesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    country_ref: Optional[CountryRef] = field(
        default=None,
        metadata={
            "name": "CountryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    allowed_in_country: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowedInCountry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_distribution_channels_ref: Optional[AllDistributionChannelsRef] = field(
        default=None,
        metadata={
            "name": "AllDistributionChannelsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_distribution_channels_ref: Optional[GroupOfDistributionChannelsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfDistributionChannelsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_channel_ref: Optional[DistributionChannelRef] = field(
        default=None,
        metadata={
            "name": "DistributionChannelRef",
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
    allowed_in_channel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowedInChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    restricted_to_channel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RestrictedToChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    mandatory_product: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MandatoryProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    initial_carrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InitialCarrier",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transit_carrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TransitCarrier",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    final_carrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FinalCarrier",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_authorities_ref: List[AllAuthoritiesRef] = field(
        default_factory=list,
        metadata={
            "name": "AllAuthoritiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    all_operators_ref: List[AllOperatorsRef] = field(
        default_factory=list,
        metadata={
            "name": "AllOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    all_transport_organisations_ref: List[AllTransportOrganisationsRef] = field(
        default_factory=list,
        metadata={
            "name": "AllTransportOrganisationsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    all_organisations_ref: Optional[AllOrganisationsRef] = field(
        default=None,
        metadata={
            "name": "AllOrganisationsRef",
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
            "max_occurs": 4,
            "sequential": True,
        }
    )
    authority_ref: List[AuthorityRef] = field(
        default_factory=list,
        metadata={
            "name": "AuthorityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    operator_ref: List[OperatorRef] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    transport_organisation_ref: List[TransportOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "TransportOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    general_organisation_ref: List[GeneralOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    management_agent_ref: List[ManagementAgentRef] = field(
        default_factory=list,
        metadata={
            "name": "ManagementAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    serviced_organisation_ref: List[ServicedOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "ServicedOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    travel_agent_ref: List[TravelAgentRef] = field(
        default_factory=list,
        metadata={
            "name": "TravelAgentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 10,
            "sequential": True,
        }
    )
    other_organisation_ref: List[OtherOrganisationRef] = field(
        default_factory=list,
        metadata={
            "name": "OtherOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
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
    responsibility_set_ref: Optional[ResponsibilitySetRef] = field(
        default=None,
        metadata={
            "name": "ResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    ticketing_service_facility_list: List[TicketingServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "TicketingServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
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
    requires_registration: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresRegistration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fulfilment_method_ref: Optional[FulfilmentMethodRef] = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
