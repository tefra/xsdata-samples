from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class EcucConfigurationVariantEnumSimple(Enum):
    """
    :cvar PRECONFIGURED_CONFIGURATION: Preconfigured (i.e. fixed)
        configuration which cannot be changed.
    :cvar RECOMMENDED_CONFIGURATION: Recommended configuration for a
        module.
    :cvar VARIANT_LINK_TIME: Specifies that the BSW Module
        implementation may use PreCompileTime and LinkTime configuration
        parameters.
    :cvar VARIANT_POST_BUILD: Specifies that the BSW Module
        implementation may use PreCompileTime, LinkTime and PostBuild
        configuration parameters.
    :cvar VARIANT_POST_BUILD_LOADABLE: Specifies that the BSW Module
        implementation may use PreCompileTime, LinkTime and PostBuild
        loadable configuration parameters (supported in the VSMD). This
        attribute is removed from the specifications and shall not be
        used.
    :cvar VARIANT_POST_BUILD_SELECTABLE: Specifies that the BSW Module
        implementation may use PreCompileTime, LinkTime and PostBuild
        selectable configuration parameters (supported in the VSMD).
        This attribute is removed from the specifications and shall not
        be used.
    :cvar VARIANT_PRE_COMPILE: Specifies that the BSW Module
        implementation uses only PreCompileTime configuration
        parameters.
    """

    PRECONFIGURED_CONFIGURATION = "PRECONFIGURED-CONFIGURATION"
    RECOMMENDED_CONFIGURATION = "RECOMMENDED-CONFIGURATION"
    VARIANT_LINK_TIME = "VARIANT-LINK-TIME"
    VARIANT_POST_BUILD = "VARIANT-POST-BUILD"
    VARIANT_POST_BUILD_LOADABLE = "VARIANT-POST-BUILD-LOADABLE"
    VARIANT_POST_BUILD_SELECTABLE = "VARIANT-POST-BUILD-SELECTABLE"
    VARIANT_PRE_COMPILE = "VARIANT-PRE-COMPILE"
