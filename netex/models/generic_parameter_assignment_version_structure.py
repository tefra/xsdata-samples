from dataclasses import dataclass, field
from typing import List, Optional
from .boolean_operator_enumeration import BooleanOperatorEnumeration
from .containment_aggregation_structure import ContainmentAggregationStructure
from .validity_parameter_assignment_version_structure import ValidityParameterAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GenericParameterAssignmentVersionStructure(ValidityParameterAssignmentVersionStructure):
    class Meta:
        name = "GenericParameterAssignment_VersionStructure"

    includes_grouping_type: Optional[BooleanOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "IncludesGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    includes: Optional["GenericParameterAssignmentsRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )


@dataclass
class GenericParameterAssignment(GenericParameterAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class GenericParameterAssignmentInContext(GenericParameterAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class GenericParameterAssignmentsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "genericParameterAssignments_RelStructure"

    generic_parameter_assignment: List[GenericParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "GenericParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    generic_parameter_assignment_in_context: List[GenericParameterAssignmentInContext] = field(
        default_factory=list,
        metadata={
            "name": "GenericParameterAssignmentInContext",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )