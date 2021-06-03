from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ContainerIPduTriggerEnumSimple(Enum):
    """
    :cvar DEFAULT_TRIGGER: Defines that the transmission of the
        ContainerIPdu shall be requested when the default trigger
        conditions apply (e.g. timeout of threshold).
    :cvar FIRST_CONTAINED_TRIGGER: Defines that the transmission of the
        ContainerIPdu shall be requested right after the first
        ContainedIPdu was put into the ContainerIPdu.
    """
    DEFAULT_TRIGGER = "DEFAULT-TRIGGER"
    FIRST_CONTAINED_TRIGGER = "FIRST-CONTAINED-TRIGGER"
