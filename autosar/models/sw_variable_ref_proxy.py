from __future__ import annotations

from dataclasses import dataclass, field

from .autosar_variable_ref import AutosarVariableRef
from .mc_data_instance_subtypes_enum import McDataInstanceSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class SwVariableRefProxy:
    """
    Proxy class for several kinds of references to a variable.

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
        name = "SW-VARIABLE-REF-PROXY"

    autosar_variable: None | AutosarVariableRef = field(
        default=None,
        metadata={
            "name": "AUTOSAR-VARIABLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mc_data_instance_var_ref: (
        None | SwVariableRefProxy.McDataInstanceVarRef
    ) = field(
        default=None,
        metadata={
            "name": "MC-DATA-INSTANCE-VAR-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    s: None | str = field(
        default=None,
        metadata={
            "name": "S",
            "type": "Attribute",
        },
    )
    t: None | str = field(
        default=None,
        metadata={
            "name": "T",
            "type": "Attribute",
            "pattern": r"([0-9]{4}-[0-9]{2}-[0-9]{2})(T[0-9]{2}:[0-9]{2}:[0-9]{2}(Z|([+\-][0-9]{2}:[0-9]{2})))?",
        },
    )

    @dataclass(kw_only=True)
    class McDataInstanceVarRef(Ref):
        dest: McDataInstanceSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
