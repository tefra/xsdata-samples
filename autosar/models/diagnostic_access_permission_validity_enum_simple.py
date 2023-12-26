from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticAccessPermissionValidityEnumSimple(Enum):
    """
    :cvar ACCES_PERRMISSION_SERVICE_CLASS: This means that the
        DiagnosticServiceClass is in charge to define the
        accessPermission.
    :cvar ACCESS_PERMISSION_INSTANCE_OVERRIDES_CLASS: This means that
        accessPermission set at the DiagnosticServiceInstance will
        override the accessPermission defined at the
        DiagnosticServiceClass.
    :cvar ACCESS_PERMISSION_SERVICE_CLASS: This means that the
        DiagnosticServiceClass is in charge to define the
        accessPermission.
    :cvar ACCESS_PERMISSION_SERVICE_INSTANCE: This means that the
        DiagnosticServiceInstance is in charge of defining the
        accessPermission
    """

    ACCES_PERRMISSION_SERVICE_CLASS = "ACCES-PERRMISSION-SERVICE-CLASS"
    ACCESS_PERMISSION_INSTANCE_OVERRIDES_CLASS = (
        "ACCESS-PERMISSION-INSTANCE-OVERRIDES-CLASS"
    )
    ACCESS_PERMISSION_SERVICE_CLASS = "ACCESS-PERMISSION-SERVICE-CLASS"
    ACCESS_PERMISSION_SERVICE_INSTANCE = "ACCESS-PERMISSION-SERVICE-INSTANCE"
