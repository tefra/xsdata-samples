from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class NonOsModuleInstantiationSubtypesEnum(Enum):
    CRYPTO_MODULE_INSTANTIATION = "CRYPTO-MODULE-INSTANTIATION"
    DO_IP_INSTANTIATION = "DO-IP-INSTANTIATION"
    GENERIC_MODULE_INSTANTIATION = "GENERIC-MODULE-INSTANTIATION"
    IAM_MODULE_INSTANTIATION = "IAM-MODULE-INSTANTIATION"
    IDS_PLATFORM_INSTANTIATION = "IDS-PLATFORM-INSTANTIATION"
    IDSM_MODULE_INSTANTIATION = "IDSM-MODULE-INSTANTIATION"
    LOG_AND_TRACE_INSTANTIATION = "LOG-AND-TRACE-INSTANTIATION"
    NM_INSTANTIATION = "NM-INSTANTIATION"
    NON_OS_MODULE_INSTANTIATION = "NON-OS-MODULE-INSTANTIATION"
    TIME_SYNC_MODULE_INSTANTIATION = "TIME-SYNC-MODULE-INSTANTIATION"
    UCM_MODULE_INSTANTIATION = "UCM-MODULE-INSTANTIATION"
