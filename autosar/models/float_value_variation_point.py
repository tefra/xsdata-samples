from dataclasses import dataclass, field
from typing import List, Optional, Type
from .binding_time_enum_simple import BindingTimeEnumSimple
from .ref import Ref
from .sw_systemconst_subtypes_enum import SwSystemconstSubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FloatValueVariationPoint:
    """This class represents an attribute value variation point for Float
    attributes.

    Note that this class might be used in the extended meta-model only

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
    :ivar binding_time: This is the binding time in which the attribute
        value needs to be bound. If this attribute is missing, the
        attribute is not a variation point. In particular this means
        that It needs to be a single value according to the type
        specified in the pure model. It is an error if it is still a
        formula.
    :ivar blueprint_value: This represents a description that documents
        how the value shall be defined when deriving objects from the
        blueprint.
    :ivar sd: This special data is provided to allow synchronization of
        Attribute value variation points with variant management
        systems. The usage is subject of agreement between the involved
        parties.
    :ivar short_label: This allows to identify the variation point. It
        is also intended to allow RTE support for CompileTime Variation
        points.
    :ivar content:
    """
    class Meta:
        name = "FLOAT-VALUE-VARIATION-POINT"

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
    binding_time: Optional[BindingTimeEnumSimple] = field(
        default=None,
        metadata={
            "name": "BINDING-TIME",
            "type": "Attribute",
        }
    )
    blueprint_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "BLUEPRINT-VALUE",
            "type": "Attribute",
        }
    )
    sd: Optional[str] = field(
        default=None,
        metadata={
            "name": "SD",
            "type": "Attribute",
        }
    )
    short_label: Optional[str] = field(
        default=None,
        metadata={
            "name": "SHORT-LABEL",
            "type": "Attribute",
            "max_length": 128,
            "pattern": r"[a-zA-Z]([a-zA-Z0-9]|_[a-zA-Z0-9])*_?",
        }
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "SYSC-STRING-REF",
                    "type": Type["FloatValueVariationPoint.SyscStringRef"],
                    "namespace": "http://autosar.org/schema/r4.0",
                },
                {
                    "name": "SYSC-REF",
                    "type": Type["FloatValueVariationPoint.SyscRef"],
                    "namespace": "http://autosar.org/schema/r4.0",
                },
            ),
        }
    )

    @dataclass
    class SyscStringRef(Ref):
        dest: Optional[SwSystemconstSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass
    class SyscRef(Ref):
        dest: Optional[SwSystemconstSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
