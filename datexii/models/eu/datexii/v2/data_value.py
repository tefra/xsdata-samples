from dataclasses import dataclass, field
from typing import Optional
from datexii.models.eu.datexii.v2.computation_method_enum import (
    ComputationMethodEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class DataValue:
    """A data value of something that can be measured or calculated.

    Any provided meta-data values specified in the attributes override
    any specified generic characteristics such as defined for a specific
    measurement in the MeasurementSiteTable.

    :ivar data_error: Indication of whether the value is deemed to be
        erroneous by the supplier, (true = erroneous). If not present
        the data value is assumed to be ok. This may be used when
        automatic fault detection information relating to sensors is
        available.
    :ivar reason_for_data_error: The reason why the value is deemed to
        be erroneous by the supplier.
    :ivar data_value_extension:
    :ivar accuracy: The extent to which the value is expected to be free
        from error, measured as a percentage of the data value. 100%
        means fully accurate.
    :ivar computational_method: Method of computation which has been
        used to compute this data value.
    :ivar number_of_incomplete_inputs: The number of inputs detected but
        not completed during the sampling or measurement period; e.g.
        vehicles detected entering but not exiting the detection zone.
    :ivar number_of_input_values_used: The number of input values used
        in the sampling or measurment period to determine the data
        value.
    :ivar smoothing_factor: Coefficient required when a moving average
        is computed to give specific weights to the former average and
        the new data. A typical formula is, F being the smoothing
        factor: New average = (old average) F + (new data) (1 - F).
    :ivar standard_deviation: The standard deviation of the sample of
        input values from which this value was derived, measured in the
        units of the data value.
    :ivar supplier_calculated_data_quality: A measure of data quality
        assigned to the value by the supplier. 100% equates to
        ideal/perfect quality. The method of calculation is supplier
        specific and needs to be agreed between supplier and client.
    """

    data_error: Optional[bool] = field(
        default=None,
        metadata={
            "name": "dataError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    reason_for_data_error: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reasonForDataError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    data_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "dataValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    computational_method: Optional[ComputationMethodEnum] = field(
        default=None,
        metadata={
            "name": "computationalMethod",
            "type": "Attribute",
        },
    )
    number_of_incomplete_inputs: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfIncompleteInputs",
            "type": "Attribute",
        },
    )
    number_of_input_values_used: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfInputValuesUsed",
            "type": "Attribute",
        },
    )
    smoothing_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "smoothingFactor",
            "type": "Attribute",
        },
    )
    standard_deviation: Optional[float] = field(
        default=None,
        metadata={
            "name": "standardDeviation",
            "type": "Attribute",
        },
    )
    supplier_calculated_data_quality: Optional[float] = field(
        default=None,
        metadata={
            "name": "supplierCalculatedDataQuality",
            "type": "Attribute",
        },
    )
