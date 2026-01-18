from __future__ import annotations

from dataclasses import dataclass, field

from .admin_data import VariationPoint
from .ref import Ref
from .someip_sd_server_event_group_timing_config_subtypes_enum import (
    SomeipSdServerEventGroupTimingConfigSubtypesEnum,
)

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass(kw_only=True)
class SomeipSdServerEventGroupTimingConfigRefConditional:
    """
    This element was generated/modified due to an atpVariation stereotype.

    :ivar someip_sd_server_event_group_timing_config_ref:
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
        name = "SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF-CONDITIONAL"

    someip_sd_server_event_group_timing_config_ref: (
        None
        | SomeipSdServerEventGroupTimingConfigRefConditional.SomeipSdServerEventGroupTimingConfigRef
    ) = field(
        default=None,
        metadata={
            "name": "SOMEIP-SD-SERVER-EVENT-GROUP-TIMING-CONFIG-REF",
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

    @dataclass(kw_only=True)
    class SomeipSdServerEventGroupTimingConfigRef(Ref):
        dest: SomeipSdServerEventGroupTimingConfigSubtypesEnum = field(
            metadata={
                "name": "DEST",
                "type": "Attribute",
                "required": True,
            }
        )
