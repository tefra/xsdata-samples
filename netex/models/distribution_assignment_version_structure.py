from dataclasses import dataclass, field
from typing import List
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

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EntitlementProductRef",
                    "type": EntitlementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceAccessRightRef",
                    "type": ServiceAccessRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageRef",
                    "type": SalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSalesOfferPackagesRef",
                    "type": GroupOfSalesOfferPackagesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionRights",
                    "type": List[DistributionRightsEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "AllCountriesRef",
                    "type": AllCountriesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CountryRef",
                    "type": CountryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllowedInCountry",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TopographicPlaceRef",
                    "type": TopographicPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllDistributionChannelsRef",
                    "type": AllDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistributionChannelsRef",
                    "type": GroupOfDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionChannelRef",
                    "type": DistributionChannelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionChannelType",
                    "type": DistributionChannelTypeEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllowedInChannel",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RestrictedToChannel",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MandatoryProduct",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InitialCarrier",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransitCarrier",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FinalCarrier",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllAuthoritiesRef",
                    "type": AllAuthoritiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllOperatorsRef",
                    "type": AllOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllTransportOrganisationsRef",
                    "type": AllTransportOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllOrganisationsRef",
                    "type": AllOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
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
                    "name": "TransportOrganisationRef",
                    "type": TransportOrganisationRef,
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
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResponsibilitySetRef",
                    "type": ResponsibilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingServiceFacilityList",
                    "type": List[TicketingServiceFacilityEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "PaymentMethods",
                    "type": List[PaymentMethodEnumeration],
                    "namespace": "http://www.netex.org.uk/netex",
                    "default_factory": list,
                    "tokens": True,
                },
                {
                    "name": "RequiresRegistration",
                    "type": bool,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodRef",
                    "type": FulfilmentMethodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "noticeAssignments",
                    "type": NoticeAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 152,
        }
    )
