from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class SecureComPropsSubtypesEnum(Enum):
    SEC_OC_SECURE_COM_PROPS = "SEC-OC-SECURE-COM-PROPS"
    SECURE_COM_PROPS = "SECURE-COM-PROPS"
    TLS_SECURE_COM_PROPS = "TLS-SECURE-COM-PROPS"
