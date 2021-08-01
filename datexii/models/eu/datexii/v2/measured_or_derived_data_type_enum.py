from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class MeasuredOrDerivedDataTypeEnum(Enum):
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
    :cvar RADIATION_INFORMATION: Measured or derived radiation
        information.
    :cvar ROAD_SURFACE_CONDITION_INFORMATION: Measured or derived road
        surface conditions information.
    :cvar TEMPERATURE_INFORMATION: Measured or derived temperature
        information.
    :cvar TRAFFIC_CONCENTRATION: Measured or derived traffic
        concentration information.
    :cvar TRAFFIC_FLOW: Measured or derived traffic flow information.
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
    """
    HUMIDITY_INFORMATION = "humidityInformation"
    INDIVIDUAL_VEHICLE_MEASUREMENTS = "individualVehicleMeasurements"
    POLLUTION_INFORMATION = "pollutionInformation"
    PRECIPITATION_INFORMATION = "precipitationInformation"
    PRESSURE_INFORMATION = "pressureInformation"
    RADIATION_INFORMATION = "radiationInformation"
    ROAD_SURFACE_CONDITION_INFORMATION = "roadSurfaceConditionInformation"
    TEMPERATURE_INFORMATION = "temperatureInformation"
    TRAFFIC_CONCENTRATION = "trafficConcentration"
    TRAFFIC_FLOW = "trafficFlow"
    TRAFFIC_HEADWAY = "trafficHeadway"
    TRAFFIC_SPEED = "trafficSpeed"
    TRAFFIC_STATUS_INFORMATION = "trafficStatusInformation"
    TRAVEL_TIME_INFORMATION = "travelTimeInformation"
    VISIBILITY_INFORMATION = "visibilityInformation"
    WIND_INFORMATION = "windInformation"
