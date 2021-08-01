from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class MaintenanceVehicleActionsEnum(Enum):
    """
    Types of maintenance vehicle actions associated with roadworks.

    :cvar MAINTENANCE_VEHICLES_MERGING_INTO_TRAFFIC_FLOW: Maintenance
        vehicles are merging into the traffic flow creating a potential
        hazard for road users.
    :cvar SALT_AND_GRIT_SPREADING: Maintenance vehicle(s) are spreading
        salt and/or grit.
    :cvar SLOW_MOVING: Maintenance vehicles are slow moving.
    :cvar SNOW_CLEARING: Maintenance vehicle(s) are involved in the
        clearance of snow.
    :cvar STOPPING_TO_SERVICE_EQUIPMENTS: Maintenance vehicles are
        stopping to service equipments on or next to the roadway.
    """
    MAINTENANCE_VEHICLES_MERGING_INTO_TRAFFIC_FLOW = "maintenanceVehiclesMergingIntoTrafficFlow"
    SALT_AND_GRIT_SPREADING = "saltAndGritSpreading"
    SLOW_MOVING = "slowMoving"
    SNOW_CLEARING = "snowClearing"
    STOPPING_TO_SERVICE_EQUIPMENTS = "stoppingToServiceEquipments"
