from dataclasses import dataclass, field
from typing import List, Optional
from .access_right_in_product_ref import AccessRightInProductRef
from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .assignment_version_structure_1 import AssignmentVersionStructure1
from .boolean_operator_enumeration import BooleanOperatorEnumeration
from .capped_discount_right_ref import CappedDiscountRightRef
from .charging_basis_enumeration import ChargingBasisEnumeration
from .controllable_element_in_sequence_ref import ControllableElementInSequenceRef
from .controllable_element_ref import ControllableElementRef
from .distance_matrix_element_inverse_ref import DistanceMatrixElementInverseRef
from .distance_matrix_element_ref import DistanceMatrixElementRef
from .distance_matrix_element_view import DistanceMatrixElementView
from .fare_element_in_sequence_ref import FareElementInSequenceRef
from .fare_product_ref import FareProductRef
from .fare_structure_element_in_sequence_ref import FareStructureElementInSequenceRef
from .fare_structure_element_ref import FareStructureElementRef
from .group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from .group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from .parking_tariff_ref import ParkingTariffRef
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .relative_operator_enumeration import RelativeOperatorEnumeration
from .sale_discount_right_ref import SaleDiscountRightRef
from .sales_offer_package_ref import SalesOfferPackageRef
from .set_operator_enumeration import SetOperatorEnumeration
from .supplement_product_ref import SupplementProductRef
from .tariff_ref import TariffRef
from .temporal_validity_parameters_rel_structure import TemporalValidityParametersRelStructure
from .third_party_product_ref import ThirdPartyProductRef
from .type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from .usage_discount_right_ref import UsageDiscountRightRef
from .usage_parameters_rel_structure import UsageParametersRelStructure
from .validable_element_ref import ValidableElementRef
from .validity_parameters_rel_structure import ValidityParametersRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccessRightParameterAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "AccessRightParameterAssignment_VersionStructure"

    is_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_access_right_assignment_ref: Optional[TypeOfAccessRightAssignmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfAccessRightAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charging_basis: Optional[ChargingBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "ChargingBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_element_ref: Optional[ValidableElementRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element_ref: Optional[ControllableElementRef] = field(
        default=None,
        metadata={
            "name": "ControllableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
            "max_occurs": 4,
            "sequential": True,
        }
    )
    amount_of_price_unit_product_ref: List[AmountOfPriceUnitProductRef] = field(
        default_factory=list,
        metadata={
            "name": "AmountOfPriceUnitProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    usage_discount_right_ref: List[UsageDiscountRightRef] = field(
        default_factory=list,
        metadata={
            "name": "UsageDiscountRightRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
            "sequential": True,
        }
    )
    third_party_product_ref: List[ThirdPartyProductRef] = field(
        default_factory=list,
        metadata={
            "name": "ThirdPartyProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 4,
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
            "max_occurs": 4,
            "sequential": True,
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
    parking_tariff_ref: List[ParkingTariffRef] = field(
        default_factory=list,
        metadata={
            "name": "ParkingTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
        }
    )
    tariff_ref: Optional[TariffRef] = field(
        default=None,
        metadata={
            "name": "TariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_element_ref: Optional[FareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element_in_sequence_ref: List[ControllableElementInSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_structure_element_in_sequence_ref: List[FareStructureElementInSequenceRef] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    access_right_in_product_ref: List[AccessRightInProductRef] = field(
        default_factory=list,
        metadata={
            "name": "AccessRightInProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_element_in_sequence_ref: Optional[FareElementInSequenceRef] = field(
        default=None,
        metadata={
            "name": "FareElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_ref: Optional[DistanceMatrixElementRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_inverse_ref: Optional[DistanceMatrixElementInverseRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementInverseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_view: Optional[DistanceMatrixElementView] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementView",
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
    group_of_distance_matrix_elements_ref: Optional[GroupOfDistanceMatrixElementsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
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
    limitation_grouping_type: Optional[BooleanOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "LimitationGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limitation_set_selection_type: Optional[SetOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "LimitationSetSelectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limitations: Optional[UsageParametersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_assignment_type: Optional[RelativeOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "ValidityParameterAssignmentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_grouping_type: Optional[BooleanOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "ValidityParameterGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_set_selection_type: Optional[SetOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "ValidityParameterSetSelectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    temporal_validity_parameters: Optional[TemporalValidityParametersRelStructure] = field(
        default=None,
        metadata={
            "name": "temporalValidityParameters",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameters: Optional[ValidityParametersRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameters",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )