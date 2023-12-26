from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DataTransformationKindEnumSimple(Enum):
    """
    :cvar ASYMMETRIC_FROM_BYTE_ARRAY: The DataTransformation shall only
        be applied to the receiving end only, i.e. transform from byte
        array to data type.
    :cvar ASYMMETRIC_TO_BYTE_ARRAY: The DataTransformation shall be
        applied to the sending end only, i.e. from data type to byte
        array.
    :cvar SYMMETRIC: The DataTransformation shall be applied at both the
        sending and the receiving end of the communication.
    """

    ASYMMETRIC_FROM_BYTE_ARRAY = "ASYMMETRIC-FROM-BYTE-ARRAY"
    ASYMMETRIC_TO_BYTE_ARRAY = "ASYMMETRIC-TO-BYTE-ARRAY"
    SYMMETRIC = "SYMMETRIC"
