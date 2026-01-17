from dataclasses import dataclass, field
from typing import Optional

from .admin_data import VariationPoint
from .identifier import Identifier
from .implementation_data_type_subtypes_enum import (
    ImplementationDataTypeSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class RoleBasedDataTypeAssignment:
    """
    This class specifies an assignment of a role to a particular data type
    of a software component (or in the BswModuleBehavior of a module or
    cluster) in the context of an AUTOSAR Service.

    With this assignment, the role of the data type can be mapped to a
    specific ServiceNeeds element, so that a tool is able to create the
    correct access.

    :ivar role: This is the role of the associated data type in the
        given context.
    :ivar used_implementation_data_type_ref: This represents the
        associated ImplementationDataType.
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
        name = "ROLE-BASED-DATA-TYPE-ASSIGNMENT"

    role: Optional[Identifier] = field(
        default=None,
        metadata={
            "name": "ROLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    used_implementation_data_type_ref: Optional[
        "RoleBasedDataTypeAssignment.UsedImplementationDataTypeRef"
    ] = field(
        default=None,
        metadata={
            "name": "USED-IMPLEMENTATION-DATA-TYPE-REF",
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
    class UsedImplementationDataTypeRef(Ref):
        dest: Optional[ImplementationDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
