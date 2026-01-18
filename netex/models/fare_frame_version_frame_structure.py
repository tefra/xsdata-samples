from __future__ import annotations

from dataclasses import dataclass, field

from .access_right_parameter_assignments_in_frame_rel_structure import (
    AccessRightParameterAssignmentsInFrameRelStructure,
)
from .all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from .authority_ref import AuthorityRef
from .border_points_in_frame_rel_structure import (
    BorderPointsInFrameRelStructure,
)
from .common_version_frame_structure import CommonVersionFrameStructure
from .controllable_elements_in_frame_rel_structure import (
    ControllableElementsInFrameRelStructure,
)
from .distance_matrix_elements_rel_structure import (
    DistanceMatrixElementsRelStructure,
)
from .distribution_assignments_in_frame_rel_structure import (
    DistributionAssignmentsInFrameRelStructure,
)
from .distribution_channels_in_frame_rel_structure import (
    DistributionChannelsInFrameRelStructure,
)
from .fare_prices_in_frame_rel_structure import FarePricesInFrameRelStructure
from .fare_products_in_frame_rel_structure import (
    FareProductsInFrameRelStructure,
)
from .fare_scheduled_stop_points_in_frame_rel_structure import (
    FareScheduledStopPointsInFrameRelStructure,
)
from .fare_sections_in_frame_rel_structure import (
    FareSectionsInFrameRelStructure,
)
from .fare_series_in_frame_rel_structure import FareSeriesInFrameRelStructure
from .fare_structure_elements_in_frame_rel_structure import (
    FareStructureElementsInFrameRelStructure,
)
from .fare_tables_in_frame_rel_structure import FareTablesInFrameRelStructure
from .fare_zones_in_frame_rel_structure import FareZonesInFrameRelStructure
from .fulfilment_methods_in_frame_rel_structure import (
    FulfilmentMethodsInFrameRelStructure,
)
from .geographical_intervals_rel_structure import (
    GeographicalIntervalsRelStructure,
)
from .geographical_structure_factors_rel_structure import (
    GeographicalStructureFactorsRelStructure,
)
from .geographical_units_rel_structure import GeographicalUnitsRelStructure
from .groups_of_distance_matrix_elements_rel_structure import (
    GroupsOfDistanceMatrixElementsRelStructure,
)
from .groups_of_distribution_channels_in_frame_rel_structure import (
    GroupsOfDistributionChannelsInFrameRelStructure,
)
from .groups_of_sales_offer_packages_in_frame_rel_structure import (
    GroupsOfSalesOfferPackagesInFrameRelStructure,
)
from .notice_assignments_in_frame_rel_structure import (
    NoticeAssignmentsInFrameRelStructure,
)
from .notices_in_frame_rel_structure import NoticesInFrameRelStructure
from .operator_ref import OperatorRef
from .parking_tariffs_in_frame_rel_structure import (
    ParkingTariffsInFrameRelStructure,
)
from .pricing_parameter_set import PricingParameterSet
from .quality_structure_factors_rel_structure import (
    QualityStructureFactorsRelStructure,
)
from .sales_offer_package_elements_in_frame_rel_structure import (
    SalesOfferPackageElementsInFrameRelStructure,
)
from .sales_offer_package_substitutions_in_frame_rel_structure import (
    SalesOfferPackageSubstitutionsInFrameRelStructure,
)
from .sales_offer_packages_in_frame_rel_structure import (
    SalesOfferPackagesInFrameRelStructure,
)
from .tariffs_in_frame_rel_structure import TariffsInFrameRelStructure
from .time_intervals_rel_structure import TimeIntervalsRelStructure
from .time_structure_factors_rel_structure import (
    TimeStructureFactorsRelStructure,
)
from .time_units_rel_structure import TimeUnitsRelStructure
from .types_of_travel_document_in_frame_rel_structure import (
    TypesOfTravelDocumentInFrameRelStructure,
)
from .usage_parameters_in_frame_rel_structure import (
    UsageParametersInFrameRelStructure,
)
from .validable_elements_in_frame_rel_structure import (
    ValidableElementsInFrameRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareFrameVersionFrameStructure(CommonVersionFrameStructure):
    class Meta:
        name = "FareFrame_VersionFrameStructure"

    mode: None | AllVehicleModesOfTransportEnumeration = field(
        default=None,
        metadata={
            "name": "Mode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_organisation_ref: None | AuthorityRef | OperatorRef = field(
        default=None,
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
            ),
        },
    )
    pricing_parameter_set: None | PricingParameterSet = field(
        default=None,
        metadata={
            "name": "PricingParameterSet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notices: None | NoticesInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: None | NoticeAssignmentsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    border_points: None | BorderPointsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "borderPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_scheduled_stop_points: (
        None | FareScheduledStopPointsInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "fareScheduledStopPoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_zones: None | FareZonesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "fareZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_sections: None | FareSectionsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "fareSections",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    series_constraints: None | FareSeriesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "seriesConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    geographical_units: None | GeographicalUnitsRelStructure = field(
        default=None,
        metadata={
            "name": "geographicalUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    geographical_intervals: None | GeographicalIntervalsRelStructure = field(
        default=None,
        metadata={
            "name": "geographicalIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    geographical_structure_factors: (
        None | GeographicalStructureFactorsRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "geographicalStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_units: None | TimeUnitsRelStructure = field(
        default=None,
        metadata={
            "name": "timeUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_intervals: None | TimeIntervalsRelStructure = field(
        default=None,
        metadata={
            "name": "timeIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_structure_factors: None | TimeStructureFactorsRelStructure = field(
        default=None,
        metadata={
            "name": "timeStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quality_structure_factors: None | QualityStructureFactorsRelStructure = (
        field(
            default=None,
            metadata={
                "name": "qualityStructureFactors",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    distance_matrix_elements: None | DistanceMatrixElementsRelStructure = (
        field(
            default=None,
            metadata={
                "name": "distanceMatrixElements",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    groups_of_distance_matrix_elements: (
        None | GroupsOfDistanceMatrixElementsRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "groupsOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_structure_elements: (
        None | FareStructureElementsInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "fareStructureElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariffs: None | TariffsInFrameRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validable_elements: None | ValidableElementsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "validableElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    controllable_elements: None | ControllableElementsInFrameRelStructure = (
        field(
            default=None,
            metadata={
                "name": "controllableElements",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    usage_parameters: None | UsageParametersInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "usageParameters",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_right_parameter_assignments: (
        None | AccessRightParameterAssignmentsInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "accessRightParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_products: None | FareProductsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "fareProducts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_groups: None | FarePricesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_tables: None | FareTablesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_channels: None | DistributionChannelsInFrameRelStructure = (
        field(
            default=None,
            metadata={
                "name": "distributionChannels",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    groups_of_distribution_channels: (
        None | GroupsOfDistributionChannelsInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "groupsOfDistributionChannels",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fulfilment_methods: None | FulfilmentMethodsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "fulfilmentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    types_of_travel_documents: (
        None | TypesOfTravelDocumentInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "typesOfTravelDocuments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_offer_packages: None | SalesOfferPackagesInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "salesOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_offer_package_elements: (
        None | SalesOfferPackageElementsInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "salesOfferPackageElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_offer_package_substitutions: (
        None | SalesOfferPackageSubstitutionsInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "salesOfferPackageSubstitutions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    groups_of_sales_offer_packages: (
        None | GroupsOfSalesOfferPackagesInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "groupsOfSalesOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_assignments: (
        None | DistributionAssignmentsInFrameRelStructure
    ) = field(
        default=None,
        metadata={
            "name": "distributionAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_tariffs: None | ParkingTariffsInFrameRelStructure = field(
        default=None,
        metadata={
            "name": "parkingTariffs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
