from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PermitTypeEnum(Enum):
    """
    Type of permission for parking.

    :cvar BLUE_ZONE_PERMIT: Blue zone permit.
    :cvar CARE_TAKING_PERMIT: Permit for care taking.
    :cvar CARPOOLING_PERMIT: A permit for vehicles used for carpooling.
    :cvar CAR_SHARING_PERMIT: A permit for car sharing vehicles.
    :cvar DISABLED_PERMIT: Permit for disabled.
    :cvar EMERGENCY_VEHICLE_PERMIT: Permit for emergency vehicle.
    :cvar EMPLOYEE_PERMIT: Permit for employees.
    :cvar FAIR_PERMIT: Permit of a fair.
    :cvar GOVERNMENT_PERMIT: Vehicles that have an official parking
        permission from the appropriate (local) government.
    :cvar MAINTENANCE_VEHICLE_PERMIT: Permit for a maintenance vehicle.
    :cvar RESIDENT_PERMIT: Permit for a resident.
    :cvar ROAD_WORKS_PERMIT: Permit for road works.
    :cvar SPECIFIC_IDENTIFIED_VEHICLE_PERMIT: A specific identified
        vehicle.
    :cvar TAXI_PERMIT: Permit for a taxi.
    :cvar OTHER: Some other permit.
    """

    BLUE_ZONE_PERMIT = "blueZonePermit"
    CARE_TAKING_PERMIT = "careTakingPermit"
    CARPOOLING_PERMIT = "carpoolingPermit"
    CAR_SHARING_PERMIT = "carSharingPermit"
    DISABLED_PERMIT = "disabledPermit"
    EMERGENCY_VEHICLE_PERMIT = "emergencyVehiclePermit"
    EMPLOYEE_PERMIT = "employeePermit"
    FAIR_PERMIT = "fairPermit"
    GOVERNMENT_PERMIT = "governmentPermit"
    MAINTENANCE_VEHICLE_PERMIT = "maintenanceVehiclePermit"
    RESIDENT_PERMIT = "residentPermit"
    ROAD_WORKS_PERMIT = "roadWorksPermit"
    SPECIFIC_IDENTIFIED_VEHICLE_PERMIT = "specificIdentifiedVehiclePermit"
    TAXI_PERMIT = "taxiPermit"
    OTHER = "other"
