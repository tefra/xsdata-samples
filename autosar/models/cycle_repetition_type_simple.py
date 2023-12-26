from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CycleRepetitionTypeSimple(Enum):
    """
    :cvar CYCLE_REPETITION_1: Attribute cycleRepetition value="1" valid
        only for FlexRay Protocol 2.1 Rev A
    :cvar CYCLE_REPETITION_10: Attribute cycleRepetition value="10" to
        support FlexRay 3.0
    :cvar CYCLE_REPETITION_16: Attribute cycleRepetition value="16"
        valid only for FlexRay Protocol 2.1 Rev A
    :cvar CYCLE_REPETITION_2: Attribute cycleRepetition value="2" valid
        only for FlexRay Protocol 2.1 Rev A
    :cvar CYCLE_REPETITION_20: Attribute cycleRepetition value="20" to
        support FlexRay 3.0
    :cvar CYCLE_REPETITION_32: Attribute cycleRepetition value="32"
        valid only for FlexRay Protocol 2.1 Rev A
    :cvar CYCLE_REPETITION_4: Attribute cycleRepetition value="4" valid
        only for FlexRay Protocol 2.1 Rev A
    :cvar CYCLE_REPETITION_40: Attribute cycleRepetition value="40" to
        support FlexRay 3.0
    :cvar CYCLE_REPETITION_5: Attribute cycleRepetition value="5" to
        support FlexRay 3.0
    :cvar CYCLE_REPETITION_50: Attribute cycleRepetition value="50" to
        support FlexRay 3.0
    :cvar CYCLE_REPETITION_64: Attribute cycleRepetition value="64"
        valid only for FlexRay Protocol 2.1 Rev A
    :cvar CYCLE_REPETITION_8: Attribute cycleRepetition value="8" valid
        only for FlexRay Protocol 2.1 Rev A
    """

    CYCLE_REPETITION_1 = "CYCLE-REPETITION-1"
    CYCLE_REPETITION_10 = "CYCLE-REPETITION-10"
    CYCLE_REPETITION_16 = "CYCLE-REPETITION-16"
    CYCLE_REPETITION_2 = "CYCLE-REPETITION-2"
    CYCLE_REPETITION_20 = "CYCLE-REPETITION-20"
    CYCLE_REPETITION_32 = "CYCLE-REPETITION-32"
    CYCLE_REPETITION_4 = "CYCLE-REPETITION-4"
    CYCLE_REPETITION_40 = "CYCLE-REPETITION-40"
    CYCLE_REPETITION_5 = "CYCLE-REPETITION-5"
    CYCLE_REPETITION_50 = "CYCLE-REPETITION-50"
    CYCLE_REPETITION_64 = "CYCLE-REPETITION-64"
    CYCLE_REPETITION_8 = "CYCLE-REPETITION-8"
