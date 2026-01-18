from __future__ import annotations

from dataclasses import dataclass, field

from .mode_driven_transmission_mode_condition import (
    ModeDrivenTransmissionModeCondition,
)
from .transmission_mode_condition import TransmissionModeCondition
from .transmission_mode_timing import TransmissionModeTiming

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


@dataclass
class TransmissionModeDeclaration:
    """
    AUTOSAR COM provides the possibility to define two different
    TRANSMISSION MODES (True and False) for each I-PDU.

    As TransmissionMode selector the signal content can be evaluated via
    transmissionModeCondition (implemented directly in the COM module) or
    mode conditions can be defined with the modeDrivenTrueCondition or
    modeDrivenFalseCondition (evaluated by BswM and invoking
    Com_SwitchIpduTxMode COM API). If modeDrivenTrueCondition and
    modeDrivenFalseCondition are defined they shall never evaluate to true
    both at the same time. The mixing of Transmission Mode Switch via API
    and signal value is not allowed.

    :ivar mode_driven_false_conditions: Defines the trigger for the
        Com_SwitchIpduTxMode Transmission Mode switch. Only if all
        defined modeDrivenFalseConditions evaluate to true (AND
        associated) the transmissionModeFalseTiming shall be activated.
        modeDrivenTrueCondition and modeDrivenFalseCondition shall never
        evaluate to true both at the same time.
    :ivar mode_driven_true_conditions: Defines the trigger for the
        Com_SwitchIpduTxMode Transmission Mode switch. Only if all
        defined modeDrivenTrueConditions evaluate to true (AND
        associated) the transmissionModeTrueTiming shall be activated.
        modeDrivenTrueCondition and modeDrivenFalseCondition shall never
        evaluate to true both at the same time.
    :ivar transmission_mode_conditions: The Transmission Mode Selector
        evaluates the conditions for a subset of signals and decides
        which transmission mode should be used. In case only one
        transmission mode is used there is no need for the
        "TransmissionModeCondition" and its sub-structure. In case the
        transmission mode shall be switched using the COM-API
        "Com_SwitchIpduTxMode" there is no need for the
        "TransmissionModeCondition" and its sub-structure.
    :ivar transmission_mode_false_timing: Timing Specification if the
        COM Transmission Mode is false. The Transmission Mode Selector
        is defined to be false, if all Conditions evaluate to false.
    :ivar transmission_mode_true_timing: Timing Specification if the COM
        Transmission Mode is true. The Transmission Mode Selector is
        defined to be true, if at least one Condition evaluates to true.
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
        name = "TRANSMISSION-MODE-DECLARATION"

    mode_driven_false_conditions: (
        None | TransmissionModeDeclaration.ModeDrivenFalseConditions
    ) = field(
        default=None,
        metadata={
            "name": "MODE-DRIVEN-FALSE-CONDITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    mode_driven_true_conditions: (
        None | TransmissionModeDeclaration.ModeDrivenTrueConditions
    ) = field(
        default=None,
        metadata={
            "name": "MODE-DRIVEN-TRUE-CONDITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmission_mode_conditions: (
        None | TransmissionModeDeclaration.TransmissionModeConditions
    ) = field(
        default=None,
        metadata={
            "name": "TRANSMISSION-MODE-CONDITIONS",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmission_mode_false_timing: None | TransmissionModeTiming = field(
        default=None,
        metadata={
            "name": "TRANSMISSION-MODE-FALSE-TIMING",
            "type": "Element",
            "namespace": "http://autosar.org/schema/r4.0",
        },
    )
    transmission_mode_true_timing: None | TransmissionModeTiming = field(
        default=None,
        metadata={
            "name": "TRANSMISSION-MODE-TRUE-TIMING",
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
    class ModeDrivenFalseConditions:
        mode_driven_transmission_mode_condition: list[
            ModeDrivenTransmissionModeCondition
        ] = field(
            default_factory=list,
            metadata={
                "name": "MODE-DRIVEN-TRANSMISSION-MODE-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class ModeDrivenTrueConditions:
        mode_driven_transmission_mode_condition: list[
            ModeDrivenTransmissionModeCondition
        ] = field(
            default_factory=list,
            metadata={
                "name": "MODE-DRIVEN-TRANSMISSION-MODE-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )

    @dataclass
    class TransmissionModeConditions:
        transmission_mode_condition: list[TransmissionModeCondition] = field(
            default_factory=list,
            metadata={
                "name": "TRANSMISSION-MODE-CONDITION",
                "type": "Element",
                "namespace": "http://autosar.org/schema/r4.0",
            },
        )
