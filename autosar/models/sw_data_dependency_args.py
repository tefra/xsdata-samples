from dataclasses import dataclass, field
from typing import List, Optional
from .autosar_parameter_ref import AutosarParameterRef
from .autosar_variable_ref import AutosarVariableRef
from .mc_data_instance_subtypes_enum import McDataInstanceSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwDataDependencyArgs:
    """
    This element specifies the elements used in a SwDataDependency.

    :ivar ar_parameter: This represents a Parameter within AUTOSAR. Note
        that the Datatype of the referenced ParameterDataPrototype shall
        be an ApplicationDataType of category VALUE.
    :ivar mc_data_instance_ref: This reference is used in the McSupport
        file to express the final instance of group axis etc. It is not
        allowed to use this outside of an McDataInstance. The referenced
        mcDataInstance shall be originated from a
        ParameterDataPrototype.
    :ivar autosar_variable: This represents the reference to a Variable
        in an Autosar system. Note that the target of the reference
        within AutosarVariableRef shall be typed by a  primitive data
        type
    :ivar mc_data_instance_var_ref: This reference is used in the
        McSupport file to express the final instance of input values
        etc. It is not allowed to use this outside of an McDataInstance.
        The referenced mcDataInstance shall be originated from a
        VariableDataPrototype.
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
        name = "SW-DATA-DEPENDENCY-ARGS"

    ar_parameter: List[AutosarParameterRef] = field(
        default_factory=list,
        metadata={
            "name": "AR-PARAMETER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequence": 1,
        },
    )
    mc_data_instance_ref: List[
        "SwDataDependencyArgs.McDataInstanceRef"
    ] = field(
        default_factory=list,
        metadata={
            "name": "MC-DATA-INSTANCE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequence": 1,
        },
    )
    autosar_variable: List[AutosarVariableRef] = field(
        default_factory=list,
        metadata={
            "name": "AUTOSAR-VARIABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequence": 2,
        },
    )
    mc_data_instance_var_ref: List[
        "SwDataDependencyArgs.McDataInstanceVarRef"
    ] = field(
        default_factory=list,
        metadata={
            "name": "MC-DATA-INSTANCE-VAR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "sequence": 2,
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
    class McDataInstanceRef(Ref):
        dest: Optional[McDataInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class McDataInstanceVarRef(Ref):
        dest: Optional[McDataInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
