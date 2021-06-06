from dataclasses import dataclass, field
from typing import Optional
from .abstract_implementation_data_type_subtypes_enum import AbstractImplementationDataTypeSubtypesEnum
from .application_data_type_subtypes_enum import ApplicationDataTypeSubtypesEnum
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class DataTypeMap:
    """
    This class represents the relationship between ApplicationDataType and its
    implementing AbstractImplementationDataType.

    :ivar application_data_type_ref: This is the corresponding
        ApplicationDataType
    :ivar implementation_data_type_ref: This is the corresponding
        AbstractImplementationDataType.
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
        name = "DATA-TYPE-MAP"

    application_data_type_ref: Optional["DataTypeMap.ApplicationDataTypeRef"] = field(
        default=None,
        metadata={
            "name": "APPLICATION-DATA-TYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    implementation_data_type_ref: Optional["DataTypeMap.ImplementationDataTypeRef"] = field(
        default=None,
        metadata={
            "name": "IMPLEMENTATION-DATA-TYPE-REF",
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
    class ApplicationDataTypeRef(Ref):
        dest: Optional[ApplicationDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class ImplementationDataTypeRef(Ref):
        dest: Optional[AbstractImplementationDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
