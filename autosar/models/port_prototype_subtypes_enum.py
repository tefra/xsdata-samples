from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PortPrototypeSubtypesEnum(Enum):
    ABSTRACT_PROVIDED_PORT_PROTOTYPE = "ABSTRACT-PROVIDED-PORT-PROTOTYPE"
    ABSTRACT_REQUIRED_PORT_PROTOTYPE = "ABSTRACT-REQUIRED-PORT-PROTOTYPE"
    P_PORT_PROTOTYPE = "P-PORT-PROTOTYPE"
    PORT_PROTOTYPE = "PORT-PROTOTYPE"
    PR_PORT_PROTOTYPE = "PR-PORT-PROTOTYPE"
    R_PORT_PROTOTYPE = "R-PORT-PROTOTYPE"
