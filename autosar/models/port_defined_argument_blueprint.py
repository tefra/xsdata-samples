from dataclasses import dataclass, field
from typing import Optional

from .admin_data import (
    DocumentationBlock,
    VariationPoint,
)
from .implementation_data_type_subtypes_enum import (
    ImplementationDataTypeSubtypesEnum,
)
from .ref import Ref

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class PortDefinedArgumentBlueprint:
    """
    This class describes a Blueprint of a PortDefinedArgument which needs to be
    defined in the SwcInternalBehavior of the component implementing the server of
    the ClientServerInterface.

    :ivar blueprint_mapping_guide: This attribute offers the possibility
        to provide additional information with respect to the mapping.
    :ivar value_type_ref: The implementation type of this argument
        value.
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
        name = "PORT-DEFINED-ARGUMENT-BLUEPRINT"

    blueprint_mapping_guide: Optional[DocumentationBlock] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-MAPPING-GUIDE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    value_type_ref: Optional["PortDefinedArgumentBlueprint.ValueTypeRef"] = (
        field(
            default=None,
            metadata={
                "name": "VALUE-TYPE-REF",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
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
    class ValueTypeRef(Ref):
        dest: Optional[ImplementationDataTypeSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
