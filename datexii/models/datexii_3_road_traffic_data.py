from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from datexii.models.datexii_3_common import (
    DataValue,
    Fault,
    FloatingPointMetreDistanceValue,
    HeaderInformation,
    Humidity,
    InternationalIdentifier,
    MultilingualString,
    PayloadPublication,
    PercentageValue,
    Period,
    Pollution,
    PrecipitationDetail,
    Pressure,
    RoadSurfaceConditionMeasurements,
    Source,
    SpeedValue,
    Temperature,
    TimePrecisionEnum1,
    Vehicle,
    VehicleCharacteristics,
    VehicleFlowValue,
    VersionedReference,
    Visibility,
    Wind,
    ComputationMethodEnum2,
    ExtensionType,
    TrafficTrendTypeEnum2,
    VehicleTypeEnum2,
    WeatherRelatedRoadConditionTypeEnum2,
)
from datexii.models.datexii_3_location_referencing import (
    Lane,
    LocationReference,
    DirectionEnum2,
)

__NAMESPACE__ = "http://datex2.eu/schema/3/roadTrafficData"


class MeasuredOrDerivedDataTypeEnum1(Enum):
    """
    Types of measured or derived data.

    :cvar HUMIDITY_INFORMATION: Measured or derived humidity
        information.
    :cvar INDIVIDUAL_VEHICLE_MEASUREMENTS: Measured or derived
        individual vehicle measurements.
    :cvar POLLUTION_INFORMATION: Measured or derived pollution
        information.
    :cvar PRECIPITATION_INFORMATION: Measured or derived precipitation
        information.
    :cvar PRESSURE_INFORMATION: Measured or derived pressure
        information.
    :cvar ROAD_SURFACE_CONDITION_INFORMATION: Measured or derived road
        surface conditions information.
    :cvar TEMPERATURE_INFORMATION: Measured or derived temperature
        information.
    :cvar TRAFFIC_CONCENTRATION: Measured or derived traffic
        concentration information.
    :cvar TRAFFIC_FLOW: Measured or derived traffic flow information.
    :cvar TRAFFIC_GAP: Measured or derived traffic gap information.
    :cvar TRAFFIC_HEADWAY: Measured or derived traffic headway
        information.
    :cvar TRAFFIC_SPEED: Measured or derived traffic speed information.
    :cvar TRAFFIC_STATUS_INFORMATION: Measured or derived traffic status
        information.
    :cvar TRAVEL_TIME_INFORMATION: Measured or derived travel time
        information.
    :cvar VISIBILITY_INFORMATION: Measured or derived visibility
        information.
    :cvar WIND_INFORMATION: Measured or derived wind information.
    :cvar EXTENDED:
    """
    HUMIDITY_INFORMATION = "humidityInformation"
    INDIVIDUAL_VEHICLE_MEASUREMENTS = "individualVehicleMeasurements"
    POLLUTION_INFORMATION = "pollutionInformation"
    PRECIPITATION_INFORMATION = "precipitationInformation"
    PRESSURE_INFORMATION = "pressureInformation"
    ROAD_SURFACE_CONDITION_INFORMATION = "roadSurfaceConditionInformation"
    TEMPERATURE_INFORMATION = "temperatureInformation"
    TRAFFIC_CONCENTRATION = "trafficConcentration"
    TRAFFIC_FLOW = "trafficFlow"
    TRAFFIC_GAP = "trafficGap"
    TRAFFIC_HEADWAY = "trafficHeadway"
    TRAFFIC_SPEED = "trafficSpeed"
    TRAFFIC_STATUS_INFORMATION = "trafficStatusInformation"
    TRAVEL_TIME_INFORMATION = "travelTimeInformation"
    VISIBILITY_INFORMATION = "visibilityInformation"
    WIND_INFORMATION = "windInformation"
    EXTENDED = "_extended"


