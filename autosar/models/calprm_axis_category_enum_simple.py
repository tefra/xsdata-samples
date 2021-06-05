from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class CalprmAxisCategoryEnumSimple(Enum):
    """
    :cvar COM_AXIS: COM-AXIS is equal to an STD_AXIS, the difference is,
        that a COM-AXIS is an shared axis, that means this axis can be
        used multiple times by different curves or maps. This value is
        obsolete.
    :cvar COM_AXIS_1: COM_AXIS is equal to an STD_AXIS, the difference
        is, that a COM_AXIS is an shared axis, that means this axis can
        be used multiple times by different CURVEs,  MAPs, CUBOIDs,
        CUBE_4s, and CUBE_5s.
    :cvar CURVE_AXIS: CURVE-AXIS uses a separate CURVE to rescale the
        axis. The referenced CURVE is used to lookup an axis index, and
        the index value is used by the controller to determine the
        operating point in the CURVE or MAP. This value is obsolete.
    :cvar CURVE_AXIS_1: CURVE_AXIS uses a separate CURVE to rescale the
        axis. The referenced CURVE is used to lookup an axis index, and
        the index value is used by the controller to determine the
        operating point in the CURVE, MAP, CUBOID, CUBE_4, or CUBE_5.
    :cvar FIX_AXIS: FIX-AXIS means that the input axis is not stored.
        The axis is calculated using parameters  and so on it is also
        not possible to modify the axis points. This value is obsolete.
    :cvar FIX_AXIS_1: FIX_AXIS means that the input axis is not stored.
        The axis is calculated using parameters  and so on it is also
        not possible to modify the axis points.
    :cvar RES_AXIS: RES-AXIS is also an shared axis like COM_AXIS, the
        difference is that this kind of axis can be used for rescaling.
        This value is obsolete.
    :cvar RES_AXIS_1: RES_AXIS is also an shared axis like COM_AXIS, the
        difference is that this kind of axis can be used for rescaling.
    :cvar STD_AXIS: STD-AXIS means that input and output axis definition
        are stored within this CURVE. There is no shared or calculated
        axis. This value is obsolete.
    :cvar STD_AXIS_1: STD_AXIS means that input and output axis
        definition are stored within this CURVE, MAP, CUBOID, CUBE_4,
        and CUBE_5. There is no shared or calculated axis.
    """
    COM_AXIS = "COM-AXIS"
    COM_AXIS_1 = "COM_AXIS"
    CURVE_AXIS = "CURVE-AXIS"
    CURVE_AXIS_1 = "CURVE_AXIS"
    FIX_AXIS = "FIX-AXIS"
    FIX_AXIS_1 = "FIX_AXIS"
    RES_AXIS = "RES-AXIS"
    RES_AXIS_1 = "RES_AXIS"
    STD_AXIS = "STD-AXIS"
    STD_AXIS_1 = "STD_AXIS"
