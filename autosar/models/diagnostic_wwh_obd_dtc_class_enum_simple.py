from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticWwhObdDtcClassEnumSimple(Enum):
    """
    :cvar DEM_DTC_WWH_OBD_CLASS_A: This attribute represents the
        severity class A.
    :cvar DEM_DTC_WWH_OBD_CLASS_B_1: This attribute represents the
        severity class B1.
    :cvar DEM_DTC_WWH_OBD_CLASS_B_2: This attribute represents the
        severity class B2.
    :cvar DEM_DTC_WWH_OBD_CLASS_C: This attribute represents the
        severity class C.
    :cvar DEM_DTC_WWH_OBD_CLASS_NO_INFORMATION: This attribute
        represents the option to intentionally not describe a dedicated
        severity class of an WWH-OBD DTC.
    """

    DEM_DTC_WWH_OBD_CLASS_A = "DEM-DTC-WWH-OBD-CLASS-A"
    DEM_DTC_WWH_OBD_CLASS_B_1 = "DEM-DTC-WWH-OBD-CLASS-B-1"
    DEM_DTC_WWH_OBD_CLASS_B_2 = "DEM-DTC-WWH-OBD-CLASS-B-2"
    DEM_DTC_WWH_OBD_CLASS_C = "DEM-DTC-WWH-OBD-CLASS-C"
    DEM_DTC_WWH_OBD_CLASS_NO_INFORMATION = (
        "DEM-DTC-WWH-OBD-CLASS-NO-INFORMATION"
    )
