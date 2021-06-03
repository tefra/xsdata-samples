from dataclasses import dataclass, field
from typing import List, Optional
from autosar.models.annotation import VariationPoint
from autosar.models.identifier import Identifier
from autosar.models.mc_data_instance_subtypes_enum import McDataInstanceSubtypesEnum
from autosar.models.ref import Ref
from autosar.models.rpt_execution_context_subtypes_enum import RptExecutionContextSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RoleBasedMcDataAssignment:
    """This meta-class allows to define links that specify logical
    relationships between single McDataInstances. The details on the existence
    and semantics of such links are not standardized.

    Possible Use Case: Rapid Prototyping solutions in which additional
    communication buffers and switches are implemented  in the RTE that
    allow to switch between the usage of the original and the bypass
    buffers. The different buffers and the switch can be represented by
    McDataInstances (in order to be accessed by MC tools) which have
    relationships to each other.

    :ivar execution_context_refs: Determines the executionContext in
        which the McDataInstance describing a local (e.g Task-Local)
        buffer of a gobal buffer is valid.
    :ivar mc_data_instance_refs: The target of the assignment.
    :ivar role: Shall be used to specify the role of the assigned data
        instance in relation to the instance that owns the assignment.
        The standardized roles of the RoleBasedMcDataAssignment.role
        attribute are: * GlobalMeasurementBuffer * RpEnablerFlag *
        RpRunnableDisablerFlag * BufferOf
    :ivar variation_point: This element was generated/modified due to an
        atpVariation stereotype.
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
        name = "ROLE-BASED-MC-DATA-ASSIGNMENT"

    execution_context_refs: Optional["RoleBasedMcDataAssignment.ExecutionContextRefs"] = field(
        default=None,
        metadata={
            "name": "EXECUTION-CONTEXT-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mc_data_instance_refs: Optional["RoleBasedMcDataAssignment.McDataInstanceRefs"] = field(
        default=None,
        metadata={
            "name": "MC-DATA-INSTANCE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    role: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "ROLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    s: Optional[str] = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        }
    )
    t: Optional[str] = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        }
    )

    @dataclass
    class ExecutionContextRefs:
        execution_context_ref: List["RoleBasedMcDataAssignment.ExecutionContextRefs.ExecutionContextRef"] = field(
            default_factory=list,
            metadata={
                "name": "EXECUTION-CONTEXT-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class ExecutionContextRef(Ref):
            dest: Optional[RptExecutionContextSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )

    @dataclass
    class McDataInstanceRefs:
        mc_data_instance_ref: List["RoleBasedMcDataAssignment.McDataInstanceRefs.McDataInstanceRef"] = field(
            default_factory=list,
            metadata={
                "name": "MC-DATA-INSTANCE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class McDataInstanceRef(Ref):
            dest: Optional[McDataInstanceSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
