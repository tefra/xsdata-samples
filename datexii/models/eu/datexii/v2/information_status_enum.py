from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class InformationStatusEnum(Enum):
    """
    Status of the related information (i.e. real, test or exercise).

    :cvar REAL: The information is real. It is not a test or exercise.
    :cvar SECURITY_EXERCISE: The information is part of an exercise
        which is for testing security.
    :cvar TECHNICAL_EXERCISE: The information is part of an exercise
        which includes tests of associated technical subsystems.
    :cvar TEST: The information is part of a test for checking the
        exchange of this type of information.
    """
    REAL = "real"
    SECURITY_EXERCISE = "securityExercise"
    TECHNICAL_EXERCISE = "technicalExercise"
    TEST = "test"
