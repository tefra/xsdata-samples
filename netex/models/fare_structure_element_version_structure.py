from dataclasses import dataclass, field
from typing import List, Optional
from .cell_versioned_child_structure import PriceableObjectVersionStructure
from .distance_matrix_element_ref import DistanceMatrixElementRef
from .distance_matrix_elements_rel_structure import DistanceMatrixElementsRelStructure
from .fare_demand_factor_ref import FareDemandFactorRef
from .fare_quota_factor_ref import FareQuotaFactorRef
from .fare_structure_element_prices_rel_structure import FareStructureElementPricesRelStructure
from .fare_structure_elements_in_sequence_rel_structure import FareStructureElementsInSequenceRelStructure
from .generic_parameter_assignment_version_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
    GenericParameterAssignmentsRelStructure,
)
from .geographical_interval_ref import GeographicalIntervalRef
from .geographical_intervals_rel_structure import GeographicalIntervalsRelStructure
from .geographical_structure_factors_rel_structure import GeographicalStructureFactorsRelStructure
from .group_of_distance_matrix_elements import GroupOfDistanceMatrixElements
from .group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from .quality_structure_factor_ref import QualityStructureFactorRef
from .quality_structure_factors_rel_structure import QualityStructureFactorsRelStructure
from .tariff_basis_enumeration import TariffBasisEnumeration
from .time_interval_ref import TimeIntervalRef
from .time_intervals_rel_structure import TimeIntervalsRelStructure
from .time_structure_factors_rel_structure import TimeStructureFactorsRelStructure
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
        }
    )
    type_of_fare_structure_element_ref: Optional[TypeOfFareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    geographical_interval_ref: Optional[GeographicalIntervalRef] = field(
        default=None,
        metadata={
            "name": "GeographicalIntervalRef",
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
    time_interval_ref: Optional[TimeIntervalRef] = field(
        default=None,
        metadata={
            "name": "TimeIntervalRef",
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
    fare_quota_factor_ref: List[FareQuotaFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareQuotaFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    fare_demand_factor_ref: List[FareDemandFactorRef] = field(
        default_factory=list,
        metadata={
            "name": "FareDemandFactorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    quality_structure_factor_ref: Optional[QualityStructureFactorRef] = field(
        default=None,
        metadata={
            "name": "QualityStructureFactorRef",
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
    distance_matrix_element_ref: Optional[DistanceMatrixElementRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementRef",
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
    group_of_distance_matrix_elements_ref: Optional[GroupOfDistanceMatrixElementsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_distance_matrix_elements: Optional[GroupOfDistanceMatrixElements] = field(
        default=None,
        metadata={
            "name": "GroupOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_elements_in_sequence: Optional[FareStructureElementsInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "fareStructureElementsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_assignments: Optional[GenericParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    generic_parameter_assignment: Optional[GenericParameterAssignment] = field(
        default=None,
        metadata={
            "name": "GenericParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    generic_parameter_assignment_in_context: Optional[GenericParameterAssignmentInContext] = field(
        default=None,
        metadata={
            "name": "GenericParameterAssignmentInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[FareStructureElementPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    name_of_class_of_unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfClassOfUnit",
            "type": "Attribute",
        }
    )
