from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ComputationMethodEnum(Enum):
    """
    Types of computational methods used in deriving data values for data sets.

    :cvar
        ARITHMETIC_AVERAGE_OF_SAMPLES_BASED_ON_AFIXED_NUMBER_OF_SAMPLES:
        Arithmetic average of sample values based on a fixed number of
        samples.
    :cvar ARITHMETIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD: Arithmetic
        average of sample values in a time period.
    :cvar HARMONIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD: Harmonic average
        of sample values in a time period.
    :cvar MEDIAN_OF_SAMPLES_IN_ATIME_PERIOD: Median of sample values
        taken over a time period.
    :cvar MOVING_AVERAGE_OF_SAMPLES: Moving average of sample values.
    """
    ARITHMETIC_AVERAGE_OF_SAMPLES_BASED_ON_AFIXED_NUMBER_OF_SAMPLES = "arithmeticAverageOfSamplesBasedOnAFixedNumberOfSamples"
    ARITHMETIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = "arithmeticAverageOfSamplesInATimePeriod"
    HARMONIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = "harmonicAverageOfSamplesInATimePeriod"
    MEDIAN_OF_SAMPLES_IN_ATIME_PERIOD = "medianOfSamplesInATimePeriod"
    MOVING_AVERAGE_OF_SAMPLES = "movingAverageOfSamples"
