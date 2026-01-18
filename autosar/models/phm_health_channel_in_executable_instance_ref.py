from __future__ import annotations

from dataclasses import dataclass, field

from .phm_health_channel_interface_subtypes_enum import (
    PhmHealthChannelInterfaceSubtypesEnum,
)
from .r_port_prototype_subtypes_enum import RPortPrototypeSubtypesEnum
from .ref import Ref
from .root_sw_component_prototype_subtypes_enum import (
    RootSwComponentPrototypeSubtypesEnum,
)
from .sw_component_prototype_subtypes_enum import (
    SwComponentPrototypeSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class PhmHealthChannelInExecutableInstanceRef:
    """
    :ivar context_root_sw_component_prototype_ref:
    :ivar context_component_prototype_ref:
    :ivar context_r_port_prototype_ref:
    :ivar target_health_channel_ref:
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
        name = "PHM-HEALTH-CHANNEL-IN-EXECUTABLE-INSTANCE-REF"

    context_root_sw_component_prototype_ref: (
        None
        | PhmHealthChannelInExecutableInstanceRef.ContextRootSwComponentPrototypeRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-ROOT-SW-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_component_prototype_ref: list[
        PhmHealthChannelInExecutableInstanceRef.ContextComponentPrototypeRef
    ] = field(
        default_factory=list,
        metadata={
            "name": "CONTEXT-COMPONENT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    context_r_port_prototype_ref: (
        None | PhmHealthChannelInExecutableInstanceRef.ContextRPortPrototypeRef
    ) = field(
        default=None,
        metadata={
            "name": "CONTEXT-R-PORT-PROTOTYPE-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    target_health_channel_ref: (
        None | PhmHealthChannelInExecutableInstanceRef.TargetHealthChannelRef
    ) = field(
        default=None,
        metadata={
            "name": "TARGET-HEALTH-CHANNEL-REF",
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
    class ContextRootSwComponentPrototypeRef(Ref):
        dest: RootSwComponentPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextComponentPrototypeRef(Ref):
        dest: SwComponentPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ContextRPortPrototypeRef(Ref):
        dest: RPortPrototypeSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class TargetHealthChannelRef(Ref):
        dest: PhmHealthChannelInterfaceSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