class PhysicalQuantityFaultEnum1(Enum):
    """
    Types of faults that may affect the measurement or calculation of physical
    quantities.

    :cvar INTERMITTENT_DATA_VALUES: Data values are being produced at
        intermittent intervals which are not consistent with the
        expected reporting interval.
    :cvar NO_DATA_VALUES_AVAILABLE: No measured or calculated data
        values are currently available.
    :cvar SPURIOUS_UNRELIABLE_DATA_VALUES: Spurious or unreliable data
        values are being produced.
    :cvar UNSPECIFIED_OR_UNKNOWN_FAULT: An unspecified or unknown fault
        exists in the process which is generating the measured or
        calculated data.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    INTERMITTENT_DATA_VALUES = "intermittentDataValues"
    NO_DATA_VALUES_AVAILABLE = "noDataValuesAvailable"
    SPURIOUS_UNRELIABLE_DATA_VALUES = "spuriousUnreliableDataValues"
    UNSPECIFIED_OR_UNKNOWN_FAULT = "unspecifiedOrUnknownFault"
    OTHER = "other"
    EXTENDED = "_extended"


class TimeMeaningEnum1(Enum):
    """
    Explains the meaning of a specific time value with respect to a time
    period.

    :cvar BEGIN_TIME: Meaning the beginning of a period
    :cvar END_TIME: Meaning the end of a period
    :cvar MIDDLE_TIME: Meaning the mid-point of a period
    :cvar EXTENDED:
    """
    BEGIN_TIME = "beginTime"
    END_TIME = "endTime"
    MIDDLE_TIME = "middleTime"
    EXTENDED = "_extended"


class TrafficStatusEnum1(Enum):
    """
    List of terms used to describe traffic conditions.

    :cvar STATIONARY: Traffic is stationary, or very near stationary, at
        the specified location (i.e. average speed is less than 10% of
        its free-flow level).
    :cvar QUEUING: Traffic is queuing at the specified location,
        although there is still some traffic movement (i.e. average
        speed is between 10% and 25% of its free-flow level).
    :cvar SLOW: Traffic is slow moving at the specified location, but
        not yet forming queues (i.e. average speed is between 25% and
        75% of its free-flow level).
    :cvar HEAVY: Traffic in the specified direction is heavier than
        usual making driving conditions more difficult than normal.
    :cvar UNSPECIFIED_ABNORMAL: There are abnormal traffic conditions of
        an unspecified nature at the specified location.
    :cvar FREE_FLOW: Traffic at the specified location is free-flowing.
    :cvar UNKNOWN: Traffic conditions are unknown.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    STATIONARY = "stationary"
    QUEUING = "queuing"
    SLOW = "slow"
    HEAVY = "heavy"
    UNSPECIFIED_ABNORMAL = "unspecifiedAbnormal"
    FREE_FLOW = "freeFlow"
    UNKNOWN = "unknown"
    OTHER = "other"
    EXTENDED = "_extended"


class TravelTimeTrendTypeEnum1(Enum):
    """
    List of terms used to describe the trend in travel times.

    :cvar DECREASING: Travel times are decreasing.
    :cvar INCREASING: Travel times are increasing.
    :cvar STABLE: Travel times are stable.
    :cvar EXTENDED:
    """
    DECREASING = "decreasing"
    INCREASING = "increasing"
    STABLE = "stable"
    EXTENDED = "_extended"


class TravelTimeTypeEnum1(Enum):
    """
    List of ways in which travel times are derived.

    :cvar BEST: Travel time is derived from the best out of a monitored
        sample.
    :cvar ESTIMATED: Travel time is an automated estimate.
    :cvar INSTANTANEOUS: Travel time is derived from instantaneous
        measurements.
    :cvar RECONSTITUTED: Travel time is reconstituted from other
        measurements.
    :cvar PREDICTOR: Travel time is the output of a predictor, for
        example a blend of current and historical data, or a traffic
        flow model using current measurements.
    :cvar PROFILE: Travel time is based on past observations, without
        use of current measurements.
    :cvar SUM: Travel time is the sum of current travel times on
        subsections of the specified location.
    :cvar EXTENDED:
    """
    BEST = "best"
    ESTIMATED = "estimated"
    INSTANTANEOUS = "instantaneous"
    RECONSTITUTED = "reconstituted"
    PREDICTOR = "predictor"
    PROFILE = "profile"
    SUM = "sum"
    EXTENDED = "_extended"


