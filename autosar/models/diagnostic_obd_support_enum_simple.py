from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticObdSupportEnumSimple(Enum):
    """
    :cvar MASTER_ECU: This represent the role "master ECU".
    :cvar NO_OBD_SUPPORT: This represents the ability to explicitly
        specify that no participation in OBD is foreseen.
    :cvar PRIMARY_ECU: This represents the role "primary ECU".
    :cvar SECONDARY_ECU: This represents the role "secondary ECU".
    """
    MASTER_ECU = "MASTER-ECU"
    NO_OBD_SUPPORT = "NO-OBD-SUPPORT"
    PRIMARY_ECU = "PRIMARY-ECU"
    SECONDARY_ECU = "SECONDARY-ECU"
