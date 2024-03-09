from dataclasses import dataclass, field
from typing import Optional

from .boolean import Boolean

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class FlexrayNmEcu:
    """
    FlexRay specific attributes.

    :ivar nm_hw_vote_enabled: Switch for enabling the processing of
        FlexRay Hardware aggregated NM-Votes.
    :ivar nm_main_function_across_fr_cycle: Parameter describing if the
        execution of the FrNm_Main function crosses theFlexRay cycle
        boundary or not.
    :ivar nm_repeat_message_bit_enable: Enables/disables the repeat
        message bit support
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
        name = "FLEXRAY-NM-ECU"

    nm_hw_vote_enabled: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-HW-VOTE-ENABLED",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_main_function_across_fr_cycle: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-MAIN-FUNCTION-ACROSS-FR-CYCLE",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    nm_repeat_message_bit_enable: Optional[Boolean] = field(
        default=None,
        metadata={
            "name": "NM-REPEAT-MESSAGE-BIT-ENABLE",
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
