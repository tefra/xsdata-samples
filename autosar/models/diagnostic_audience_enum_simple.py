from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticAudienceEnumSimple(Enum):
    """
    :cvar AFTER_SALES: The object is relevant for the OEM after-sales
        organization.
    :cvar AFTERMAKET: The object is for free aftermarket service
        organizations.
    :cvar AFTERMARKET: The object is for free aftermarket service
        organizations.
    :cvar DEVELOPMENT: The object is relevant for engineering only.
    :cvar MANUFACTURING: The object is relevant for manufacturing.
    :cvar SUPPLIER: The object is relevant for the ECU-supplier
        aftermarket organization.
    """

    AFTER_SALES = "AFTER-SALES"
    AFTERMAKET = "AFTERMAKET"
    AFTERMARKET = "AFTERMARKET"
    DEVELOPMENT = "DEVELOPMENT"
    MANUFACTURING = "MANUFACTURING"
    SUPPLIER = "SUPPLIER"
