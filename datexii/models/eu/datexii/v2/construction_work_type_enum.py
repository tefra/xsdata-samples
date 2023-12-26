from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class ConstructionWorkTypeEnum(Enum):
    """
    Types of works relating to construction.

    :cvar BLASTING_WORK: Blasting or quarrying work at the specified
        location.
    :cvar CONSTRUCTION_WORK: Construction work of a general nature at
        the specified location.
    :cvar DEMOLITION_WORK: Demolition work associated with the
        construction work.
    :cvar ROAD_IMPROVEMENT_OR_UPGRADING: Construction work associated
        with improvements to the road or its layout or with it
        upgrading.
    :cvar ROAD_WIDENING_WORK: Road widening work at the specified
        location.
    """

    BLASTING_WORK = "blastingWork"
    CONSTRUCTION_WORK = "constructionWork"
    DEMOLITION_WORK = "demolitionWork"
    ROAD_IMPROVEMENT_OR_UPGRADING = "roadImprovementOrUpgrading"
    ROAD_WIDENING_WORK = "roadWideningWork"