@dataclass
class AxleCharacteristics:
    """
    Characteristics of vehicle axles.

    :ivar maximum_weight: Maximum axle weight
    :ivar minimum_weight: Minimum axle weight
    :ivar axle_characteristics_extension:
    """
    maximum_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    minimum_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "minimumWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    axle_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_axleCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class AxleFlowValue(DataValue):
    """
    A measured or calculated value of the flow rate of vehicle axles.

    :ivar axle_flow_rate: A value of the flow rate of vehicle axles
        expressed in axles per hour.
    :ivar axle_flow_value_extension:
    """
    axle_flow_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "axleFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    axle_flow_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_axleFlowValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class DailyTrafficFlowValue(DataValue):
    """
    A measured or calculated value of daily traffic flow.

    :ivar vehicle_flow_rate: Value of daily vehicle flow in units of
        vehicles per day
    :ivar daily_traffic_flow_value_extension:
    """
    vehicle_flow_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "vehicleFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    daily_traffic_flow_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_dailyTrafficFlowValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class DateTimeValue(DataValue):
    """
    A measured or calculated value of an instant in time.

    :ivar date_time: A time stamp defining an instant in time.
    :ivar date_time_value_extension:
    """
    date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "dateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    date_time_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_dateTimeValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class DurationValue(DataValue):
    """
    A measured or calculated value of a period of time.

    :ivar duration: A period of time expressed in seconds.
    :ivar duration_value_extension:
    """
    duration: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    duration_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_durationValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class PcuFlowValue(DataValue):
    """
    A measured or calculated value of the flow rate of passenger car units.

    :ivar pcu_flow_rate: A value of passenger car unit flow rate
        expressed in passenger car units per hour.
    :ivar pcu_flow_value_extension:
    """
    pcu_flow_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "pcuFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    pcu_flow_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pcuFlowValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class SpeedPercentile:
    """
    Details of percentage (from an observation set) of vehicles whose speeds
    fall below a stated value.

    :ivar vehicle_percentage: The percentage of vehicles from the
        observation set whose speeds fall below the stated speed
        (speedPercentile).
    :ivar speed_percentile: The speed below which the associated
        percentage of vehicles in the measurement set are travelling at.
    :ivar speed_percentile_extension:
    """
    vehicle_percentage: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "name": "vehiclePercentage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    speed_percentile: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "speedPercentile",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    speed_percentile_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_speedPercentileExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TrafficDensityValue(DataValue):
    """
    A measured or calculated value of the density of vehicles on a unit stretch
    of road in a given direction.

    :ivar density_of_vehicles: A value of traffic density expressed in
        the number of vehicles per kilometre of road.
    :ivar traffic_density_value_extension:
    """
    density_of_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "densityOfVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    traffic_density_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficDensityValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class MeasuredOrDerivedDataTypeEnum2:
    class Meta:
        name = "_MeasuredOrDerivedDataTypeEnum"

    value: Optional[MeasuredOrDerivedDataTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class MeasurementSiteTableVersionedReference(VersionedReference):
    class Meta:
        name = "_MeasurementSiteTableVersionedReference"

    target_class: str = field(
        init=False,
        default="roa:MeasurementSiteTable",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MeasurementSiteVersionedReference(VersionedReference):
    class Meta:
        name = "_MeasurementSiteVersionedReference"

    target_class: str = field(
        init=False,
        default="roa:MeasurementSite",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PhysicalQuantityFaultEnum2:
    class Meta:
        name = "_PhysicalQuantityFaultEnum"

    value: Optional[PhysicalQuantityFaultEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class PredefinedLocationGroupVersionedReference(VersionedReference):
    class Meta:
        name = "_PredefinedLocationGroupVersionedReference"

    target_class: str = field(
        init=False,
        default="loc:PredefinedLocationGroup",
        metadata={
            "name": "targetClass",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class TimeMeaningEnum2:
    class Meta:
        name = "_TimeMeaningEnum"

    value: Optional[TimeMeaningEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TrafficStatusEnum2:
    class Meta:
        name = "_TrafficStatusEnum"

    value: Optional[TrafficStatusEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TravelTimeTrendTypeEnum2:
    class Meta:
        name = "_TravelTimeTrendTypeEnum"

    value: Optional[TravelTimeTrendTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class TravelTimeTypeEnum2:
    class Meta:
        name = "_TravelTimeTypeEnum"

    value: Optional[TravelTimeTypeEnum1] = field(
        default=None,
    )
    extended_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "_extendedValue",
            "type": "Attribute",
        }
    )


@dataclass
class MeasurementOrCalculationTime:
    """Describes the time at which a measured or calculated value or set of
    values was measured or calculated.

    It may be a future time at which a data value is predicted to apply.

    :ivar time_meaning: Meaning of associated time value
    :ivar time_value: Point in time at which this specific value or set
        of values has been measured or calculated. It may also be a
        future time at which a data value is predicted.  It may be the
        time of the beginning, the end or the middle of a measurement
        period.
    :ivar period: The measurement or calculation period
    :ivar measurement_or_calculation_time_extension:
    :ivar time_precision: The precision to which the time of measurement
        or calculation is given.
    """
    time_meaning: Optional[TimeMeaningEnum2] = field(
        default=None,
        metadata={
            "name": "timeMeaning",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    time_value: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    period: Optional[Period] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_or_calculation_time_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_measurementOrCalculationTimeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    time_precision: Optional[TimePrecisionEnum1] = field(
        default=None,
        metadata={
            "name": "timePrecision",
            "type": "Attribute",
        }
    )


@dataclass
class MeasurementSpecificCharacteristics:
    """
    Characteristics which are specific to an individual measurement type
    (specified in a known order) at the given measurement site.

    :ivar accuracy: The extent to which the value is expected to be free
        from error, measured as a percentage of the data value. 100%
        means fully accurate.
    :ivar computation_method: Method of computation which is used to
        compute the measured value at the measurement site.
    :ivar default_measurement_height: Default height, above (positive
        value) or below (negative value) ground level, at which
        measurements are made. For example in wind measurement this
        could be the height of an anemometer.
    :ivar measurement_side: Side of the road on which measurements are
        acquired, corresponding to the direction of the road.
    :ivar period: The time elapsed between the beginning and the end of
        the sampling or measurement period. This item may differ from
        the unit attribute; e.g. an hourly flow can be estimated from a
        5-minute measurement period.
    :ivar smoothing_factor: Coefficient required when a moving average
        is computed to give specific weights to the former average and
        the new data. A typical formula is, F being the smoothing
        factor: New average = (old average) F + (new data) (1 - F).
    :ivar specific_measurement_value_type: The type of this specific
        measurement at the measurement site.
    :ivar specific_vehicle_characteristics:
    :ivar specific_lane: The lane(s) to which the specific measurement
        at the measurement site relate(s). This overrides any lane
        specified for the measurement site as a whole.
    :ivar axle_characteristics: Axle characteristics for which the
        measurement applies
    :ivar measurement_specific_characteristics_extension:
    """
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    computation_method: Optional[ComputationMethodEnum2] = field(
        default=None,
        metadata={
            "name": "computationMethod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    default_measurement_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "defaultMeasurementHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_side: Optional[DirectionEnum2] = field(
        default=None,
        metadata={
            "name": "measurementSide",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    period: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    smoothing_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "smoothingFactor",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    specific_measurement_value_type: Optional[MeasuredOrDerivedDataTypeEnum2] = field(
        default=None,
        metadata={
            "name": "specificMeasurementValueType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    specific_vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "specificVehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    specific_lane: List[Lane] = field(
        default_factory=list,
        metadata={
            "name": "specificLane",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    axle_characteristics: Optional[AxleCharacteristics] = field(
        default=None,
        metadata={
            "name": "axleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_specific_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_measurementSpecificCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class PhysicalQuantityFault(Fault):
    """
    Details of a fault related to the derivation of a quantity.

    :ivar physical_quantity_fault_type: The type of fault related to the
        measurement or calculation of the physical quantity
    :ivar physical_quantity_fault_extension:
    """
    physical_quantity_fault_type: Optional[PhysicalQuantityFaultEnum2] = field(
        default=None,
        metadata={
            "name": "physicalQuantityFaultType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    physical_quantity_fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_physicalQuantityFaultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class ReferenceSettings:
    """Specification of default values for locations on the road network.

    Where a default status value is supplied, it shall apply for all
    specified locations, unless the publication includes an additional
    status value for a specified location.

    :ivar predefined_location_group_reference: A reference to a
        versioned instance of a predefined non-ordered location group as
        specified in a PredefinedLocationsPublication.
    :ivar traffic_status_default: The default value of traffic status
        that can be assumed to apply to the locations defined by the
        associated predefined location set.
    :ivar reference_settings_extension:
    """
    predefined_location_group_reference: Optional[PredefinedLocationGroupVersionedReference] = field(
        default=None,
        metadata={
            "name": "predefinedLocationGroupReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    traffic_status_default: Optional[TrafficStatusEnum2] = field(
        default=None,
        metadata={
            "name": "trafficStatusDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    reference_settings_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_referenceSettingsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TrafficStatusValue(DataValue):
    """
    A measured or calculated value of the status of traffic conditions on a
    section of road in a specified direction.

    :ivar traffic_status_value: A status value of traffic conditions on
        the identified section of road in the specified direction.
    :ivar traffic_status_value_extension:
    """
    traffic_status_value: Optional[TrafficStatusEnum2] = field(
        default=None,
        metadata={
            "name": "trafficStatusValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    traffic_status_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficStatusValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class BasicData:
    """
    Data that are either measured or calculated at the same time or over the
    same time period.

    :ivar measurement_or_calculation_time: Characteristics of the
        measurement or calculation time which should be considered to
        override any specified defaults
    :ivar basic_data_extension:
    """
    measurement_or_calculation_time: Optional[MeasurementOrCalculationTime] = field(
        default=None,
        metadata={
            "name": "measurementOrCalculationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    basic_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_basicDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class PhysicalQuantity:
    """
    A measured or calculated physical quantity, with related properties
    explaining its context, meaning or status.

    :ivar forecast: Indication of whether this quantity data is a
        forecast (true = forecast).
    :ivar measurement_equipment_type_used: The type of equipment used to
        gather the raw information from which the data values are
        determined, e.g. 'loop', 'ANPR' (automatic number plate
        recognition) or 'urban traffic management system' (such as
        SCOOT).
    :ivar pertinent_location: The location (e.g. the stretch of road or
        area) to which the data value(s) is or are pertinent/relevant.
        This may be different from the location of the measurement
        equipment (i.e. the measurement site location).
    :ivar physical_quantity_fault:
    :ivar source:
    :ivar information_manager_override: Organisation that manages the
        information content (is responsible for updates of this
        information) typically the organisation that first made the
        DATEX II publication of this content. This value overrides any
        value specified at a more general level.
    :ivar physical_quantity_extension:
    """
    forecast: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_equipment_type_used: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentTypeUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    pertinent_location: Optional[LocationReference] = field(
        default=None,
        metadata={
            "name": "pertinentLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    physical_quantity_fault: List[PhysicalQuantityFault] = field(
        default_factory=list,
        metadata={
            "name": "physicalQuantityFault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    source: Optional[Source] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    information_manager_override: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "informationManagerOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    physical_quantity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_physicalQuantityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class MeasurementSiteIndexMeasurementSpecificCharacteristics:
    class Meta:
        name = "_MeasurementSiteIndexMeasurementSpecificCharacteristics"

    measurement_specific_characteristics: Optional[MeasurementSpecificCharacteristics] = field(
        default=None,
        metadata={
            "name": "measurementSpecificCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class ElaboratedDataPublication(PayloadPublication):
    """
    A publication containing one or more elaborated data sets.

    :ivar forecast_default: The default value for the publication of
        whether the elaborated data is a forecast (true = forecast).
    :ivar period_default: The default value for the publication of the
        time elapsed between the beginning and the end of the sampling
        or measurement period. This item may differ from the unit
        attribute; e.g. an hourly flow can be estimated from a 5-minute
        measurement period.
    :ivar time_default: The default for the publication of the time at
        which the values have been computed/derived.
    :ivar header_information:
    :ivar reference_settings:
    :ivar physical_quantity:
    :ivar information_manager: Organisation that manages the information
        content (is responsible for updates of this information)
        typically the organisation that first made the DATEX II
        publication of this content.
    :ivar elaborated_data_publication_extension:
    """
    forecast_default: Optional[bool] = field(
        default=None,
        metadata={
            "name": "forecastDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    period_default: Optional[float] = field(
        default=None,
        metadata={
            "name": "periodDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    time_default: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "timeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    reference_settings: Optional[ReferenceSettings] = field(
        default=None,
        metadata={
            "name": "referenceSettings",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    physical_quantity: List[PhysicalQuantity] = field(
        default_factory=list,
        metadata={
            "name": "physicalQuantity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "min_occurs": 1,
        }
    )
    information_manager: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "informationManager",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    elaborated_data_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_elaboratedDataPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class MeasurementSite:
    """
    An identifiable single measurement site entry/record in the measurement
    site table.

    :ivar measurement_site_record_version_time: The date/time that this
        version of the measurement site record was defined. The identity
        and version of the measurement site record are defined by the
        class stereotype implementation.
    :ivar measurement_equipment_reference: The reference given to the
        measurement equipment at the site.
    :ivar measurement_equipment_type_used: The type of equipment used to
        gather the raw information from which the data values are
        determined, e.g. 'loop', 'ANPR' (automatic number plate
        recognition) or 'urban traffic management system' (such as
        SCOOT).
    :ivar measurement_site_name: Name of a measurement site.
    :ivar measurement_site_number_of_lanes: The number of lanes over
        which the measured value is determined.
    :ivar measurement_site_identification: Identification of a
        measurement site used by the supplier or consumer systems.
    :ivar measurement_specific_characteristics: Indexed measurement-
        specific characteristics associated with the measurement site.
        The index uniquely associates the measurement characteristics
        with the corresponding indexed measurement values for the
        measurement site.
    :ivar measurement_site_location:
    :ivar information_manager_override: Organisation that manages the
        information content (is responsible for updates of this
        information) typically the organisation that first made the
        DATEX II publication of this content. This value overrides any
        value specified at a more general level.
    :ivar measurement_site_extension:
    :ivar id:
    :ivar version:
    """
    measurement_site_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementSiteRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_equipment_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "max_length": 1024,
        }
    )
    measurement_equipment_type_used: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentTypeUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_site_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementSiteName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_site_number_of_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementSiteNumberOfLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_site_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "max_length": 1024,
        }
    )
    measurement_specific_characteristics: List[MeasurementSiteIndexMeasurementSpecificCharacteristics] = field(
        default_factory=list,
        metadata={
            "name": "measurementSpecificCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_site_location: Optional[LocationReference] = field(
        default=None,
        metadata={
            "name": "measurementSiteLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    information_manager_override: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "informationManagerOverride",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_site_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_measurementSiteExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class SinglePhysicalQuantity(PhysicalQuantity):
    """
    A measured or calculated physical quantity at a single instant or period in
    time, with related properties explaining its context, meaning or status.
    """
    basic_data: Optional[BasicData] = field(
        default=None,
        metadata={
            "name": "basicData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    single_physical_quantity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_singlePhysicalQuantityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TimeProfiledPhysicalQuantity(PhysicalQuantity):
    """
    A set of values for a measured or calculated physical quantity over a set
    of measurement or calculation times.
    """
    basic_data: List[BasicData] = field(
        default_factory=list,
        metadata={
            "name": "basicData",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    time_profiled_physical_quantity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_timeProfiledPhysicalQuantityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TrafficData(BasicData):
    """
    Measured or derived values relating to traffic or individual vehicle
    movements on a specific section or at a specific point on the road network.

    :ivar for_vehicles_with_characteristics_of: Used to define the
        vehicle characteristics to which the TrafficValue is applicable
        primarily in Elaborated Data Publications, but may also be used
        in Measured Data Publications to override vehicle
        characteristics defined for the measurement site.
    :ivar traffic_data_extension:
    """
    for_vehicles_with_characteristics_of: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "forVehiclesWithCharacteristicsOf",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    traffic_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TrafficStatus(BasicData):
    """
    The status of traffic conditions on a specific section or at a specific
    point on the road network.

    :ivar traffic_trend_type: A characterization of the trend in the
        traffic conditions at the specified location and direction.
    :ivar traffic_status: Status of traffic conditions on the identified
        section of road in the specified direction.
    :ivar traffic_status_extension:
    """
    traffic_trend_type: Optional[TrafficTrendTypeEnum2] = field(
        default=None,
        metadata={
            "name": "trafficTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    traffic_status: Optional[TrafficStatusValue] = field(
        default=None,
        metadata={
            "name": "trafficStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    traffic_status_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficStatusExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TravelTimeData(BasicData):
    """Derived/computed travel time information relating to a linear section of the road network; forecast = true means a forecast for a vehicle at the start of the specified location, forecast = false means calculation/measurement at the end.

    :ivar travel_time_trend_type: The current trend in the travel time
        between the defined locations in the specified direction.
    :ivar travel_time_type: Indication of the way in which the travel
        time is derived.
    :ivar vehicle_type: Vehicle type.
    :ivar travel_time: Derived/computed travel time information relating
        to a specific group of locations.
    :ivar free_flow_travel_time: The travel time which would be expected
        under ideal free flow conditions.
    :ivar normally_expected_travel_time: The travel time which is
        expected for the given period (e.g. date/time, holiday status
        etc.) and any known quasi-static conditions (e.g. long-term
        roadworks). This value is derived from historical analysis.
    :ivar travel_time_delay: Delay in travel time compared to free-flow
        conditions
    :ivar free_flow_speed: The free flow speed expected under ideal
        conditions, corresponding to the freeFlowTravelTime.
    :ivar travel_time_data_extension:
    """
    travel_time_trend_type: Optional[TravelTimeTrendTypeEnum2] = field(
        default=None,
        metadata={
            "name": "travelTimeTrendType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    travel_time_type: Optional[TravelTimeTypeEnum2] = field(
        default=None,
        metadata={
            "name": "travelTimeType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    vehicle_type: List[VehicleTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "vehicleType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    travel_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "travelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    free_flow_travel_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "freeFlowTravelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    normally_expected_travel_time: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "normallyExpectedTravelTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    travel_time_delay: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "travelTimeDelay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    free_flow_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "freeFlowSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    travel_time_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_travelTimeDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class WeatherData(BasicData):
    """
    Measured or derived values relating to the weather at a specific location
    or locations.
    """
    weather_data_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_weatherDataExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class SiteMeasurementsIndexPhysicalQuantity:
    class Meta:
        name = "_SiteMeasurementsIndexPhysicalQuantity"

    physical_quantity: Optional[PhysicalQuantity] = field(
        default=None,
        metadata={
            "name": "physicalQuantity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    index: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class HumidityInformation(WeatherData):
    """
    Measurements of atmospheric humidity.
    """
    humidity: Optional[Humidity] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    humidity_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_humidityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class IndividualVehicleDataValues(TrafficData):
    """
    Measured or calculated data values relating to individual vehicles derived
    from detectors at the specified measurement site.

    :ivar arrival_time: The time of the arrival of an individual vehicle
        in a detection zone.
    :ivar distance_gap: The measured distance between the front of this
        vehicle and the rear of the preceding one, in metres at the
        specified measurement site.
    :ivar distance_headway: The measured distance between one end
        (normally the front) of this vehicle and the same end of the
        preceding vehicle at the specified measurement site.
    :ivar exit_time: The time when an individual vehicle leaves a
        detection zone.
    :ivar passage_duration: The time elapsed between an individual
        vehicle entering a detection zone and exiting the same detection
        zone as detected by entry and exit sensors.
    :ivar presence_duration: The period of time during which a vehicle
        activates a presence sensor.
    :ivar speed: The measured speed of the individual vehicle at the
        specified measurement site.
    :ivar time_gap: The time interval between the arrival of this
        vehicle's front at a point on the roadway, and that of the
        departure of the rear of the preceding one.
    :ivar time_headway: The measured time interval between this
        vehicle's arrival at (or departure from) a point on the roadway,
        and the equivalent event for the preceding vehicle.
    :ivar individual_vehicle: Properties of the individual vehicle to
        which the measurement values relate
    :ivar individual_vehicle_data_values_extension:
    """
    arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "arrivalTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    distance_gap: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    distance_headway: Optional[float] = field(
        default=None,
        metadata={
            "name": "distanceHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    exit_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "exitTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    passage_duration: Optional[float] = field(
        default=None,
        metadata={
            "name": "passageDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    presence_duration: Optional[float] = field(
        default=None,
        metadata={
            "name": "presenceDuration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    speed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    time_gap: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    time_headway: Optional[float] = field(
        default=None,
        metadata={
            "name": "timeHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    individual_vehicle: Optional[Vehicle] = field(
        default=None,
        metadata={
            "name": "individualVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    individual_vehicle_data_values_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_individualVehicleDataValuesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class MeasurementSiteTable:
    """A Measurement Site Table comprising a number of sets of data, each
    describing the location from where a stream of measured data may be
    derived.

    Each location is known as a "measurement site" which can be a point,
    a linear road section or an area.

    :ivar measurement_site_table_identification: An alphanumeric
        identification for the measurement site table, possibly human
        readable.
    :ivar measurement_site:
    :ivar information_manager: Organisation that manages the information
        content (is responsible for updates of this information)
        typically the organisation that first made the DATEX II
        publication of this content.
    :ivar measurement_site_table_extension:
    :ivar id:
    :ivar version:
    """
    measurement_site_table_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteTableIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "max_length": 1024,
        }
    )
    measurement_site: List[MeasurementSite] = field(
        default_factory=list,
        metadata={
            "name": "measurementSite",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "min_occurs": 1,
        }
    )
    information_manager: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "informationManager",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_site_table_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_measurementSiteTableExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    version: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class PollutionInformation(WeatherData):
    """
    Measurements of atmospheric pollution.
    """
    pollution: List[Pollution] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "min_occurs": 1,
        }
    )
    pollution_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pollutionInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class PrecipitationInformation(WeatherData):
    """
    Measurements of precipitation.

    :ivar no_precipitation: Indication of whether precipitation is
        present or not. True indicates that there is no precipitation.
    :ivar precipitation_detail:
    :ivar precipitation_information_extension:
    """
    no_precipitation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "noPrecipitation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    precipitation_detail: Optional[PrecipitationDetail] = field(
        default=None,
        metadata={
            "name": "precipitationDetail",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    precipitation_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_precipitationInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class PressureInformation(WeatherData):
    """
    Measurements of atmospheric pressure.
    """
    pressure: Optional[Pressure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    pressure_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pressureInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class RoadSurfaceConditionInformation(WeatherData):
    """
    Measurements of road surface conditions which are related to the weather.

    :ivar weather_related_road_condition_type: The type of road surface
        condition that is related to the weather which is affecting the
        driving conditions.
    :ivar road_surface_condition_measurements:
    :ivar road_surface_condition_information_extension:
    """
    weather_related_road_condition_type: List[WeatherRelatedRoadConditionTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "weatherRelatedRoadConditionType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    road_surface_condition_measurements: Optional[RoadSurfaceConditionMeasurements] = field(
        default=None,
        metadata={
            "name": "roadSurfaceConditionMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    road_surface_condition_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_roadSurfaceConditionInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class SiteMeasurements:
    """
    A  measurement data set derived from a specific measurement site.

    :ivar measurement_site_reference: A reference to a versioned
        measurement site record defined in a Measurement Site table.
    :ivar physical_quantity: Indexed measured value associated with the
        measurement site. The index uniquely associates the measurement
        value with the corresponding indexed measurement characteristics
        defined for the measurement site.
    :ivar measurement_time_default: The time associated with the set of
        measurements.
    :ivar site_measurements_extension:
    """
    measurement_site_reference: Optional[MeasurementSiteVersionedReference] = field(
        default=None,
        metadata={
            "name": "measurementSiteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    physical_quantity: List[SiteMeasurementsIndexPhysicalQuantity] = field(
        default_factory=list,
        metadata={
            "name": "physicalQuantity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    measurement_time_default: Optional[MeasurementOrCalculationTime] = field(
        default=None,
        metadata={
            "name": "measurementTimeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    site_measurements_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_siteMeasurementsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TemperatureInformation(WeatherData):
    """
    Measurements of atmospheric temperature.
    """
    temperature: Optional[Temperature] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    temperature_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_temperatureInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TrafficConcentration(TrafficData):
    """
    Averaged measurements or calculations of traffic concentration.

    :ivar density: An averaged measurement or calculation of the
        concentration of vehicles at the specified measurement site.
    :ivar occupancy: An averaged measurement or calculation of the
        percentage of time that a section of road at the specified
        measurement site is occupied by vehicles.
    :ivar traffic_concentration_extension:
    """
    density: Optional[TrafficDensityValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    occupancy: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    traffic_concentration_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficConcentrationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TrafficFlow(TrafficData):
    """
    Averaged measurements or calculations of traffic flow rates.

    :ivar axle_flow: An averaged measurement or calculation of flow rate
        defined in terms of the number of vehicle axles passing the
        specified measurement site.
    :ivar pcu_flow: An averaged measurement or calculation of flow rate
        defined in terms of the number of passenger car units passing
        the specified measurement site.
    :ivar percentage_long_vehicles: An averaged measurement or
        calculation of the percentage of long vehicles contained in the
        traffic flow at the specified measurement site.
    :ivar vehicle_flow: An averaged measurement of flow rate defined in
        terms of the number of vehicles passing the specified
        measurement site.
    :ivar normally_expected_flow: The vehicle flow which is expected for
        the given period (e.g. date/time, holiday status etc.) and any
        known quasi-static conditions (e.g. long-term roadworks). This
        value is derived from historical analysis.
    :ivar annual_average_daily_traffic: Daily traffic flow averaged from
        the total over one year.
    :ivar monthly_average_daily_traffic: Daily traffic flow averaged
        from the total over one month.
    :ivar axle_characteristics: Axle characteristics for which the flow
        measurement applies.
    :ivar traffic_flow_extension:
    """
    axle_flow: Optional[AxleFlowValue] = field(
        default=None,
        metadata={
            "name": "axleFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    pcu_flow: Optional[PcuFlowValue] = field(
        default=None,
        metadata={
            "name": "pcuFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    percentage_long_vehicles: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "name": "percentageLongVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    vehicle_flow: Optional[VehicleFlowValue] = field(
        default=None,
        metadata={
            "name": "vehicleFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    normally_expected_flow: Optional[VehicleFlowValue] = field(
        default=None,
        metadata={
            "name": "normallyExpectedFlow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    annual_average_daily_traffic: Optional[DailyTrafficFlowValue] = field(
        default=None,
        metadata={
            "name": "annualAverageDailyTraffic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    monthly_average_daily_traffic: Optional[DailyTrafficFlowValue] = field(
        default=None,
        metadata={
            "name": "monthlyAverageDailyTraffic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    axle_characteristics: Optional[AxleCharacteristics] = field(
        default=None,
        metadata={
            "name": "axleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    traffic_flow_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficFlowExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TrafficGap(TrafficData):
    """
    Averaged measurements or calculations of traffic gap i.e. the distance or
    time interval between vehicles, measured between the rear of one vehicle
    and the front of the following vehicle.

    :ivar average_distance_gap: The average distance between the front
        of one vehicle and the rear of the preceding vehicle, averaged
        for all vehicles within a defined measurement period at the
        specified measurement site.
    :ivar average_time_gap: The average time gap between the front of
        one vehicle and the rear of the preceding vehicle, averaged for
        all vehicles within a defined measurement period at the
        specified measurement site.
    :ivar traffic_gap_extension:
    """
    average_distance_gap: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "averageDistanceGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    average_time_gap: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "averageTimeGap",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    traffic_gap_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficGapExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TrafficHeadway(TrafficData):
    """Averaged measurements or calculations of traffic headway, i.e. the
    distance or time interval between vehicles.

    This is measured one end (normally the front) of one vehicle to the
    same end of the following vehicle.

    :ivar average_distance_headway: The average distance between one end
        (normally the front) of this vehicle and the same end of the
        preceding vehicle, averaged for all vehicles within a defined
        measurement period at the specified measurement site.
    :ivar average_time_headway: The average time interval between one
        end (normally the front) of this vehicle and the same end of the
        preceding vehicle, averaged for all vehicles within a defined
        measurement period at the specified measurement site.
    :ivar traffic_headway_extension:
    """
    average_distance_headway: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "averageDistanceHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    average_time_headway: Optional[DurationValue] = field(
        default=None,
        metadata={
            "name": "averageTimeHeadway",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    traffic_headway_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficHeadwayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class TrafficSpeed(TrafficData):
    """
    Averaged measurements or calculations of traffic speed.

    :ivar average_vehicle_speed: An averaged measurement or calculation
        of the speed of vehicles at the specified location.
    :ivar speed_percentile:
    :ivar normally_expected_speed: The average vehicle speed which is
        expected for the given period (e.g. date/time, holiday status
        etc.) and any known quasi-static conditions (e.g. long-term
        roadworks). This value is derived from historical analysis.
    :ivar minimum_speed: The minimum speed
    :ivar maximum_speed: The maximum speed
    :ivar traffic_speed_extension:
    """
    average_vehicle_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "averageVehicleSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    speed_percentile: List[SpeedPercentile] = field(
        default_factory=list,
        metadata={
            "name": "speedPercentile",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    normally_expected_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "normallyExpectedSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    minimum_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "minimumSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    maximum_speed: Optional[SpeedValue] = field(
        default=None,
        metadata={
            "name": "maximumSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
    traffic_speed_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_trafficSpeedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class VisibilityInformation(WeatherData):
    """
    Measurements of atmospheric visibility.
    """
    visibility: Optional[Visibility] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    visibility_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_visibilityInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class WindInformation(WeatherData):
    """
    Measurements of wind conditions.
    """
    wind: Optional[Wind] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    wind_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_windInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class MeasuredDataPublication(PayloadPublication):
    """
    A publication containing one or more measurement data sets, each set being
    measured at a single measurement site.

    :ivar measurement_site_table_reference: A reference to a versioned
        Measurement Site table.
    :ivar header_information:
    :ivar site_measurements:
    :ivar measured_data_publication_extension:
    """
    measurement_site_table_reference: List[MeasurementSiteTableVersionedReference] = field(
        default_factory=list,
        metadata={
            "name": "measurementSiteTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "min_occurs": 1,
        }
    )
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    site_measurements: List[SiteMeasurements] = field(
        default_factory=list,
        metadata={
            "name": "siteMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "min_occurs": 1,
        }
    )
    measured_data_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_measuredDataPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )


@dataclass
class MeasurementSiteTablePublication(PayloadPublication):
    """
    A publication containing one or more Measurement Site Tables.
    """
    header_information: Optional[HeaderInformation] = field(
        default=None,
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "required": True,
        }
    )
    measurement_site_table: List[MeasurementSiteTable] = field(
        default_factory=list,
        metadata={
            "name": "measurementSiteTable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
            "min_occurs": 1,
        }
    )
    measurement_site_table_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_measurementSiteTablePublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/roadTrafficData",
        }
    )
