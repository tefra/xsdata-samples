from dataclasses import dataclass, field
from typing import List
from .capping_rule_price import CappingRulePrice
from .capping_rule_price_ref import CappingRulePriceRef
from .cell_versioned_child_structure import (
    ParkingPrice,
    PriceGroup1,
)
from .controllable_element_price import ControllableElementPrice
from .controllable_element_price_ref import ControllableElementPriceRef
from .customer_purchase_package_price import CustomerPurchasePackagePrice
from .customer_purchase_package_price_ref import CustomerPurchasePackagePriceRef
from .distance_matrix_element_price import DistanceMatrixElementPrice
from .distance_matrix_element_price_ref import DistanceMatrixElementPriceRef
from .fare_price_1 import FarePrice1
from .fare_price_2 import FarePrice2
from .fare_price_ref import FarePriceRef
from .fare_product_price import FareProductPrice
from .fare_product_price_ref import FareProductPriceRef
from .fare_structure_element_price import FareStructureElementPrice
from .fare_structure_element_price_ref import FareStructureElementPriceRef
from .fulfilment_method_price import FulfilmentMethodPrice
from .fulfilment_method_price_ref import FulfilmentMethodPriceRef
from .geographical_interval_price import GeographicalIntervalPrice
from .geographical_interval_price_ref import GeographicalIntervalPriceRef
from .geographical_unit_price import GeographicalUnitPrice
from .geographical_unit_price_ref import GeographicalUnitPriceRef
from .parking_price_ref import ParkingPriceRef
from .price_group_2 import PriceGroup2
from .price_group_ref import PriceGroupRef
from .quality_structure_factor_price import QualityStructureFactorPrice
from .quality_structure_factor_price_ref import QualityStructureFactorPriceRef
from .sales_offer_package_price import SalesOfferPackagePrice
from .sales_offer_package_price_ref import SalesOfferPackagePriceRef
from .series_constraint_price import SeriesConstraintPrice
from .series_constraint_price_ref import SeriesConstraintPriceRef
from .strict_containment_aggregation_structure import StrictContainmentAggregationStructure
from .time_interval_price import TimeIntervalPrice
from .time_interval_price_ref import TimeIntervalPriceRef
from .time_unit_price import TimeUnitPrice
from .time_unit_price_ref import TimeUnitPriceRef
from .usage_parameter_price import UsageParameterPrice
from .usage_parameter_price_ref import UsageParameterPriceRef
from .validable_element_price import ValidableElementPrice
from .validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class CompositePricesRelStructure(StrictContainmentAggregationStructure):
    class Meta:
        name = "compositePrices_RelStructure"

    customer_purchase_package_price_ref: List[CustomerPurchasePackagePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackagePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_price_ref: List[ParkingPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_interval_price_ref: List[TimeIntervalPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_unit_price_ref: List[TimeUnitPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factor_price_ref: List[QualityStructureFactorPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactorPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element_price_ref: List[ControllableElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_element_price_ref: List[ValidableElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_interval_price_ref: List[GeographicalIntervalPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalIntervalPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit_price_ref: List[GeographicalUnitPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnitPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_parameter_price_ref: List[UsageParameterPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_price_ref: List[SalesOfferPackagePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackagePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_price_ref: List[DistanceMatrixElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_element_price_ref: List[FareStructureElementPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fulfilment_method_price_ref: List[FulfilmentMethodPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraint_price_ref: List[SeriesConstraintPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capping_rule_price_ref: List[CappingRulePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "CappingRulePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_product_price_ref: List[FareProductPriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareProductPriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_price_ref: List[FarePriceRef] = field(
        default_factory=list,
        metadata={
            "name": "FarePriceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_group_ref: List[PriceGroupRef] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroupRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_price: List[CustomerPurchasePackagePrice] = field(
        default_factory=list,
        metadata={
            "name": "CustomerPurchasePackagePrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_price: List[ParkingPrice] = field(
        default_factory=list,
        metadata={
            "name": "ParkingPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_price: List[SalesOfferPackagePrice] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackagePrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fulfilment_method_price: List[FulfilmentMethodPrice] = field(
        default_factory=list,
        metadata={
            "name": "FulfilmentMethodPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    capping_rule_price: List[CappingRulePrice] = field(
        default_factory=list,
        metadata={
            "name": "CappingRulePrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_product_price: List[FareProductPrice] = field(
        default_factory=list,
        metadata={
            "name": "FareProductPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_element_price: List[FareStructureElementPrice] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_interval_price: List[TimeIntervalPrice] = field(
        default_factory=list,
        metadata={
            "name": "TimeIntervalPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    time_unit_price: List[TimeUnitPrice] = field(
        default_factory=list,
        metadata={
            "name": "TimeUnitPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    quality_structure_factor_price: List[QualityStructureFactorPrice] = field(
        default_factory=list,
        metadata={
            "name": "QualityStructureFactorPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element_price: List[ControllableElementPrice] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_element_price: List[ValidableElementPrice] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElementPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    usage_parameter_price: List[UsageParameterPrice] = field(
        default_factory=list,
        metadata={
            "name": "UsageParameterPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_price: List[DistanceMatrixElementPrice] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElementPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_interval_price: List[GeographicalIntervalPrice] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalIntervalPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_unit_price: List[GeographicalUnitPrice] = field(
        default_factory=list,
        metadata={
            "name": "GeographicalUnitPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraint_price: List[SeriesConstraintPrice] = field(
        default_factory=list,
        metadata={
            "name": "SeriesConstraintPrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_price: List[FarePrice1] = field(
        default_factory=list,
        metadata={
            "name": "FarePrice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_fare_price: List[FarePrice2] = field(
        default_factory=list,
        metadata={
            "name": "FarePrice_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    price_group: List[PriceGroup1] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    netex_org_uk_netex_price_group: List[PriceGroup2] = field(
        default_factory=list,
        metadata={
            "name": "PriceGroup_",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
