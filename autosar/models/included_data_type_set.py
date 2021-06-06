from dataclasses import dataclass, field
from typing import List, Optional
from .autosar_data_type_subtypes_enum import AutosarDataTypeSubtypesEnum
from .identifier import Identifier
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class IncludedDataTypeSet:
    """An includedDataTypeSet declares that a set of AutosarDataType is used by
    a basic software module or a software component for its implementation and
    the AutosarDataType becomes part of the contract.

    This information is required if the AutosarDataType is not used for
    any DataPrototype owned by this software component or if the
    enumeration literals, lowerLimit and upperLimit constants shall be
    generated with a literalPrefix. The optional literalPrefix is used
    to add a common prefix on enumeration literals, lowerLimit and
    upperLimit constants created by the RTE.

    :ivar data_type_refs: AutosarDataType belonging to the
        includedDataTypeSet
    :ivar literal_prefix: LiteralPrefix defines a common prefix for all
        AutosarDataTypes of the includedDataTypeSet to be added on
        enumeration literals, lowerLimit and upperLimit constants
        created by the RTE.
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
        name = "INCLUDED-DATA-TYPE-SET"

    data_type_refs: Optional["IncludedDataTypeSet.DataTypeRefs"] = field(
        default=None,
        metadata={
            "name": "DATA-TYPE-REFS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        }
    )
    literal_prefix: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "LITERAL-PREFIX",
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
    class DataTypeRefs:
        data_type_ref: List["IncludedDataTypeSet.DataTypeRefs.DataTypeRef"] = field(
            default_factory=list,
            metadata={
                "name": "DATA-TYPE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            }
        )

        @dataclass
        class DataTypeRef(Ref):
            dest: Optional[AutosarDataTypeSubtypesEnum] = field(
                default=None,
                metadata={
                    "name": "DEST",
                    "type": "Attribute",
                    "required": True,
                }
            )
