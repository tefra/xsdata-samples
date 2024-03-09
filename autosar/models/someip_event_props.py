from dataclasses import dataclass, field
from typing import Optional

from .ref import Ref
from .someip_collection_props import SomeipCollectionProps
from .someip_event_deployment_subtypes_enum import (
    SomeipEventDeploymentSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SomeipEventProps:
    """
    This meta-class allows to set configuration options for an event in the
    provided service instance.

    :ivar collection_props: Collection of timing attributes configurable
        for an event that is provided by a Service Instance.
    :ivar event_ref: Reference to the event for which the
        SomeipEventProps are applicable.
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
        name = "SOMEIP-EVENT-PROPS"

    collection_props: Optional[SomeipCollectionProps] = field(
        default=None,
        metadata={
            "name": "COLLECTION-PROPS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_ref: Optional["SomeipEventProps.EventRef"] = field(
        default=None,
        metadata={
            "name": "EVENT-REF",
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
    class EventRef(Ref):
        dest: Optional[SomeipEventDeploymentSubtypesEnum] = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
