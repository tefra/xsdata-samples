from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ServiceFieldDeploymentSubtypesEnum(Enum):
    DDS_FIELD_DEPLOYMENT = "DDS-FIELD-DEPLOYMENT"
    SERVICE_FIELD_DEPLOYMENT = "SERVICE-FIELD-DEPLOYMENT"
    SOMEIP_FIELD_DEPLOYMENT = "SOMEIP-FIELD-DEPLOYMENT"
    USER_DEFINED_FIELD_DEPLOYMENT = "USER-DEFINED-FIELD-DEPLOYMENT"
