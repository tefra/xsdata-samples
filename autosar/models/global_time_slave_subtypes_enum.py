from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class GlobalTimeSlaveSubtypesEnum(Enum):
    GLOBAL_TIME_CAN_SLAVE = "GLOBAL-TIME-CAN-SLAVE"
    GLOBAL_TIME_ETH_SLAVE = "GLOBAL-TIME-ETH-SLAVE"
    GLOBAL_TIME_FR_SLAVE = "GLOBAL-TIME-FR-SLAVE"
    GLOBAL_TIME_SLAVE = "GLOBAL-TIME-SLAVE"
    USER_DEFINED_GLOBAL_TIME_SLAVE = "USER-DEFINED-GLOBAL-TIME-SLAVE"