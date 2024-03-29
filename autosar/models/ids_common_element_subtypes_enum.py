from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class IdsCommonElementSubtypesEnum(Enum):
    IDS_COMMON_ELEMENT = "IDS-COMMON-ELEMENT"
    IDS_MAPPING = "IDS-MAPPING"
    IDSM_INSTANCE = "IDSM-INSTANCE"
    IDSM_PROPERTIES = "IDSM-PROPERTIES"
    SECURITY_EVENT_CONTEXT_MAPPING = "SECURITY-EVENT-CONTEXT-MAPPING"
    SECURITY_EVENT_CONTEXT_MAPPING_APPLICATION = (
        "SECURITY-EVENT-CONTEXT-MAPPING-APPLICATION"
    )
    SECURITY_EVENT_CONTEXT_MAPPING_BSW_MODULE = (
        "SECURITY-EVENT-CONTEXT-MAPPING-BSW-MODULE"
    )
    SECURITY_EVENT_CONTEXT_MAPPING_COMM_CONNECTOR = (
        "SECURITY-EVENT-CONTEXT-MAPPING-COMM-CONNECTOR"
    )
    SECURITY_EVENT_CONTEXT_MAPPING_FUNCTIONAL_CLUSTER = (
        "SECURITY-EVENT-CONTEXT-MAPPING-FUNCTIONAL-CLUSTER"
    )
    SECURITY_EVENT_DEFINITION = "SECURITY-EVENT-DEFINITION"
    SECURITY_EVENT_FILTER_CHAIN = "SECURITY-EVENT-FILTER-CHAIN"
