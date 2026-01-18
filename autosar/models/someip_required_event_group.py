from __future__ import annotations

from dataclasses import dataclass, field

from .identifier import Identifier
from .ref import Ref
from .short_name_fragment import ShortNameFragment
from .someip_event_group_subtypes_enum import SomeipEventGroupSubtypesEnum
from .someip_sd_client_event_group_timing_config_subtypes_enum import (
    SomeipSdClientEventGroupTimingConfigSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class SomeipRequiredEventGroup:
    """
    The meta-class represents the ability to configure ServiceInstance
    related communication settings on the required side for each EventGroup
    separately.

    :ivar short_name: This specifies an identifying shortName for the
        object. It needs to be unique within its context and is intended
        for humans but even more for technical reference.
    :ivar short_name_fragments: This specifies how the
        Referrable.shortName is composed of several shortNameFragments.
    :ivar event_group_ref: Reference to the SomeipEventGroup in the
        System Manifest for which the ServiceInstance related EventGroup
        settings are valid.
    :ivar sd_client_event_group_timing_config_ref: Client Timing
        configuration settings that are EventGroup specific.
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
        name = "SOMEIP-REQUIRED-EVENT-GROUP"

    short_name: None | Identifier = field(
        default=None,
        metadata={
            "name": "SHORT-NAME",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
            "required": True,
        },
    )
    short_name_fragments: (
        None | SomeipRequiredEventGroup.ShortNameFragments
    ) = field(
        default=None,
        metadata={
            "name": "SHORT-NAME-FRAGMENTS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    event_group_ref: None | SomeipRequiredEventGroup.EventGroupRef = field(
        default=None,
        metadata={
            "name": "EVENT-GROUP-REF",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    sd_client_event_group_timing_config_ref: (
        None | SomeipRequiredEventGroup.SdClientEventGroupTimingConfigRef
    ) = field(
        default=None,
        metadata={
            "name": "SD-CLIENT-EVENT-GROUP-TIMING-CONFIG-REF",
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
    class ShortNameFragments:
        short_name_fragment: list[ShortNameFragment] = field(
            default_factory=list,
            metadata={
                "name": "SHORT-NAME-FRAGMENT",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class EventGroupRef(Ref):
        dest: None | SomeipEventGroupSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )

    @dataclass
    class SdClientEventGroupTimingConfigRef(Ref):
        dest: None | SomeipSdClientEventGroupTimingConfigSubtypesEnum = field(
            default=None,
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            },
        )
