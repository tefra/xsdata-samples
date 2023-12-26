from dataclasses import dataclass, field
from typing import List, Optional
from .boolean_operator_enumeration import BooleanOperatorEnumeration
from .containment_aggregation_structure import ContainmentAggregationStructure
from .distribution_assignment_ref import DistributionAssignmentRef
from .organisation_ref_structure import OrganisationRefStructure
from .point_ref_structure import PointRefStructure
from .validity_parameter_assignment_version_structure import (
    ValidityParameterAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SpecificParameterAssignmentVersionStructure(
    ValidityParameterAssignmentVersionStructure
):
    class Meta:
        name = "SpecificParameterAssignment_VersionStructure"

    access_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "AccessNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    includes_grouping_type: Optional[BooleanOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "IncludesGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    includes: Optional["SpecificParameterAssignmentsRelStructure"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_assignment_ref: Optional[DistributionAssignmentRef] = field(
        default=None,
        metadata={
            "name": "DistributionAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retailing_organization_ref: Optional[OrganisationRefStructure] = field(
        default=None,
        metadata={
            "name": "RetailingOrganizationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    collection_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "CollectionPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass
class SpecificParameterAssignment(SpecificParameterAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass
class SpecificParameterAssignmentsRelStructure(
    ContainmentAggregationStructure
):
    class Meta:
        name = "specificParameterAssignments_RelStructure"

    specific_parameter_assignment: List[SpecificParameterAssignment] = field(
        default_factory=list,
        metadata={
            "name": "SpecificParameterAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
