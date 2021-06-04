from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.access_right_parameter_assignments_in_frame_rel_structure import AccessRightParameterAssignmentsInFrameRelStructure
from netex.models.authority_ref import AuthorityRef
from netex.models.border_points_in_frame_rel_structure import BorderPointsInFrameRelStructure
from netex.models.common_version_frame_structure import CommonVersionFrameStructure
from netex.models.controllable_elements_in_frame_rel_structure import ControllableElementsInFrameRelStructure
from netex.models.distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from netex.models.distribution_assignments_in_frame_rel_structure import DistributionAssignmentsInFrameRelStructure
from netex.models.distribution_channels_in_frame_rel_structure import DistributionChannelsInFrameRelStructure
from netex.models.fare_prices_in_frame_rel_structure import FarePricesInFrameRelStructure
from netex.models.fare_products_in_frame_rel_structure import FareProductsInFrameRelStructure
from netex.models.fare_scheduled_stop_points_in_frame_rel_structure import FareScheduledStopPointsInFrameRelStructure
from netex.models.fare_sections_in_frame_rel_structure import FareSectionsInFrameRelStructure
from netex.models.fare_series_in_frame_rel_structure import FareSeriesInFrameRelStructure
from netex.models.fare_structure_elements_in_frame_rel_structure import FareStructureElementsInFrameRelStructure
from netex.models.fare_tables_in_frame_rel_structure import FareTablesInFrameRelStructure
from netex.models.fare_zones_in_frame_rel_structure import FareZonesInFrameRelStructure
from netex.models.fulfilment_methods_in_frame_rel_structure import FulfilmentMethodsInFrameRelStructure
from netex.models.geographical_intervals_rel_structure import GeographicalIntervalsRelStructure
from netex.models.geographical_structure_factors_rel_structure import GeographicalStructureFactorsRelStructure
from netex.models.geographical_units_rel_structure import GeographicalUnitsRelStructure
from netex.models.groups_of_distance_matrix_elements_rel_structure import GroupsOfDistanceMatrixElementsRelStructure
from netex.models.groups_of_distribution_channels_in_frame_rel_structure import GroupsOfDistributionChannelsInFrameRelStructure
from netex.models.groups_of_sales_offer_packages_in_frame_rel_structure import GroupsOfSalesOfferPackagesInFrameRelStructure
from netex.models.notice_assignments_in_frame_rel_structure import NoticeAssignmentsInFrameRelStructure
from netex.models.notices_in_frame_rel_structure import NoticesInFrameRelStructure
from netex.models.operator_ref import OperatorRef
from netex.models.parking_tariffs_in_frame_rel_structure import ParkingTariffsInFrameRelStructure
from netex.models.pricing_parameter_set import PricingParameterSet
from netex.models.quality_structure_factors_rel_structure import QualityStructureFactorsRelStructure
from netex.models.sales_offer_package_elements_in_frame_rel_structure import SalesOfferPackageElementsInFrameRelStructure
from netex.models.sales_offer_package_substitutions_in_frame_rel_structure import SalesOfferPackageSubstitutionsInFrameRelStructure
from netex.models.sales_offer_packages_in_frame_rel_structure import SalesOfferPackagesInFrameRelStructure
from netex.models.tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from netex.models.time_intervals_rel_structure import TimeIntervalsRelStructure
from netex.models.time_structure_factors_rel_structure import TimeStructureFactorsRelStructure
from netex.models.time_units_rel_structure import TimeUnitsRelStructure
from netex.models.transport_organisation_ref import TransportOrganisationRef
from netex.models.types_of_travel_document_in_frame_rel_structure import TypesOfTravelDocumentInFrameRelStructure
from netex.models.usage_parameters_in_frame_rel_structure import UsageParametersInFrameRelStructure
from netex.models.validable_elements_in_frame_rel_structure import ValidableElementsInFrameRelStructure
from netex.models.vehicle_mode_enumeration import VehicleModeEnumeration

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
    transport_organisation_ref: Optional[TransportOrganisationRef] = field(
        default=None,
        metadata={
            "name": "TransportOrganisationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pricing_parameter_set: Optional[PricingParameterSet] = field(
        default=None,
        metadata={
            "name": "PricingParameterSet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notices: Optional[NoticesInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    notice_assignments: Optional[NoticeAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    border_points: Optional[BorderPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "borderPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_points: Optional[FareScheduledStopPointsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareScheduledStopPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_zones: Optional[FareZonesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_sections: Optional[FareSectionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareSections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraints: Optional[FareSeriesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "seriesConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_units: Optional[GeographicalUnitsRelStructure] = field(
        default=None,
        metadata={
            "name": "geographicalUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_intervals: Optional[GeographicalIntervalsRelStructure] = field(
        default=None,
        metadata={
            "name": "geographicalIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_structure_factors: Optional[GeographicalStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "geographicalStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_units: Optional[TimeUnitsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_intervals: Optional[TimeIntervalsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_structure_factors: Optional[TimeStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factors: Optional[QualityStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "qualityStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_elements: Optional[DistanceMatrixElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "distanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_distance_matrix_elements: Optional[GroupsOfDistanceMatrixElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_elements: Optional[FareStructureElementsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareStructureElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tariffs: Optional[TariffsInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_elements: Optional[ValidableElementsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "validableElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_elements: Optional[ControllableElementsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "controllableElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_parameters: Optional[UsageParametersInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "usageParameters",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_right_parameter_assignments: Optional[AccessRightParameterAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "accessRightParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_products: Optional[FareProductsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareProducts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_groups: Optional[FarePricesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_tables: Optional[FareTablesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_channels: Optional[DistributionChannelsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "distributionChannels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_distribution_channels: Optional[GroupsOfDistributionChannelsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfDistributionChannels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fulfilment_methods: Optional[FulfilmentMethodsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "fulfilmentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    types_of_travel_documents: Optional[TypesOfTravelDocumentInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "typesOfTravelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_packages: Optional[SalesOfferPackagesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "salesOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_elements: Optional[SalesOfferPackageElementsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "salesOfferPackageElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_substitutions: Optional[SalesOfferPackageSubstitutionsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "salesOfferPackageSubstitutions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    groups_of_sales_offer_packages: Optional[GroupsOfSalesOfferPackagesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "groupsOfSalesOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distribution_assignments: Optional[DistributionAssignmentsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "distributionAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_tariffs: Optional[ParkingTariffsInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "parkingTariffs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
