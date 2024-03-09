from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean
from .ref import Ref
from .software_cluster_dependency_operator_enum import (
    SoftwareClusterDependencyOperatorEnum,
)
from .software_cluster_subtypes_enum import SoftwareClusterSubtypesEnum
from .strong_revision_label_string import StrongRevisionLabelString

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SoftwareClusterDependencyCompareCondition:
    """
    This meta-class represents the ability to specify a concrete dependency
    condition in the context of a SoftwareClusterDependencyFormula.

    :ivar compare_type: This attribute identifies the semantics of the
        compare operator.
    :ivar consider_build_number: If this attribute is set to true then
        the build number shall be taken into account for the comparison.
        Build numbers don't have to be consecutive but could be created
        by some kind of hashing algorithm. In such a case it might make
        sense to include the build number in a test for equality but it
        is probably not reasonable to apply e.g. a less-than comparison.
    :ivar software_cluster_ref: This reference identifies the
        SoftwareCluster to which the dependency/conflict applies.
    :ivar version: This attribute represents the value of a version
        against which the comparison shall be executed.
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
        name = "SOFTWARE-CLUSTER-DEPENDENCY-COMPARE-CONDITION"

    compare_type: Optional[SoftwareClusterDependencyOperatorEnum] = field(
        default=None,
        metadata={
            "name": "COMPARE-TYPE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    consider_build_number: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "CONSIDER-BUILD-NUMBER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    software_cluster_ref: Optional[
        "SoftwareClusterDependencyCompareCondition.SoftwareClusterRef"
    ] = field(
        default=None,
        metadata={
            "name": "SOFTWARE-CLUSTER-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    version: Optional[StrongRevisionLabelString] = field(
        default=None,
        metadata={
            "name": "VERSION",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass
    class SoftwareClusterRef(Ref):
        dest: Optional[SoftwareClusterSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
