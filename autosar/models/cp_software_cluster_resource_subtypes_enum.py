from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CpSoftwareClusterResourceSubtypesEnum(StrEnum):
    CP_SOFTWARE_CLUSTER_COMMUNICATION_RESOURCE = (
        "CP-SOFTWARE-CLUSTER-COMMUNICATION-RESOURCE"
    )
    CP_SOFTWARE_CLUSTER_RESOURCE = "CP-SOFTWARE-CLUSTER-RESOURCE"
    CP_SOFTWARE_CLUSTER_SERVICE_RESOURCE = (
        "CP-SOFTWARE-CLUSTER-SERVICE-RESOURCE"
    )
