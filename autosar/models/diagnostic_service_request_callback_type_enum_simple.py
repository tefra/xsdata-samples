from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticServiceRequestCallbackTypeEnumSimple(Enum):
    """
    :cvar REQUEST_CALLBACK_TYPE_MANUFACTURER: This represents the case
        that the usage of PortInterface ServiceRequestNotification has
        the characteristics of being used by a manufacturer.
    :cvar REQUEST_CALLBACK_TYPE_SUPPLIER: This represents the case that
        the usage of PortInterface ServiceRequestNotification has the
        characteristics of being used by a supplier.
    """

    REQUEST_CALLBACK_TYPE_MANUFACTURER = "REQUEST-CALLBACK-TYPE-MANUFACTURER"
    REQUEST_CALLBACK_TYPE_SUPPLIER = "REQUEST-CALLBACK-TYPE-SUPPLIER"
