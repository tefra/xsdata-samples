from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticJumpToBootLoaderEnumSimple(Enum):
    """
    :cvar NO_BOOT: This diagnostic session doesn't allow to jump to
        Bootloader.
    :cvar OEM_BOOT: This diagnostic session allows to jump to OEM
        Bootloader. In this case the bootloader send the final response.
    :cvar OEM_BOOT_RESP_APP: This diagnostic session allows to jump to
        OEM Bootloader and application sends final response.
    :cvar SYSTEM_SUPPLIER_BOOT: This diagnostic session allows to jump
        to System Supplier Bootloader.  In this case the bootloader send
        the final response.
    :cvar SYSTEM_SUPPLIER_BOOT_RESP_APP: This diagnostic session allows
        to jump to System Supplier Bootloader and application sends
        final response.
    """
    NO_BOOT = "NO-BOOT"
    OEM_BOOT = "OEM-BOOT"
    OEM_BOOT_RESP_APP = "OEM-BOOT-RESP-APP"
    SYSTEM_SUPPLIER_BOOT = "SYSTEM-SUPPLIER-BOOT"
    SYSTEM_SUPPLIER_BOOT_RESP_APP = "SYSTEM-SUPPLIER-BOOT-RESP-APP"
