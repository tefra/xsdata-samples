from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class RoadMaintenanceTypeEnum(Enum):
    """
    Types of road maintenance.

    :cvar CLEARANCE_WORK: Clearance work of an unspecified nature.
    :cvar CONTROLLED_AVALANCHE: Controlled avalanche work.
    :cvar INSTALLATION_WORK: Installation of new equipments or systems
        on or along-side the roadway.
    :cvar GRASS_CUTTING_WORK: Grass cutting work.
    :cvar LITTER_CLEARANCE: Work to collect litter from the roadway
        and/or adjacent verges.
    :cvar MAINTENANCE_WORK: Maintenance of road, associated
        infrastructure or equipments.
    :cvar OVERHEAD_WORKS: Works which are overhead of the carriageway.
    :cvar REPAIR_WORK: Repair work to road, associated infrastructure or
        equipments.
    :cvar RESURFACING_WORK: Work associated with relaying or renewal of
        worn-out road surface (pavement).
    :cvar ROAD_MARKING_WORK: Striping and repainting of road markings,
        plus placement or replacement of reflecting studs (cats' eyes).
    :cvar ROADSIDE_WORK: Road side work of an unspecified nature.
    :cvar ROADWORKS_CLEARANCE: Roadworks are completed and are being
        cleared.
    :cvar ROADWORKS: Road maintenance or improvement activity of an
        unspecified nature which may potentially cause traffic
        disruption.
    :cvar ROCK_FALL_PREVENTATIVE_MAINTENANCE: Rock fall preventative
        maintenance.
    :cvar SALTING_IN_PROGRESS: Spreading of salt and / or grit on the
        road surface to prevent or melt snow or ice.
    :cvar SNOWPLOUGHS_IN_USE: Snowploughs or other similar mechanical
        devices in use to clear snow from the road.
    :cvar SWEEPING_OF_ROAD: Sweeping of the roadway.
    :cvar TREE_AND_VEGETATION_CUTTING_WORK: Tree and vegetation cutting
        work adjacent to the roadway.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    CLEARANCE_WORK = "clearanceWork"
    CONTROLLED_AVALANCHE = "controlledAvalanche"
    INSTALLATION_WORK = "installationWork"
    GRASS_CUTTING_WORK = "grassCuttingWork"
    LITTER_CLEARANCE = "litterClearance"
    MAINTENANCE_WORK = "maintenanceWork"
    OVERHEAD_WORKS = "overheadWorks"
    REPAIR_WORK = "repairWork"
    RESURFACING_WORK = "resurfacingWork"
    ROAD_MARKING_WORK = "roadMarkingWork"
    ROADSIDE_WORK = "roadsideWork"
    ROADWORKS_CLEARANCE = "roadworksClearance"
    ROADWORKS = "roadworks"
    ROCK_FALL_PREVENTATIVE_MAINTENANCE = "rockFallPreventativeMaintenance"
    SALTING_IN_PROGRESS = "saltingInProgress"
    SNOWPLOUGHS_IN_USE = "snowploughsInUse"
    SWEEPING_OF_ROAD = "sweepingOfRoad"
    TREE_AND_VEGETATION_CUTTING_WORK = "treeAndVegetationCuttingWork"
    OTHER = "other"
