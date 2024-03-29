from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class PortInterfaceSubtypesEnum(Enum):
    ABSTRACT_RAW_DATA_STREAM_INTERFACE = "ABSTRACT-RAW-DATA-STREAM-INTERFACE"
    ABSTRACT_SYNCHRONIZED_TIME_BASE_INTERFACE = (
        "ABSTRACT-SYNCHRONIZED-TIME-BASE-INTERFACE"
    )
    CLIENT_SERVER_INTERFACE = "CLIENT-SERVER-INTERFACE"
    COMPOSITE_INTERFACE = "COMPOSITE-INTERFACE"
    CRYPTO_CERTIFICATE_INTERFACE = "CRYPTO-CERTIFICATE-INTERFACE"
    CRYPTO_INTERFACE = "CRYPTO-INTERFACE"
    CRYPTO_KEY_SLOT_INTERFACE = "CRYPTO-KEY-SLOT-INTERFACE"
    CRYPTO_PROVIDER_INTERFACE = "CRYPTO-PROVIDER-INTERFACE"
    CRYPTO_TRUST_MASTER_INTERFACE = "CRYPTO-TRUST-MASTER-INTERFACE"
    DATA_INTERFACE = "DATA-INTERFACE"
    DIAGNOSTIC_ABSTRACT_DATA_IDENTIFIER_INTERFACE = (
        "DIAGNOSTIC-ABSTRACT-DATA-IDENTIFIER-INTERFACE"
    )
    DIAGNOSTIC_ABSTRACT_ROUTINE_INTERFACE = (
        "DIAGNOSTIC-ABSTRACT-ROUTINE-INTERFACE"
    )
    DIAGNOSTIC_CONDITION_INTERFACE = "DIAGNOSTIC-CONDITION-INTERFACE"
    DIAGNOSTIC_DATA_ELEMENT_INTERFACE = "DIAGNOSTIC-DATA-ELEMENT-INTERFACE"
    DIAGNOSTIC_DATA_IDENTIFIER_GENERIC_INTERFACE = (
        "DIAGNOSTIC-DATA-IDENTIFIER-GENERIC-INTERFACE"
    )
    DIAGNOSTIC_DATA_IDENTIFIER_INTERFACE = (
        "DIAGNOSTIC-DATA-IDENTIFIER-INTERFACE"
    )
    DIAGNOSTIC_DO_IP_ACTIVATION_LINE_INTERFACE = (
        "DIAGNOSTIC-DO-IP-ACTIVATION-LINE-INTERFACE"
    )
    DIAGNOSTIC_DO_IP_GROUP_IDENTIFICATION_INTERFACE = (
        "DIAGNOSTIC-DO-IP-GROUP-IDENTIFICATION-INTERFACE"
    )
    DIAGNOSTIC_DO_IP_POWER_MODE_INTERFACE = (
        "DIAGNOSTIC-DO-IP-POWER-MODE-INTERFACE"
    )
    DIAGNOSTIC_DO_IP_TRIGGER_VEHICLE_ANNOUNCEMENT_INTERFACE = (
        "DIAGNOSTIC-DO-IP-TRIGGER-VEHICLE-ANNOUNCEMENT-INTERFACE"
    )
    DIAGNOSTIC_DOWNLOAD_INTERFACE = "DIAGNOSTIC-DOWNLOAD-INTERFACE"
    DIAGNOSTIC_DTC_INFORMATION_INTERFACE = (
        "DIAGNOSTIC-DTC-INFORMATION-INTERFACE"
    )
    DIAGNOSTIC_ECU_RESET_INTERFACE = "DIAGNOSTIC-ECU-RESET-INTERFACE"
    DIAGNOSTIC_EVENT_INTERFACE = "DIAGNOSTIC-EVENT-INTERFACE"
    DIAGNOSTIC_GENERIC_UDS_INTERFACE = "DIAGNOSTIC-GENERIC-UDS-INTERFACE"
    DIAGNOSTIC_INDICATOR_INTERFACE = "DIAGNOSTIC-INDICATOR-INTERFACE"
    DIAGNOSTIC_MONITOR_INTERFACE = "DIAGNOSTIC-MONITOR-INTERFACE"
    DIAGNOSTIC_OPERATION_CYCLE_INTERFACE = (
        "DIAGNOSTIC-OPERATION-CYCLE-INTERFACE"
    )
    DIAGNOSTIC_PORT_INTERFACE = "DIAGNOSTIC-PORT-INTERFACE"
    DIAGNOSTIC_ROUTINE_GENERIC_INTERFACE = (
        "DIAGNOSTIC-ROUTINE-GENERIC-INTERFACE"
    )
    DIAGNOSTIC_ROUTINE_INTERFACE = "DIAGNOSTIC-ROUTINE-INTERFACE"
    DIAGNOSTIC_SECURITY_LEVEL_INTERFACE = "DIAGNOSTIC-SECURITY-LEVEL-INTERFACE"
    DIAGNOSTIC_SERVICE_VALIDATION_INTERFACE = (
        "DIAGNOSTIC-SERVICE-VALIDATION-INTERFACE"
    )
    DIAGNOSTIC_UPLOAD_INTERFACE = "DIAGNOSTIC-UPLOAD-INTERFACE"
    MODE_SWITCH_INTERFACE = "MODE-SWITCH-INTERFACE"
    NV_DATA_INTERFACE = "NV-DATA-INTERFACE"
    PARAMETER_INTERFACE = "PARAMETER-INTERFACE"
    PERSISTENCY_FILE_STORAGE_INTERFACE = "PERSISTENCY-FILE-STORAGE-INTERFACE"
    PERSISTENCY_INTERFACE = "PERSISTENCY-INTERFACE"
    PERSISTENCY_KEY_VALUE_STORAGE_INTERFACE = (
        "PERSISTENCY-KEY-VALUE-STORAGE-INTERFACE"
    )
    PHM_ABSTRACT_RECOVERY_NOTIFICATION_INTERFACE = (
        "PHM-ABSTRACT-RECOVERY-NOTIFICATION-INTERFACE"
    )
    PHM_HEALTH_CHANNEL_INTERFACE = "PHM-HEALTH-CHANNEL-INTERFACE"
    PHM_HEALTH_CHANNEL_RECOVERY_NOTIFICATION_INTERFACE = (
        "PHM-HEALTH-CHANNEL-RECOVERY-NOTIFICATION-INTERFACE"
    )
    PHM_RECOVERY_ACTION_INTERFACE = "PHM-RECOVERY-ACTION-INTERFACE"
    PHM_SUPERVISED_ENTITY_INTERFACE = "PHM-SUPERVISED-ENTITY-INTERFACE"
    PHM_SUPERVISION_RECOVERY_NOTIFICATION_INTERFACE = (
        "PHM-SUPERVISION-RECOVERY-NOTIFICATION-INTERFACE"
    )
    PLATFORM_HEALTH_MANAGEMENT_INTERFACE = (
        "PLATFORM-HEALTH-MANAGEMENT-INTERFACE"
    )
    PORT_INTERFACE = "PORT-INTERFACE"
    RAW_DATA_STREAM_CLIENT_INTERFACE = "RAW-DATA-STREAM-CLIENT-INTERFACE"
    RAW_DATA_STREAM_SERVER_INTERFACE = "RAW-DATA-STREAM-SERVER-INTERFACE"
    REST_SERVICE_INTERFACE = "REST-SERVICE-INTERFACE"
    SECURITY_EVENT_REPORT_INTERFACE = "SECURITY-EVENT-REPORT-INTERFACE"
    SENDER_RECEIVER_INTERFACE = "SENDER-RECEIVER-INTERFACE"
    SERVICE_INTERFACE = "SERVICE-INTERFACE"
    SYNCHRONIZED_TIME_BASE_CONSUMER_INTERFACE = (
        "SYNCHRONIZED-TIME-BASE-CONSUMER-INTERFACE"
    )
    SYNCHRONIZED_TIME_BASE_PROVIDER_INTERFACE = (
        "SYNCHRONIZED-TIME-BASE-PROVIDER-INTERFACE"
    )
    TRIGGER_INTERFACE = "TRIGGER-INTERFACE"
