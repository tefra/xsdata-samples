from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class AccidentTypeEnum(Enum):
    """
    Collection of descriptive terms for types of accidents.

    :cvar ACCIDENT: Accidents are situations in which one or more
        vehicles lose control and do not recover.  They include
        collisions between vehicle(s) or other road user(s), between
        vehicle(s) and fixed obstacle(s), or they result from a vehicle
        running off the road.
    :cvar ACCIDENT_INVOLVING_BICYCLES: Includes all accidents involving
        at least one bicycle.
    :cvar ACCIDENT_INVOLVING_BUSES: Includes all accidents involving at
        least one passenger vehicle.
    :cvar ACCIDENT_INVOLVING_HAZARDOUS_MATERIALS: Includes all accidents
        involving at least one vehicle believed to be carrying
        materials, which could present an additional hazard to road
        users.
    :cvar ACCIDENT_INVOLVING_HEAVY_LORRIES: Includes all accidents
        involving at least one heavy goods vehicle.
    :cvar ACCIDENT_INVOLVING_MASS_TRANSIT_VEHICLE: Includes all
        accidents involving at least one mass transit vehicle.
    :cvar ACCIDENT_INVOLVING_MOPEDS: Includes all accidents involving at
        least one moped.
    :cvar ACCIDENT_INVOLVING_MOTORCYCLES: Includes all accidents
        involving at least one motorcycle.
    :cvar ACCIDENT_INVOLVING_RADIOACTIVE_MATERIAL: Accident involving
        radioactive material.
    :cvar ACCIDENT_INVOLVING_TRAIN: Includes all accidents involving
        collision with a train.
    :cvar CHEMICAL_SPILLAGE_ACCIDENT: Includes all situations resulting
        in a spillage of chemicals on the carriageway.
    :cvar COLLISION: Collision of vehicle with another object of
        unspecified type.
    :cvar COLLISION_WITH_ANIMAL: Collision of vehicle with one or more
        animals.
    :cvar COLLISION_WITH_OBSTRUCTION: Collision of vehicle with an
        object of a stationary nature.
    :cvar COLLISION_WITH_PERSON: Collision of vehicle with one or more
        pedestrians.
    :cvar EARLIER_ACCIDENT: An earlier reported accident that is causing
        disruption to traffic or is resulting in further accidents.
    :cvar FUEL_SPILLAGE_ACCIDENT: Includes all situations resulting in a
        spillage of fuel on the carriageway.
    :cvar HEAD_ON_COLLISION: Collision of vehicle with another vehicle
        head on.
    :cvar HEAD_ON_OR_SIDE_COLLISION: Collision of vehicle with another
        vehicle either head on or sideways.
    :cvar JACKKNIFED_ARTICULATED_LORRY: Includes all situations
        resulting in a heavy goods vehicle folding together in an
        accidental skidding movement on the carriageway.
    :cvar JACKKNIFED_CARAVAN: Includes all situations resulting in a
        vehicle and caravan folding together in an accidental skidding
        movement on the carriageway.
    :cvar JACKKNIFED_TRAILER: Includes all situations resulting in a
        vehicle and trailer folding together in an accidental skidding
        movement on the carriageway.
    :cvar MULTIPLE_VEHICLE_COLLISION: Multiple vehicles involved in a
        collision.
    :cvar MULTIVEHICLE_ACCIDENT: Includes all accidents involving three
        or more vehicles.
    :cvar OIL_SPILLAGE_ACCIDENT: Includes all situations resulting in a
        spillage of oil on the carriageway.
    :cvar OVERTURNED_HEAVY_LORRY: Includes all situations resulting in
        the overturning of a heavy goods vehicle on the carriageway.
    :cvar OVERTURNED_TRAILER: Includes all situations resulting in the
        overturning of a trailer.
    :cvar OVERTURNED_VEHICLE: Includes all situations resulting in the
        overturning of a vehicle (of unspecified type) on the
        carriageway.
    :cvar REAR_COLLISION: Includes all accidents where one or more
        vehicles have collided with the rear of one or more other
        vehicles.
    :cvar SECONDARY_ACCIDENT: Includes all situations resulting from
        vehicles avoiding or being distracted by earlier accidents.
    :cvar SERIOUS_ACCIDENT: Includes all accidents believed to involve
        fatality or injury expected to require overnight
        hospitalisation.
    :cvar SIDE_COLLISION: Includes all accidents where one or more
        vehicles have collided with the side of one or more other
        vehicles.
    :cvar VEHICLE_OFF_ROAD: Includes all accidents where one or more
        vehicles have left the roadway.
    :cvar VEHICLE_SPUN_AROUND: Includes all accidents where a vehicle
        has skidded and has come to rest not facing its intended line of
        travel.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    ACCIDENT = "accident"
    ACCIDENT_INVOLVING_BICYCLES = "accidentInvolvingBicycles"
    ACCIDENT_INVOLVING_BUSES = "accidentInvolvingBuses"
    ACCIDENT_INVOLVING_HAZARDOUS_MATERIALS = (
        "accidentInvolvingHazardousMaterials"
    )
    ACCIDENT_INVOLVING_HEAVY_LORRIES = "accidentInvolvingHeavyLorries"
    ACCIDENT_INVOLVING_MASS_TRANSIT_VEHICLE = (
        "accidentInvolvingMassTransitVehicle"
    )
    ACCIDENT_INVOLVING_MOPEDS = "accidentInvolvingMopeds"
    ACCIDENT_INVOLVING_MOTORCYCLES = "accidentInvolvingMotorcycles"
    ACCIDENT_INVOLVING_RADIOACTIVE_MATERIAL = (
        "accidentInvolvingRadioactiveMaterial"
    )
    ACCIDENT_INVOLVING_TRAIN = "accidentInvolvingTrain"
    CHEMICAL_SPILLAGE_ACCIDENT = "chemicalSpillageAccident"
    COLLISION = "collision"
    COLLISION_WITH_ANIMAL = "collisionWithAnimal"
    COLLISION_WITH_OBSTRUCTION = "collisionWithObstruction"
    COLLISION_WITH_PERSON = "collisionWithPerson"
    EARLIER_ACCIDENT = "earlierAccident"
    FUEL_SPILLAGE_ACCIDENT = "fuelSpillageAccident"
    HEAD_ON_COLLISION = "headOnCollision"
    HEAD_ON_OR_SIDE_COLLISION = "headOnOrSideCollision"
    JACKKNIFED_ARTICULATED_LORRY = "jackknifedArticulatedLorry"
    JACKKNIFED_CARAVAN = "jackknifedCaravan"
    JACKKNIFED_TRAILER = "jackknifedTrailer"
    MULTIPLE_VEHICLE_COLLISION = "multipleVehicleCollision"
    MULTIVEHICLE_ACCIDENT = "multivehicleAccident"
    OIL_SPILLAGE_ACCIDENT = "oilSpillageAccident"
    OVERTURNED_HEAVY_LORRY = "overturnedHeavyLorry"
    OVERTURNED_TRAILER = "overturnedTrailer"
    OVERTURNED_VEHICLE = "overturnedVehicle"
    REAR_COLLISION = "rearCollision"
    SECONDARY_ACCIDENT = "secondaryAccident"
    SERIOUS_ACCIDENT = "seriousAccident"
    SIDE_COLLISION = "sideCollision"
    VEHICLE_OFF_ROAD = "vehicleOffRoad"
    VEHICLE_SPUN_AROUND = "vehicleSpunAround"
    OTHER = "other"
