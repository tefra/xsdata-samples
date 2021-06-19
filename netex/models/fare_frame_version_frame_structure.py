from dataclasses import dataclass, field
from typing import List, Optional
from .access_right_parameter_assignments_in_frame_rel_structure import AccessRightParameterAssignmentsInFrameRelStructure
from .authority_ref import AuthorityRef
from .border_points_in_frame_rel_structure import BorderPointsInFrameRelStructure
from .common_version_frame_structure import CommonVersionFrameStructure
from .controllable_elements_in_frame_rel_structure import ControllableElementsInFrameRelStructure
from .distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from .distribution_assignments_in_frame_rel_structure import DistributionAssignmentsInFrameRelStructure
from .distribution_channels_in_frame_rel_structure import DistributionChannelsInFrameRelStructure
from .fare_prices_in_frame_rel_structure import FarePricesInFrameRelStructure
from .fare_products_in_frame_rel_structure import FareProductsInFrameRelStructure
from .fare_scheduled_stop_points_in_frame_rel_structure import FareScheduledStopPointsInFrameRelStructure
from .fare_sections_in_frame_rel_structure import FareSectionsInFrameRelStructure
from .fare_series_in_frame_rel_structure import FareSeriesInFrameRelStructure
from .fare_structure_elements_in_frame_rel_structure import FareStructureElementsInFrameRelStructure
from .fare_tables_in_frame_rel_structure import FareTablesInFrameRelStructure
from .fare_zones_in_frame_rel_structure import FareZonesInFrameRelStructure
from .fulfilment_methods_in_frame_rel_structure import FulfilmentMethodsInFrameRelStructure
from .geographical_intervals_rel_structure import GeographicalIntervalsRelStructure
from .geographical_structure_factors_rel_structure import GeographicalStructureFactorsRelStructure
from .geographical_units_rel_structure import GeographicalUnitsRelStructure
from .groups_of_distance_matrix_elements_rel_structure import GroupsOfDistanceMatrixElementsRelStructure
from .groups_of_distribution_channels_in_frame_rel_structure import GroupsOfDistributionChannelsInFrameRelStructure
from .groups_of_sales_offer_packages_in_frame_rel_structure import GroupsOfSalesOfferPackagesInFrameRelStructure
from .notice_assignments_in_frame_rel_structure import NoticeAssignmentsInFrameRelStructure
from .notices_in_frame_rel_structure import NoticesInFrameRelStructure
from .operator_ref import OperatorRef
from .parking_tariffs_in_frame_rel_structure import ParkingTariffsInFrameRelStructure
from .pricing_parameter_set import PricingParameterSet
from .quality_structure_factors_rel_structure import QualityStructureFactorsRelStructure
from .sales_offer_package_elements_in_frame_rel_structure import SalesOfferPackageElementsInFrameRelStructure
from .sales_offer_package_substitutions_in_frame_rel_structure import SalesOfferPackageSubstitutionsInFrameRelStructure
from .sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from .tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from .time_intervals_rel_structure import TimeIntervalsRelStructure
from .time_structure_factors_rel_structure import TimeStructureFactorsRelStructure
from .time_units_rel_structure import TimeUnitsRelStructure
from .transport_organisation_ref import TransportOrganisationRef
from .types_of_travel_document_in_frame_rel_structure import TypesOfTravelDocumentInFrameRelStructure
from .usage_parameters_in_frame_rel_structure import UsageParametersInFrameRelStructure
from .validable_elements_in_frame_rel_structure import ValidableElementsInFrameRelStructure
from .vehicle_mode_enumeration import VehicleModeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareFrameVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "FareFrame_VersionFrameStructure"

    mode: Optional[VehicleModeEnumeration] = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "PricingParameterSet",
                    "type": PricingParameterSet,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "notices",
                    "type": NoticesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "noticeAssignments",
                    "type": NoticeAssignmentsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "borderPoints",
                    "type": BorderPointsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fareScheduledStopPoints",
                    "type": FareScheduledStopPointsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fareZones",
                    "type": FareZonesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fareSections",
                    "type": FareSectionsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "seriesConstraints",
                    "type": FareSeriesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "geographicalUnits",
                    "type": GeographicalUnitsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "geographicalIntervals",
                    "type": GeographicalIntervalsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "geographicalStructureFactors",
                    "type": GeographicalStructureFactorsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "timeUnits",
                    "type": TimeUnitsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "timeIntervals",
                    "type": TimeIntervalsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "timeStructureFactors",
                    "type": TimeStructureFactorsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "qualityStructureFactors",
                    "type": QualityStructureFactorsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "distanceMatrixElements",
                    "type": DistanceMatrixElementsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "groupsOfDistanceMatrixElements",
                    "type": GroupsOfDistanceMatrixElementsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fareStructureElements",
                    "type": FareStructureElementsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "tariffs",
                    "type": TariffsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "validableElements",
                    "type": ValidableElementsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "controllableElements",
                    "type": ControllableElementsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "usageParameters",
                    "type": UsageParametersInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "accessRightParameterAssignments",
                    "type": AccessRightParameterAssignmentsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fareProducts",
                    "type": FareProductsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "priceGroups",
                    "type": FarePricesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fareTables",
                    "type": FareTablesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "distributionChannels",
                    "type": DistributionChannelsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "groupsOfDistributionChannels",
                    "type": GroupsOfDistributionChannelsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "fulfilmentMethods",
                    "type": FulfilmentMethodsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "typesOfTravelDocuments",
                    "type": TypesOfTravelDocumentInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "salesOfferPackages",
                    "type": SalesOfferPackagesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "salesOfferPackageElements",
                    "type": SalesOfferPackageElementsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "salesOfferPackageSubstitutions",
                    "type": SalesOfferPackageSubstitutionsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "groupsOfSalesOfferPackages",
                    "type": GroupsOfSalesOfferPackagesInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "distributionAssignments",
                    "type": DistributionAssignmentsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "parkingTariffs",
                    "type": ParkingTariffsInFrameRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 43,
        }
    )
