from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ServiceMethodDeploymentSubtypesEnum(StrEnum):
    SERVICE_METHOD_DEPLOYMENT = "SERVICE-METHOD-DEPLOYMENT"
    SOMEIP_METHOD_DEPLOYMENT = "SOMEIP-METHOD-DEPLOYMENT"
    USER_DEFINED_METHOD_DEPLOYMENT = "USER-DEFINED-METHOD-DEPLOYMENT"
