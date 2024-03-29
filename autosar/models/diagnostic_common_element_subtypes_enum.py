from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticCommonElementSubtypesEnum(Enum):
    DIAGNOSTIC_ABSTRACT_ALIAS_EVENT = "DIAGNOSTIC-ABSTRACT-ALIAS-EVENT"
    DIAGNOSTIC_ABSTRACT_DATA_IDENTIFIER = "DIAGNOSTIC-ABSTRACT-DATA-IDENTIFIER"
    DIAGNOSTIC_ACCESS_PERMISSION = "DIAGNOSTIC-ACCESS-PERMISSION"
    DIAGNOSTIC_AGING = "DIAGNOSTIC-AGING"
    DIAGNOSTIC_CLEAR_CONDITION = "DIAGNOSTIC-CLEAR-CONDITION"
    DIAGNOSTIC_CLEAR_CONDITION_GROUP = "DIAGNOSTIC-CLEAR-CONDITION-GROUP"
    DIAGNOSTIC_CLEAR_CONDITION_PORT_MAPPING = (
        "DIAGNOSTIC-CLEAR-CONDITION-PORT-MAPPING"
    )
    DIAGNOSTIC_CLEAR_DIAGNOSTIC_INFORMATION = (
        "DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION"
    )
    DIAGNOSTIC_CLEAR_DIAGNOSTIC_INFORMATION_CLASS = (
        "DIAGNOSTIC-CLEAR-DIAGNOSTIC-INFORMATION-CLASS"
    )
    DIAGNOSTIC_CLEAR_RESET_EMISSION_RELATED_INFO = (
        "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO"
    )
    DIAGNOSTIC_CLEAR_RESET_EMISSION_RELATED_INFO_CLASS = (
        "DIAGNOSTIC-CLEAR-RESET-EMISSION-RELATED-INFO-CLASS"
    )
    DIAGNOSTIC_COM_CONTROL = "DIAGNOSTIC-COM-CONTROL"
    DIAGNOSTIC_COM_CONTROL_CLASS = "DIAGNOSTIC-COM-CONTROL-CLASS"
    DIAGNOSTIC_COMMON_ELEMENT = "DIAGNOSTIC-COMMON-ELEMENT"
    DIAGNOSTIC_CONDITION = "DIAGNOSTIC-CONDITION"
    DIAGNOSTIC_CONDITION_GROUP = "DIAGNOSTIC-CONDITION-GROUP"
    DIAGNOSTIC_CONTROL_DTC_SETTING = "DIAGNOSTIC-CONTROL-DTC-SETTING"
    DIAGNOSTIC_CONTROL_DTC_SETTING_CLASS = (
        "DIAGNOSTIC-CONTROL-DTC-SETTING-CLASS"
    )
    DIAGNOSTIC_CUSTOM_SERVICE_CLASS = "DIAGNOSTIC-CUSTOM-SERVICE-CLASS"
    DIAGNOSTIC_CUSTOM_SERVICE_INSTANCE = "DIAGNOSTIC-CUSTOM-SERVICE-INSTANCE"
    DIAGNOSTIC_DATA_BY_IDENTIFIER = "DIAGNOSTIC-DATA-BY-IDENTIFIER"
    DIAGNOSTIC_DATA_IDENTIFIER = "DIAGNOSTIC-DATA-IDENTIFIER"
    DIAGNOSTIC_DATA_IDENTIFIER_SET = "DIAGNOSTIC-DATA-IDENTIFIER-SET"
    DIAGNOSTIC_DATA_TRANSFER = "DIAGNOSTIC-DATA-TRANSFER"
    DIAGNOSTIC_DATA_TRANSFER_CLASS = "DIAGNOSTIC-DATA-TRANSFER-CLASS"
    DIAGNOSTIC_DEM_PROVIDED_DATA_MAPPING = (
        "DIAGNOSTIC-DEM-PROVIDED-DATA-MAPPING"
    )
    DIAGNOSTIC_DYNAMIC_DATA_IDENTIFIER = "DIAGNOSTIC-DYNAMIC-DATA-IDENTIFIER"
    DIAGNOSTIC_DYNAMICALLY_DEFINE_DATA_IDENTIFIER = (
        "DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER"
    )
    DIAGNOSTIC_DYNAMICALLY_DEFINE_DATA_IDENTIFIER_CLASS = (
        "DIAGNOSTIC-DYNAMICALLY-DEFINE-DATA-IDENTIFIER-CLASS"
    )
    DIAGNOSTIC_ECU_INSTANCE_PROPS = "DIAGNOSTIC-ECU-INSTANCE-PROPS"
    DIAGNOSTIC_ECU_RESET = "DIAGNOSTIC-ECU-RESET"
    DIAGNOSTIC_ECU_RESET_CLASS = "DIAGNOSTIC-ECU-RESET-CLASS"
    DIAGNOSTIC_ENABLE_CONDITION = "DIAGNOSTIC-ENABLE-CONDITION"
    DIAGNOSTIC_ENABLE_CONDITION_GROUP = "DIAGNOSTIC-ENABLE-CONDITION-GROUP"
    DIAGNOSTIC_ENABLE_CONDITION_PORT_MAPPING = (
        "DIAGNOSTIC-ENABLE-CONDITION-PORT-MAPPING"
    )
    DIAGNOSTIC_ENVIRONMENTAL_CONDITION = "DIAGNOSTIC-ENVIRONMENTAL-CONDITION"
    DIAGNOSTIC_EVENT = "DIAGNOSTIC-EVENT"
    DIAGNOSTIC_EVENT_PORT_MAPPING = "DIAGNOSTIC-EVENT-PORT-MAPPING"
    DIAGNOSTIC_EVENT_TO_DEBOUNCE_ALGORITHM_MAPPING = (
        "DIAGNOSTIC-EVENT-TO-DEBOUNCE-ALGORITHM-MAPPING"
    )
    DIAGNOSTIC_EVENT_TO_ENABLE_CONDITION_GROUP_MAPPING = (
        "DIAGNOSTIC-EVENT-TO-ENABLE-CONDITION-GROUP-MAPPING"
    )
    DIAGNOSTIC_EVENT_TO_OPERATION_CYCLE_MAPPING = (
        "DIAGNOSTIC-EVENT-TO-OPERATION-CYCLE-MAPPING"
    )
    DIAGNOSTIC_EVENT_TO_SECURITY_EVENT_MAPPING = (
        "DIAGNOSTIC-EVENT-TO-SECURITY-EVENT-MAPPING"
    )
    DIAGNOSTIC_EVENT_TO_STORAGE_CONDITION_GROUP_MAPPING = (
        "DIAGNOSTIC-EVENT-TO-STORAGE-CONDITION-GROUP-MAPPING"
    )
    DIAGNOSTIC_EVENT_TO_TROUBLE_CODE_J_1939_MAPPING = (
        "DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-J-1939-MAPPING"
    )
    DIAGNOSTIC_EVENT_TO_TROUBLE_CODE_UDS_MAPPING = (
        "DIAGNOSTIC-EVENT-TO-TROUBLE-CODE-UDS-MAPPING"
    )
    DIAGNOSTIC_EXTENDED_DATA_RECORD = "DIAGNOSTIC-EXTENDED-DATA-RECORD"
    DIAGNOSTIC_FIM_ALIAS_EVENT = "DIAGNOSTIC-FIM-ALIAS-EVENT"
    DIAGNOSTIC_FIM_ALIAS_EVENT_GROUP = "DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP"
    DIAGNOSTIC_FIM_ALIAS_EVENT_GROUP_MAPPING = (
        "DIAGNOSTIC-FIM-ALIAS-EVENT-GROUP-MAPPING"
    )
    DIAGNOSTIC_FIM_ALIAS_EVENT_MAPPING = "DIAGNOSTIC-FIM-ALIAS-EVENT-MAPPING"
    DIAGNOSTIC_FIM_EVENT_GROUP = "DIAGNOSTIC-FIM-EVENT-GROUP"
    DIAGNOSTIC_FIM_FUNCTION_MAPPING = "DIAGNOSTIC-FIM-FUNCTION-MAPPING"
    DIAGNOSTIC_FREEZE_FRAME = "DIAGNOSTIC-FREEZE-FRAME"
    DIAGNOSTIC_FUNCTION_IDENTIFIER = "DIAGNOSTIC-FUNCTION-IDENTIFIER"
    DIAGNOSTIC_FUNCTION_IDENTIFIER_INHIBIT = (
        "DIAGNOSTIC-FUNCTION-IDENTIFIER-INHIBIT"
    )
    DIAGNOSTIC_INDICATOR = "DIAGNOSTIC-INDICATOR"
    DIAGNOSTIC_INDICATOR_PORT_MAPPING = "DIAGNOSTIC-INDICATOR-PORT-MAPPING"
    DIAGNOSTIC_INFO_TYPE = "DIAGNOSTIC-INFO-TYPE"
    DIAGNOSTIC_INHIBIT_SOURCE_EVENT_MAPPING = (
        "DIAGNOSTIC-INHIBIT-SOURCE-EVENT-MAPPING"
    )
    DIAGNOSTIC_IO_CONTROL = "DIAGNOSTIC-IO-CONTROL"
    DIAGNOSTIC_IO_CONTROL_CLASS = "DIAGNOSTIC-IO-CONTROL-CLASS"
    DIAGNOSTIC_IUMPR = "DIAGNOSTIC-IUMPR"
    DIAGNOSTIC_IUMPR_DENOMINATOR_GROUP = "DIAGNOSTIC-IUMPR-DENOMINATOR-GROUP"
    DIAGNOSTIC_IUMPR_GROUP = "DIAGNOSTIC-IUMPR-GROUP"
    DIAGNOSTIC_J_1939_EXPANDED_FREEZE_FRAME = (
        "DIAGNOSTIC-J-1939-EXPANDED-FREEZE-FRAME"
    )
    DIAGNOSTIC_J_1939_FREEZE_FRAME = "DIAGNOSTIC-J-1939-FREEZE-FRAME"
    DIAGNOSTIC_J_1939_NODE = "DIAGNOSTIC-J-1939-NODE"
    DIAGNOSTIC_J_1939_SPN = "DIAGNOSTIC-J-1939-SPN"
    DIAGNOSTIC_J_1939_SPN_MAPPING = "DIAGNOSTIC-J-1939-SPN-MAPPING"
    DIAGNOSTIC_J_1939_SW_MAPPING = "DIAGNOSTIC-J-1939-SW-MAPPING"
    DIAGNOSTIC_MAPPING = "DIAGNOSTIC-MAPPING"
    DIAGNOSTIC_MASTER_TO_SLAVE_EVENT_MAPPING = (
        "DIAGNOSTIC-MASTER-TO-SLAVE-EVENT-MAPPING"
    )
    DIAGNOSTIC_MEASUREMENT_IDENTIFIER = "DIAGNOSTIC-MEASUREMENT-IDENTIFIER"
    DIAGNOSTIC_MEMORY_ADDRESSABLE_RANGE_ACCESS = (
        "DIAGNOSTIC-MEMORY-ADDRESSABLE-RANGE-ACCESS"
    )
    DIAGNOSTIC_MEMORY_BY_ADDRESS = "DIAGNOSTIC-MEMORY-BY-ADDRESS"
    DIAGNOSTIC_MEMORY_DESTINATION = "DIAGNOSTIC-MEMORY-DESTINATION"
    DIAGNOSTIC_MEMORY_DESTINATION_MIRROR = (
        "DIAGNOSTIC-MEMORY-DESTINATION-MIRROR"
    )
    DIAGNOSTIC_MEMORY_DESTINATION_PORT_MAPPING = (
        "DIAGNOSTIC-MEMORY-DESTINATION-PORT-MAPPING"
    )
    DIAGNOSTIC_MEMORY_DESTINATION_PRIMARY = (
        "DIAGNOSTIC-MEMORY-DESTINATION-PRIMARY"
    )
    DIAGNOSTIC_MEMORY_DESTINATION_USER_DEFINED = (
        "DIAGNOSTIC-MEMORY-DESTINATION-USER-DEFINED"
    )
    DIAGNOSTIC_MEMORY_IDENTIFIER = "DIAGNOSTIC-MEMORY-IDENTIFIER"
    DIAGNOSTIC_OPERATION_CYCLE = "DIAGNOSTIC-OPERATION-CYCLE"
    DIAGNOSTIC_OPERATION_CYCLE_PORT_MAPPING = (
        "DIAGNOSTIC-OPERATION-CYCLE-PORT-MAPPING"
    )
    DIAGNOSTIC_PARAMETER_IDENTIFIER = "DIAGNOSTIC-PARAMETER-IDENTIFIER"
    DIAGNOSTIC_POWERTRAIN_FREEZE_FRAME = "DIAGNOSTIC-POWERTRAIN-FREEZE-FRAME"
    DIAGNOSTIC_PROTOCOL = "DIAGNOSTIC-PROTOCOL"
    DIAGNOSTIC_PROVIDED_DATA_MAPPING = "DIAGNOSTIC-PROVIDED-DATA-MAPPING"
    DIAGNOSTIC_READ_DATA_BY_IDENTIFIER = "DIAGNOSTIC-READ-DATA-BY-IDENTIFIER"
    DIAGNOSTIC_READ_DATA_BY_IDENTIFIER_CLASS = (
        "DIAGNOSTIC-READ-DATA-BY-IDENTIFIER-CLASS"
    )
    DIAGNOSTIC_READ_DATA_BY_PERIODIC_ID = "DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID"
    DIAGNOSTIC_READ_DATA_BY_PERIODIC_ID_CLASS = (
        "DIAGNOSTIC-READ-DATA-BY-PERIODIC-ID-CLASS"
    )
    DIAGNOSTIC_READ_DTC_INFORMATION = "DIAGNOSTIC-READ-DTC-INFORMATION"
    DIAGNOSTIC_READ_DTC_INFORMATION_CLASS = (
        "DIAGNOSTIC-READ-DTC-INFORMATION-CLASS"
    )
    DIAGNOSTIC_READ_MEMORY_BY_ADDRESS = "DIAGNOSTIC-READ-MEMORY-BY-ADDRESS"
    DIAGNOSTIC_READ_MEMORY_BY_ADDRESS_CLASS = (
        "DIAGNOSTIC-READ-MEMORY-BY-ADDRESS-CLASS"
    )
    DIAGNOSTIC_READ_SCALING_DATA_BY_IDENTIFIER = (
        "DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER"
    )
    DIAGNOSTIC_READ_SCALING_DATA_BY_IDENTIFIER_CLASS = (
        "DIAGNOSTIC-READ-SCALING-DATA-BY-IDENTIFIER-CLASS"
    )
    DIAGNOSTIC_REQUEST_CONTROL_OF_ON_BOARD_DEVICE = (
        "DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE"
    )
    DIAGNOSTIC_REQUEST_CONTROL_OF_ON_BOARD_DEVICE_CLASS = (
        "DIAGNOSTIC-REQUEST-CONTROL-OF-ON-BOARD-DEVICE-CLASS"
    )
    DIAGNOSTIC_REQUEST_CURRENT_POWERTRAIN_DATA = (
        "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA"
    )
    DIAGNOSTIC_REQUEST_CURRENT_POWERTRAIN_DATA_CLASS = (
        "DIAGNOSTIC-REQUEST-CURRENT-POWERTRAIN-DATA-CLASS"
    )
    DIAGNOSTIC_REQUEST_DOWNLOAD = "DIAGNOSTIC-REQUEST-DOWNLOAD"
    DIAGNOSTIC_REQUEST_DOWNLOAD_CLASS = "DIAGNOSTIC-REQUEST-DOWNLOAD-CLASS"
    DIAGNOSTIC_REQUEST_EMISSION_RELATED_DTC = (
        "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC"
    )
    DIAGNOSTIC_REQUEST_EMISSION_RELATED_DTC_CLASS = (
        "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-CLASS"
    )
    DIAGNOSTIC_REQUEST_EMISSION_RELATED_DTC_PERMANENT_STATUS = (
        "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS"
    )
    DIAGNOSTIC_REQUEST_EMISSION_RELATED_DTC_PERMANENT_STATUS_CLASS = (
        "DIAGNOSTIC-REQUEST-EMISSION-RELATED-DTC-PERMANENT-STATUS-CLASS"
    )
    DIAGNOSTIC_REQUEST_FILE_TRANSFER = "DIAGNOSTIC-REQUEST-FILE-TRANSFER"
    DIAGNOSTIC_REQUEST_FILE_TRANSFER_CLASS = (
        "DIAGNOSTIC-REQUEST-FILE-TRANSFER-CLASS"
    )
    DIAGNOSTIC_REQUEST_ON_BOARD_MONITORING_TEST_RESULTS = (
        "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS"
    )
    DIAGNOSTIC_REQUEST_ON_BOARD_MONITORING_TEST_RESULTS_CLASS = (
        "DIAGNOSTIC-REQUEST-ON-BOARD-MONITORING-TEST-RESULTS-CLASS"
    )
    DIAGNOSTIC_REQUEST_POWERTRAIN_FREEZE_FRAME_DATA = (
        "DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA"
    )
    DIAGNOSTIC_REQUEST_POWERTRAIN_FREEZE_FRAME_DATA_CLASS = (
        "DIAGNOSTIC-REQUEST-POWERTRAIN-FREEZE-FRAME-DATA-CLASS"
    )
    DIAGNOSTIC_REQUEST_UPLOAD = "DIAGNOSTIC-REQUEST-UPLOAD"
    DIAGNOSTIC_REQUEST_UPLOAD_CLASS = "DIAGNOSTIC-REQUEST-UPLOAD-CLASS"
    DIAGNOSTIC_REQUEST_VEHICLE_INFO = "DIAGNOSTIC-REQUEST-VEHICLE-INFO"
    DIAGNOSTIC_REQUEST_VEHICLE_INFO_CLASS = (
        "DIAGNOSTIC-REQUEST-VEHICLE-INFO-CLASS"
    )
    DIAGNOSTIC_RESPONSE_ON_EVENT = "DIAGNOSTIC-RESPONSE-ON-EVENT"
    DIAGNOSTIC_RESPONSE_ON_EVENT_CLASS = "DIAGNOSTIC-RESPONSE-ON-EVENT-CLASS"
    DIAGNOSTIC_ROUTINE = "DIAGNOSTIC-ROUTINE"
    DIAGNOSTIC_ROUTINE_CONTROL = "DIAGNOSTIC-ROUTINE-CONTROL"
    DIAGNOSTIC_ROUTINE_CONTROL_CLASS = "DIAGNOSTIC-ROUTINE-CONTROL-CLASS"
    DIAGNOSTIC_SECURITY_ACCESS = "DIAGNOSTIC-SECURITY-ACCESS"
    DIAGNOSTIC_SECURITY_ACCESS_CLASS = "DIAGNOSTIC-SECURITY-ACCESS-CLASS"
    DIAGNOSTIC_SECURITY_EVENT_REPORTING_MODE_MAPPING = (
        "DIAGNOSTIC-SECURITY-EVENT-REPORTING-MODE-MAPPING"
    )
    DIAGNOSTIC_SECURITY_LEVEL = "DIAGNOSTIC-SECURITY-LEVEL"
    DIAGNOSTIC_SECURITY_LEVEL_PORT_MAPPING = (
        "DIAGNOSTIC-SECURITY-LEVEL-PORT-MAPPING"
    )
    DIAGNOSTIC_SERVICE_CLASS = "DIAGNOSTIC-SERVICE-CLASS"
    DIAGNOSTIC_SERVICE_DATA_IDENTIFIER_PORT_MAPPING = (
        "DIAGNOSTIC-SERVICE-DATA-IDENTIFIER-PORT-MAPPING"
    )
    DIAGNOSTIC_SERVICE_DATA_MAPPING = "DIAGNOSTIC-SERVICE-DATA-MAPPING"
    DIAGNOSTIC_SERVICE_GENERIC_MAPPING = "DIAGNOSTIC-SERVICE-GENERIC-MAPPING"
    DIAGNOSTIC_SERVICE_INSTANCE = "DIAGNOSTIC-SERVICE-INSTANCE"
    DIAGNOSTIC_SERVICE_SW_MAPPING = "DIAGNOSTIC-SERVICE-SW-MAPPING"
    DIAGNOSTIC_SERVICE_TABLE = "DIAGNOSTIC-SERVICE-TABLE"
    DIAGNOSTIC_SESSION = "DIAGNOSTIC-SESSION"
    DIAGNOSTIC_SESSION_CONTROL = "DIAGNOSTIC-SESSION-CONTROL"
    DIAGNOSTIC_SESSION_CONTROL_CLASS = "DIAGNOSTIC-SESSION-CONTROL-CLASS"
    DIAGNOSTIC_SOFTWARE_CLUSTER_PROPS = "DIAGNOSTIC-SOFTWARE-CLUSTER-PROPS"
    DIAGNOSTIC_STORAGE_CONDITION = "DIAGNOSTIC-STORAGE-CONDITION"
    DIAGNOSTIC_STORAGE_CONDITION_GROUP = "DIAGNOSTIC-STORAGE-CONDITION-GROUP"
    DIAGNOSTIC_STORAGE_CONDITION_PORT_MAPPING = (
        "DIAGNOSTIC-STORAGE-CONDITION-PORT-MAPPING"
    )
    DIAGNOSTIC_SW_MAPPING = "DIAGNOSTIC-SW-MAPPING"
    DIAGNOSTIC_TEST_RESULT = "DIAGNOSTIC-TEST-RESULT"
    DIAGNOSTIC_TEST_ROUTINE_IDENTIFIER = "DIAGNOSTIC-TEST-ROUTINE-IDENTIFIER"
    DIAGNOSTIC_TRANSFER_EXIT = "DIAGNOSTIC-TRANSFER-EXIT"
    DIAGNOSTIC_TRANSFER_EXIT_CLASS = "DIAGNOSTIC-TRANSFER-EXIT-CLASS"
    DIAGNOSTIC_TROUBLE_CODE = "DIAGNOSTIC-TROUBLE-CODE"
    DIAGNOSTIC_TROUBLE_CODE_GROUP = "DIAGNOSTIC-TROUBLE-CODE-GROUP"
    DIAGNOSTIC_TROUBLE_CODE_J_1939 = "DIAGNOSTIC-TROUBLE-CODE-J-1939"
    DIAGNOSTIC_TROUBLE_CODE_OBD = "DIAGNOSTIC-TROUBLE-CODE-OBD"
    DIAGNOSTIC_TROUBLE_CODE_PROPS = "DIAGNOSTIC-TROUBLE-CODE-PROPS"
    DIAGNOSTIC_TROUBLE_CODE_UDS = "DIAGNOSTIC-TROUBLE-CODE-UDS"
    DIAGNOSTIC_TROUBLE_CODE_UDS_TO_CLEAR_CONDITION_GROUP_MAPPING = (
        "DIAGNOSTIC-TROUBLE-CODE-UDS-TO-CLEAR-CONDITION-GROUP-MAPPING"
    )
    DIAGNOSTIC_TROUBLE_CODE_UDS_TO_TROUBLE_CODE_OBD_MAPPING = (
        "DIAGNOSTIC-TROUBLE-CODE-UDS-TO-TROUBLE-CODE-OBD-MAPPING"
    )
    DIAGNOSTIC_WRITE_DATA_BY_IDENTIFIER = "DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER"
    DIAGNOSTIC_WRITE_DATA_BY_IDENTIFIER_CLASS = (
        "DIAGNOSTIC-WRITE-DATA-BY-IDENTIFIER-CLASS"
    )
    DIAGNOSTIC_WRITE_MEMORY_BY_ADDRESS = "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS"
    DIAGNOSTIC_WRITE_MEMORY_BY_ADDRESS_CLASS = (
        "DIAGNOSTIC-WRITE-MEMORY-BY-ADDRESS-CLASS"
    )
