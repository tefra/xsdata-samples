from dataclasses import dataclass, field
from typing import Optional, Union

from .distance_matrix_element_ref import DistanceMatrixElementRef
from .distance_matrix_elements_rel_structure import (
    DistanceMatrixElementsRelStructure,
)
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_quota_factor_ref import FareQuotaFactorRef
from .fare_structure_element_prices_rel_structure import (
    FareStructureElementPricesRelStructure,
)
from .fare_structure_elements_in_sequence_rel_structure import (
    FareStructureElementsInSequenceRelStructure,
)
from .generic_parameter_assignments_rel_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
    GenericParameterAssignmentsRelStructure,
)
from .geographical_interval_ref import GeographicalIntervalRef
from .geographical_intervals_rel_structure import (
    GeographicalIntervalsRelStructure,
)
from .geographical_structure_factors_rel_structure import (
    GeographicalStructureFactorsRelStructure,
)
from .group_of_distance_matrix_elements import GroupOfDistanceMatrixElements
from .group_of_distance_matrix_elements_ref import (
    GroupOfDistanceMatrixElementsRef,
)
from .priceable_object_version_structure import PriceableObjectVersionStructure
from .quality_structure_factor_ref import QualityStructureFactorRef
from .quality_structure_factors_rel_structure import (
    QualityStructureFactorsRelStructure,
)
from .tariff_basis_enumeration import TariffBasisEnumeration
from .time_interval_ref import TimeIntervalRef
from .time_intervals_rel_structure import TimeIntervalsRelStructure
from .time_structure_factors_rel_structure import (
    TimeStructureFactorsRelStructure,
)
from .type_of_fare_structure_element_ref import TypeOfFareStructureElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FareStructureElementVersionStructure(PriceableObjectVersionStructure):
    class Meta:
        name = "FareStructureElement_VersionStructure"

    tariff_basis: Optional[TariffBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "TariffBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_fare_structure_element_ref: Optional[
        TypeOfFareStructureElementRef
    ] = field(
        default=None,
        metadata={
            "name": "TypeOfFareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    geographical_interval_ref_or_geographical_intervals_or_geographical_structure_factors: Optional[
        Union[
            GeographicalIntervalRef,
            GeographicalIntervalsRelStructure,
            GeographicalStructureFactorsRelStructure,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalIntervalRef",
                    "type": GeographicalIntervalRef,
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
            ),
        },
    )
    time_interval_ref_or_time_intervals_or_time_structure_factors: Optional[
        Union[
            TimeIntervalRef,
            TimeIntervalsRelStructure,
            TimeStructureFactorsRelStructure,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeIntervalRef",
                    "type": TimeIntervalRef,
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
            ),
        },
    )
    choice: Optional[
        Union[
            FareQuotaFactorRef,
            FareDemandFactorRef,
            QualityStructureFactorRef,
            QualityStructureFactorsRelStructure,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareQuotaFactorRef",
                    "type": FareQuotaFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorRef",
                    "type": QualityStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "qualityStructureFactors",
                    "type": QualityStructureFactorsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice_1: Optional[
        Union[
            DistanceMatrixElementRef,
            DistanceMatrixElementsRelStructure,
            GroupOfDistanceMatrixElementsRef,
            GroupOfDistanceMatrixElements,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "distanceMatrixElements",
                    "type": DistanceMatrixElementsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElementsRef",
                    "type": GroupOfDistanceMatrixElementsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistanceMatrixElements",
                    "type": GroupOfDistanceMatrixElements,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    fare_structure_elements_in_sequence: Optional[
        FareStructureElementsInSequenceRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "fareStructureElementsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context: Optional[
        Union[
            GenericParameterAssignmentsRelStructure,
            GenericParameterAssignment,
            GenericParameterAssignmentInContext,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "validityParameterAssignments",
                    "type": GenericParameterAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    prices: Optional[FareStructureElementPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    name_of_class_of_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClassOfUnit",
            "type": "Attribute",
        },
    )
