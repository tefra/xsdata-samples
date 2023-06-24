from dataclasses import dataclass, field
from typing import Optional
from .data_prototype_subtypes_enum import DataPrototypeSubtypesEnum
from .parameter_in_atomic_swc_type_instance_ref import ParameterInAtomicSwcTypeInstanceRef
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class AutosarParameterRef:
    """This class represents a reference to a parameter within AUTOSAR which can be one of the following use cases:
    localParameter:
    * localParameter which is used as whole (e.g.  sharedAxis for curve)
    autosarVariable:
    * a parameter provided via PortPrototype which is used as whole (e.g. parameterAccess)
    * an element inside of a composite local parameter typed by ApplicationDatatype (e.g. sharedAxis for a curve)
    * an element inside of a composite parameter provided via Port and typed by ApplicationDatatype (e.g. sharedAxis for a curve)
    autosarParameterInImplDatatype:
    * an element inside of a composite local parameter typed by ImplementationDatatype
    * an element inside of a composite parameter provided via PortPrototype and typed by ImplementationDatatype

    :ivar autosar_parameter_iref: This instance reference is used if the
        callibration parameter is either imported via a port or is part
        of a composite data structure.
    :ivar local_parameter_ref: In the majority of cases this reference
        goes to ParameterDataPrototypes rather than
        VariableDataPrototypes. Pointing the reference to a
        VariableDataPrototype is limited to special use cases, e.g. if
        the AutosarParameterRef is used in the context of an
        SwAxisGrouped. This reference is used if the arParameter is
        local to the current component. Of course, it would technically
        also be feasible to use an InstanceRef for this case. However,
        the InstanceRef would not have a contextElement (because the
        current instance is the context). Hence, the local instance is a
        special case which may provide further optimization. Therefore
        an explicit reference is provided for this case.
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
        name = "AUTOSAR-PARAMETER-REF"

    autosar_parameter_iref: Optional[ParameterInAtomicSwcTypeInstanceRef] = field(
        default=None,
        metadata={
            "name": "AUTOSAR-PARAMETER-IREF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    local_parameter_ref: Optional["AutosarParameterRef.LocalParameterRef"] = field(
        default=None,
        metadata={
            "name": "LOCAL-PARAMETER-REF",
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
    class LocalParameterRef(Ref):
        dest: Optional[DataPrototypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
