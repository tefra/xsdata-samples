from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class MemorySectionTypeSimple(Enum):
    """
    :cvar CALIBRATION_OFFLINE: Program data which can only be used for
        offline calibration.  '''Note''': This value is deprecated and
        shall be substituted by calPrm.
    :cvar CALIBRATION_ONLINE: Program data which can be used for online
        calibration.  '''Note''': This value is deprecated and shall be
        substituted by calPrm.
    :cvar CALIBRATION_VARIABLES: This memory section is reserved for
        "virtual variables" that are computed by an MCD system during a
        measurement session but do not exist in the ECU memory.
    :cvar CALPRM: To be used for calibratable constants of ECU-
        functions.
    :cvar CODE: To be used for mapping code to application block, boot
        block, external flash etc.
    :cvar CONFIG_DATA: Constants with attributes that show that they
        reside in one segment for module configuration.
    :cvar CONST: To be used for global or static constants.
    :cvar EXCLUDE_FROM_FLASH: This memory section is reserved for
        "virtual parameters" that are taken for computing the values of
        so-called dependent parameter of an MCD system. Dependent
        Parameters that are not at the same time "virtual parameters"
        are allocated in the ECU memory.  Virtual parameters, on the
        other hand, are not allocated in the ECU memory. Virtual
        parameters exist in the ECU Hex file for the purpose of being
        considered (for computing the values of dependent parameters)
        during an offline-calibration session.
    :cvar USER_DEFINED: No specific categorization of sectionType
        possible.  '''Note''': This value is deprecated and shall be
        substituted by var, code, const, calprm, configData,
        excludeFromFlash and the appropriate values of the orthogonal
        attributes sectionInitializationPolicy,
        memoryAllocationKeywordPolicy and option.
    :cvar VAR: To be used for global or static variables. The expected
        initialization is specified with the attribute
        sectionInitializationPolicy.
    :cvar VAR_FAST: To be used for all global or static variables that
        have at least one of the following properties: - accessed bit-
        wise - frequently used - high number of accesses in source code
        Some platforms allow the use of bit instructions for variables
        located in this specific RAM area as well as shorter addressing
        instructions. This saves code and runtime.  '''Note''': This
        value is deprecated and shall be substituted by var and the
        appropriate values of the orthogonal attributes
        sectionInitializationPolicy, memoryAllocationKeywordPolicy and
        option.
    :cvar VAR_NO_INIT: To be used for all global or static variables
        that are never initialized.  '''Note''': This value is
        deprecated and shall be substituted by var and the appropriate
        values of the orthogonal attributes sectionInitializationPolicy,
        memoryAllocationKeywordPolicy and option.
    :cvar VAR_POWER_ON_INIT: To be used for all global or static
        variables that are initialized only after power on reset.
        '''Note''': This value is deprecated and shall be substituted by
        var and the appropriate values of the orthogonal attributes
        sectionInitializationPolicy, memoryAllocationKeywordPolicy and
        option.
    """
    CALIBRATION_OFFLINE = "CALIBRATION-OFFLINE"
    CALIBRATION_ONLINE = "CALIBRATION-ONLINE"
    CALIBRATION_VARIABLES = "CALIBRATION-VARIABLES"
    CALPRM = "CALPRM"
    CODE = "CODE"
    CONFIG_DATA = "CONFIG-DATA"
    CONST = "CONST"
    EXCLUDE_FROM_FLASH = "EXCLUDE-FROM-FLASH"
    USER_DEFINED = "USER-DEFINED"
    VAR = "VAR"
    VAR_FAST = "VAR-FAST"
    VAR_NO_INIT = "VAR-NO-INIT"
    VAR_POWER_ON_INIT = "VAR-POWER-ON-INIT"
