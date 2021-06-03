from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class ServiceProviderEnumSimple(Enum):
    """
    :cvar ANY_STANDARDIZED: This value means that the specific nature is
        either unknown or it is not important for the given purpose.
        This is also the default value for any attribute of type
        ServiceProviderEnum
    :cvar BASIC_SOFTWARE_MODE_MANAGER: The service relates to the Basic
        Software Mode Manager (BswM)
    :cvar COM_MANAGER: The service relates to the COM Manager (ComM).
    :cvar CRYPTO_SERVICE_MANAGER: The service relates to the Crypto
        Service Manager (CsM).
    :cvar DEFAULT_ERROR_TRACER: The service relates to the Default Error
        Tracer (DET)
    :cvar DEVELOPMENT_ERROR_TRACER: The service relates to the
        Development Error Tracer (DET).
    :cvar DIAGNOSTIC_COMMUNICATION_MANAGER: The service relates to the
        Diagnostic Communication Manager (DCM).
    :cvar DIAGNOSTIC_EVENT_MANAGER: The service relates to the
        Diagnostic Event Manager (DEM).
    :cvar DIAGNOSTIC_LOG_AND_TRACE: The service relates to the
        Diagnostic Log and Trace (DLT).
    :cvar ECU_MANAGER: The service relates to the ECU Manager (EcuM).
    :cvar ERROR_TRACER: This service relates to the error tracer.
    :cvar FUNCTION_INHIBITION_MANAGER: The service relates to the
        Function Inhibition Manager (FIM).
    :cvar HARDWARE_TEST_MANAGER: This service relates to the hardware
        test manager.
    :cvar J_1939_DCM:
    :cvar J_1939_REQUEST_MANAGER: The service relates to the J1939Rm.
    :cvar NON_VOLATILE_RAM_MANAGER: The service relates to the Non-
        Volatile RAM Manager (NvM).
    :cvar OPERATING_SYSTEM: The service relates to the Operating System
        (OS).
    :cvar SECURE_ON_BOARD_COMMUNICATION: The service relates to the
        SecOc module.
    :cvar SYNC_BASE_TIME_MANAGER: The service relates to the Sync Time
        Base Manager (StbM).
    :cvar V_2_X_FACILITIES: This service relates to the Vehicle to X
        facilities.
    :cvar V_2_X_MANAGEMENT: This service relates to the Vehicle to X
        management.
    :cvar VENDOR_SPECIFIC: This value denotes a vendor-specific service.
    :cvar WATCH_DOG_MANAGER: The service relates to the Watchdog Manager
        (WdgM).
    """
    ANY_STANDARDIZED = "ANY-STANDARDIZED"
    BASIC_SOFTWARE_MODE_MANAGER = "BASIC-SOFTWARE-MODE-MANAGER"
    COM_MANAGER = "COM-MANAGER"
    CRYPTO_SERVICE_MANAGER = "CRYPTO-SERVICE-MANAGER"
    DEFAULT_ERROR_TRACER = "DEFAULT-ERROR-TRACER"
    DEVELOPMENT_ERROR_TRACER = "DEVELOPMENT-ERROR-TRACER"
    DIAGNOSTIC_COMMUNICATION_MANAGER = "DIAGNOSTIC-COMMUNICATION-MANAGER"
    DIAGNOSTIC_EVENT_MANAGER = "DIAGNOSTIC-EVENT-MANAGER"
    DIAGNOSTIC_LOG_AND_TRACE = "DIAGNOSTIC-LOG-AND-TRACE"
    ECU_MANAGER = "ECU-MANAGER"
    ERROR_TRACER = "ERROR-TRACER"
    FUNCTION_INHIBITION_MANAGER = "FUNCTION-INHIBITION-MANAGER"
    HARDWARE_TEST_MANAGER = "HARDWARE-TEST-MANAGER"
    J_1939_DCM = "J-1939-DCM"
    J_1939_REQUEST_MANAGER = "J-1939-REQUEST-MANAGER"
    NON_VOLATILE_RAM_MANAGER = "NON-VOLATILE-RAM-MANAGER"
    OPERATING_SYSTEM = "OPERATING-SYSTEM"
    SECURE_ON_BOARD_COMMUNICATION = "SECURE-ON-BOARD-COMMUNICATION"
    SYNC_BASE_TIME_MANAGER = "SYNC-BASE-TIME-MANAGER"
    V_2_X_FACILITIES = "V-2-X-FACILITIES"
    V_2_X_MANAGEMENT = "V-2-X-MANAGEMENT"
    VENDOR_SPECIFIC = "VENDOR-SPECIFIC"
    WATCH_DOG_MANAGER = "WATCH-DOG-MANAGER"
