from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .bsw_module_entity_subtypes_enum import BswModuleEntitySubtypesEnum
from .ref import Ref
from .runnable_entity_subtypes_enum import RunnableEntitySubtypesEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SwcBswRunnableMapping:
    """
    Maps a BswModuleEntity to a RunnableEntity if it is implemented as part
    of a BSW module (in the case of an AUTOSAR Service, a Complex Driver or
    an ECU Abstraction).

    The mapping can be used by a tool to find relevant information on the
    behavior, e.g. whether the bswEntity shall be running in interrupt
    context.

    :ivar bsw_entity_ref: The mapped BswModuleEntity
    :ivar swc_runnable_ref: The mapped SWC runnable.
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
        name = "SWC-BSW-RUNNABLE-MAPPING"

    bsw_entity_ref: None | SwcBswRunnableMapping.BswEntityRef = field(
        default=None,
        metadata={
            "name": "BSW-ENTITY-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    swc_runnable_ref: None | SwcBswRunnableMapping.SwcRunnableRef = field(
        default=None,
        metadata={
            "name": "SWC-RUNNABLE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    variation_point: None | VariationPoint = field(
        default=None,
        metadata={
            "name": "VARIATION-POINT",
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

    @dataclass
    class BswEntityRef(Ref):
        dest: None | BswModuleEntitySubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SwcRunnableRef(Ref):
        dest: None | RunnableEntitySubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
