from dataclasses import dataclass, field
from typing import Optional
from .annotation import VariationPoint
from .autosar_parameter_ref import AutosarParameterRef
from .autosar_variable_ref import AutosarVariableRef
from .identifier import Identifier
from .per_instance_memory_subtypes_enum import PerInstanceMemorySubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RoleBasedDataAssignment:
    """This class specifies an assignment of a role to a particular data object in
    the SwcInternalBehavior of a software component (or in the BswModuleBehavior of
    a module or cluster) in the context of an AUTOSAR Service.

    With this assignment, the role of the data can be mapped to a
    specific ServiceNeeds element, so that a tool is able to create the
    correct access.

    :ivar role: This is the role of the assigned data in the given
        context, for example for an NVRAM Block it is used to
        distinguish between an mirror block and a ROM default block.
        Possible values need to be specified on M1 level. This also is
        intended to support the so called "Signal based Approach" of the
        DCM. In this use case the name of the involved data element is
        required. This name shall be taken from the DataElement
        referenced by the property usedDataElement. The following values
        are standardized: * '''ramBlock''' indicates data to be used as
        a mirror for an NVRAM Block. * '''defaultValue''' indicates
        constant data to be used as default in the context of this
        ServiceNeeds, e.g. for an NVRAM Block. *
        '''signalBasedDiagnostics''' indicates the
        RoleBasedDataAssignment shall be used for signal based
        diagnostics.
    :ivar used_data_element: The VariableDataPrototype used in this
        role, e.g. * Permanent RAM Block of an NVRAM Block which shall
        belong to the same SwcInternalBehavior or BswInternalBehavior. *
        In the role signalBasedDiagnostics it has to refer to a
        VariableDataPrototype in a SenderReceiverInterface or a
        NvDataInterface.
    :ivar used_parameter_element: The ParameterDataPrototype used in
        this role, e.g. * ROM Block of an NVRAM Block. It shall belong
        to the same SwcInternalBehavior or BswInternalbehavior. * In the
        role signalBasedDiagnostics it has to refer to a
        ParameterDataPrototype in a ParameterInterface.
    :ivar used_pim_ref: The (untyped) PerInstanceMemory used in this
        role (e.g. as a Permanent RAM Block for an NVRAM Block).
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
        name = "ROLE-BASED-DATA-ASSIGNMENT"

    role: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "ROLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    used_data_element: Optional[AutosarVariableRef] = field(
        default=None,
        metadata={
            "name": "USED-DATA-ELEMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    used_parameter_element: Optional[AutosarParameterRef] = field(
        default=None,
        metadata={
            "name": "USED-PARAMETER-ELEMENT",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    used_pim_ref: Optional["RoleBasedDataAssignment.UsedPimRef"] = field(
        default=None,
        metadata={
            "name": "USED-PIM-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: Optional[VariationPoint] = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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
    class UsedPimRef(Ref):
        dest: Optional[PerInstanceMemorySubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
