from dataclasses import dataclass, field
from typing import List, Optional
from .all_authorities_ref import AllAuthoritiesRef
from .all_countries_ref import AllCountriesRef
from .all_distribution_channels_ref import AllDistributionChannelsRef
from .all_operators_ref import AllOperatorsRef
from .all_organisations_ref import AllOrganisationsRef
from .all_transport_organisations_ref import AllTransportOrganisationsRef
from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .assignment_version_structure_2 import AssignmentVersionStructure2
from .authority_ref import AuthorityRef
from .capped_discount_right_ref import CappedDiscountRightRef
from .country_ref import CountryRef
from .distribution_channel_ref import DistributionChannelRef
from .distribution_channel_type_enumeration import DistributionChannelTypeEnumeration
from .distribution_rights_enumeration import DistributionRightsEnumeration
from .entitlement_product_ref import EntitlementProductRef
from .fare_product_ref import FareProductRef
from .fulfilment_method_ref import FulfilmentMethodRef
from .general_organisation_ref import GeneralOrganisationRef
from .group_of_distribution_channels_ref import GroupOfDistributionChannelsRef
from .group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from .management_agent_ref import ManagementAgentRef
from .notice_assignments_rel_structure import NoticeAssignmentsRelStructure
from .operator_ref import OperatorRef
from .organisation_ref import OrganisationRef
from .other_organisation_ref import OtherOrganisationRef
from .payment_method_enumeration import PaymentMethodEnumeration
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .responsibility_set_ref import ResponsibilitySetRef
from .retail_consortium_ref import RetailConsortiumRef
from .sale_discount_right_ref import SaleDiscountRightRef
from .sales_offer_package_ref import SalesOfferPackageRef
from .service_access_right_ref import ServiceAccessRightRef
from .serviced_organisation_ref import ServicedOrganisationRef
from .supplement_product_ref import SupplementProductRef
from .third_party_product_ref import ThirdPartyProductRef
from .ticketing_service_facility_enumeration import TicketingServiceFacilityEnumeration
from .topographic_place_ref import TopographicPlaceRef
from .transport_organisation_ref import TransportOrganisationRef
from .travel_agent_ref import TravelAgentRef
from .usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class DistributionAssignmentVersionStructure(AssignmentVersionStructure2):
    class Meta:
        name = "DistributionAssignment_VersionStructure"

    entitlement_product_ref: Optional[EntitlementProductRef] = field(
        default=None,
        metadata={
            "name": "EntitlementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    supplement_product_ref: Optional[SupplementProductRef] = field(
        default=None,
        metadata={
            "name": "SupplementProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    preassigned_fare_product_ref: Optional[PreassignedFareProductRef] = field(
        default=None,
        metadata={
            "name": "PreassignedFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    amount_of_price_unit_product_ref: Optional[AmountOfPriceUnitProductRef] = field(
        default=None,
        metadata={
            "name": "AmountOfPriceUnitProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_discount_right_ref: Optional[UsageDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "UsageDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    third_party_product_ref: Optional[ThirdPartyProductRef] = field(
        default=None,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capped_discount_right_ref: Optional[CappedDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "CappedDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sale_discount_right_ref: Optional[SaleDiscountRightRef] = field(
        default=None,
        metadata={
            "name": "SaleDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_product_ref: Optional[FareProductRef] = field(
        default=None,
        metadata={
            "name": "FareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    all_authorities_ref: Optional[AllAuthoritiesRef] = field(
        default=None,
        metadata={
            "name": "AllAuthoritiesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_operators_ref: Optional[AllOperatorsRef] = field(
        default=None,
        metadata={
            "name": "AllOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_transport_organisations_ref: Optional[AllTransportOrganisationsRef] = field(
        default=None,
        metadata={
            "name": "AllTransportOrganisationsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    transport_organisation_ref: Optional[TransportOrganisationRef] = field(
        default=None,
        metadata={
            "name": "TransportOrganisationRef",
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
