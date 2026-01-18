from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class TrustedPlatformExecutableLaunchBehaviorEnumSimple(Enum):
    """
    :cvar MONITOR_MODE: An Executable shall always launch, even if the
        corresponding authentication fails
    :cvar NO_TRUSTED_PLATFORM_SUPPORT: This value shall be used if there
        is no TrustedPlatform support on the Machine
    :cvar STRICT_MODE: An Executable shall not launch if the
        corresponding authentication fails.
    """

    MONITOR_MODE = "MONITOR-MODE"
    NO_TRUSTED_PLATFORM_SUPPORT = "NO-TRUSTED-PLATFORM-SUPPORT"
    STRICT_MODE = "STRICT-MODE"
