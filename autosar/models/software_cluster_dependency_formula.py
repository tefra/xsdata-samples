from __future__ import annotations

from dataclasses import dataclass, field

from .category_string import CategoryString
from .software_cluster_dependency_compare_condition import (
    SoftwareClusterDependencyCompareCondition,
)
from .software_cluster_dependency_logical_operator_enum import (
    SoftwareClusterDependencyLogicalOperatorEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SoftwareClusterDependencyFormula:
    """
    This meta-class represents the ability to define a dependency among
    SoftwareClusters.

    :ivar category: This attribute specializes the semantics of the
        enclosing SoftwareClusterDependencyFormula.
    :ivar operator: This logical operator can be used to relate the
        results of different SoftwareClusterDependencyParts.
    :ivar parts: This aggregation represents the ordered collection of
        the parts of the SoftwareClusterDependencyFormula.
    :ivar s: Checksum calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine if
        an ArObject has changed. The checksum has no semantic meaning
        for an AUTOSAR model and there is no requirement for AUTOSAR
        tools to manage the checksum.
    :ivar t: Timestamp calculated by the user's tool environment for an
        ArObject. May be used in an own tool environment to determine
        the last change of an ArObject. The timestamp has no semantic
        meaning for an AUTOSAR model and there is no requirement for
        AUTOSAR tools to manage the timestamp.
    """

    class Meta:
        name = "SOFTWARE-CLUSTER-DEPENDENCY-FORMULA"

    category: CategoryString | None = field(
        default=None,
        metadata={
            "name": "CATEGORY",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    operator: SoftwareClusterDependencyLogicalOperatorEnum | None = field(
        default=None,
        metadata={
            "name": "OPERATOR",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    parts: SoftwareClusterDependencyFormula.Parts | None = field(
        default=None,
        metadata={
            "name": "PARTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: str | None = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: str | None = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class Parts:
        software_cluster_dependency_compare_condition: list[
            SoftwareClusterDependencyCompareCondition
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOFTWARE-CLUSTER-DEPENDENCY-COMPARE-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
        software_cluster_dependency_formula: list[
            SoftwareClusterDependencyFormula
        ] = field(
            default_factory=list,
            metadata={
                "name": "SOFTWARE-CLUSTER-DEPENDENCY-FORMULA",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
