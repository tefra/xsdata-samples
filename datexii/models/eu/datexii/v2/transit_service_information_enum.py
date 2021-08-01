from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class TransitServiceInformationEnum(Enum):
    """
    Types of public transport information.

    :cvar CANCELLATIONS: Public transport, park-and-ride, rail or bus
        services will be cancelled until the specified time.
    :cvar DELAY_DUE_TO_BAD_WEATHER: The specified service is delayed due
        to bad weather.
    :cvar DELAY_DUE_TO_REPAIRS: The specified service is delayed due to
        the need for repairs.
    :cvar DELAYED_UNTIL_FURTHER_NOTICE: The specified public transport
        service will be delayed until further notice.
    :cvar DELAYS_DUE_TO_FLOTSAM: The departure of the specified ferry
        service is delayed due to flotsam.
    :cvar DEPARTURE_ON_SCHEDULE: The departure of the specified service
        is on schedule.
    :cvar FERRY_REPLACED_BY_ICE_ROAD: The ferry service has been
        replaced by an ice road.
    :cvar FREE_SHUTTLE_SERVICE_OPERATING: A shuttle service is operating
        at no charge between specified locations until the specified
        time.
    :cvar INFORMATION_SERVICE_NOT_AVAILABLE: The information service
        relating to the specified transport system is not currently
        available.
    :cvar IRREGULAR_SERVICE_DELAYS: The specified service is subject to
        irregular delays.
    :cvar LOAD_CAPACITY_CHANGED: The load capacity for the specified
        service has been changed.
    :cvar RESTRICTIONS_FOR_LONGER_VEHICLES: Long vehicles are subject to
        restrictions on the specified service.
    :cvar SERVICE_DELAYS: The specified service is subject to delays.
    :cvar SERVICE_DELAYS_OF_UNCERTAIN_DURATION: The specified service is
        subject to delays whose predicted duration cannot be estimated
        accurately.
    :cvar SERVICE_FULLY_BOOKED: The departure of the specified service
        is fully booked.
    :cvar SERVICE_NOT_OPERATING: The specified service is not operating
        until the specified time.
    :cvar SERVICE_NOT_OPERATING_SUBSTITUTE_SERVICE_AVAILABLE: The
        specified service is not operating but an alternative service is
        available.
    :cvar SERVICE_SUSPENDED: The specified service has been suspended
        until the specified time.
    :cvar SERVICE_WITHDRAWN: The specified service has been cancelled.
    :cvar SHUTTLE_SERVICE_OPERATING: A shuttle service is operating
        between the specified locations until the specified time.
    :cvar TEMPORARY_CHANGES_TO_TIMETABLES: The timetable for the
        specified service is subject to temporary changes.
    :cvar OTHER: Other than as defined in this enumeration.
    """
    CANCELLATIONS = "cancellations"
    DELAY_DUE_TO_BAD_WEATHER = "delayDueToBadWeather"
    DELAY_DUE_TO_REPAIRS = "delayDueToRepairs"
    DELAYED_UNTIL_FURTHER_NOTICE = "delayedUntilFurtherNotice"
    DELAYS_DUE_TO_FLOTSAM = "delaysDueToFlotsam"
    DEPARTURE_ON_SCHEDULE = "departureOnSchedule"
    FERRY_REPLACED_BY_ICE_ROAD = "ferryReplacedByIceRoad"
    FREE_SHUTTLE_SERVICE_OPERATING = "freeShuttleServiceOperating"
    INFORMATION_SERVICE_NOT_AVAILABLE = "informationServiceNotAvailable"
    IRREGULAR_SERVICE_DELAYS = "irregularServiceDelays"
    LOAD_CAPACITY_CHANGED = "loadCapacityChanged"
    RESTRICTIONS_FOR_LONGER_VEHICLES = "restrictionsForLongerVehicles"
    SERVICE_DELAYS = "serviceDelays"
    SERVICE_DELAYS_OF_UNCERTAIN_DURATION = "serviceDelaysOfUncertainDuration"
    SERVICE_FULLY_BOOKED = "serviceFullyBooked"
    SERVICE_NOT_OPERATING = "serviceNotOperating"
    SERVICE_NOT_OPERATING_SUBSTITUTE_SERVICE_AVAILABLE = "serviceNotOperatingSubstituteServiceAvailable"
    SERVICE_SUSPENDED = "serviceSuspended"
    SERVICE_WITHDRAWN = "serviceWithdrawn"
    SHUTTLE_SERVICE_OPERATING = "shuttleServiceOperating"
    TEMPORARY_CHANGES_TO_TIMETABLES = "temporaryChangesToTimetables"
    OTHER = "other"
