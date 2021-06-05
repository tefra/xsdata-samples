from dataclasses import dataclass, field
from typing import Optional
from autosar.models.autosar_parameter_ref import AutosarParameterRef
from autosar.models.mc_data_instance_subtypes_enum import McDataInstanceSubtypesEnum
from autosar.models.ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwCalprmRefProxy:
    """
    Wrapper class for different kinds of references to a calibration parameter.

    :ivar ar_parameter: This represents a Parameter within AUTOSAR. Note
        that the Datatype of the referenced ParameterDataPrototype shall
        be an ApplicationDataType of category VALUE.
    :ivar mc_data_instance_ref: This reference is used in the McSupport
        file to express the final instance of group axis etc. It is not
        allowed to use this outside of an McDataInstance. The referenced
        mcDataInstance shall be originated from a
        ParameterDataPrototype.
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
        name = "SW-CALPRM-REF-PROXY"

    ar_parameter: Optional[AutosarParameterRef] = field(
        default=None,
        metadata={
            "name": "AR-PARAMETER",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    mc_data_instance_ref: Optional["SwCalprmRefProxy.McDataInstanceRef"] = field(
        default=None,
        metadata={
            "name": "MC-DATA-INSTANCE-REF",
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
    class McDataInstanceRef(Ref):
        dest: Optional[McDataInstanceSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
