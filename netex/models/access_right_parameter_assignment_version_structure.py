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
    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "ParkingTariffRef",
                    "type": ParkingTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffRef",
                    "type": TariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementRef",
                    "type": FareStructureElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementInSequenceRef",
                    "type": ControllableElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementInSequenceRef",
                    "type": FareStructureElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightInProductRef",
                    "type": AccessRightInProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareElementInSequenceRef",
                    "type": FareElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementInverseRef",
                    "type": DistanceMatrixElementInverseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementView",
                    "type": DistanceMatrixElementView,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageRef",
                    "type": SalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElementsRef",
                    "type": GroupOfDistanceMatrixElementsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfSalesOfferPackagesRef",
                    "type": GroupOfSalesOfferPackagesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LimitationGroupingType",
                    "type": BooleanOperatorEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                    "default": BooleanOperatorEnumeration.AND_VALUE,
                },
                {
                    "name": "LimitationSetSelectionType",
                    "type": SetOperatorEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "limitations",
                    "type": UsageParametersRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityParameterAssignmentType",
                    "type": RelativeOperatorEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                    "default": RelativeOperatorEnumeration.EQ,
                },
                {
                    "name": "ValidityParameterGroupingType",
                    "type": BooleanOperatorEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                    "default": BooleanOperatorEnumeration.AND_VALUE,
                },
                {
                    "name": "ValidityParameterSetSelectionType",
                    "type": SetOperatorEnumeration,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "temporalValidityParameters",
                    "type": TemporalValidityParametersRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "validityParameters",
                    "type": ValidityParametersRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
            "max_occurs": 70,
        }
    )
