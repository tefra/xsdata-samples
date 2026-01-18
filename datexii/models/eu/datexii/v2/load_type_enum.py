from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class LoadTypeEnum(Enum):
    """
    Types of load carried by a vehicle.

    :cvar ABNORMAL_LOAD: A load that exceeds normal vehicle dimensions
        in terms of height, length, width, gross vehicle weight or axle
        weight or any combination of these. Generally termed an
        "abnormal load".
    :cvar AMMUNITION: Ammunition.
    :cvar CHEMICALS: Chemicals of unspecified type.
    :cvar COMBUSTIBLE_MATERIALS: Combustible materials of unspecified
        type.
    :cvar CORROSIVE_MATERIALS: Corrosive materials of unspecified type.
    :cvar DEBRIS: Debris of unspecified type.
    :cvar EMPTY: No load.
    :cvar EXPLOSIVE_MATERIALS: Explosive materials of unspecified type.
    :cvar EXTRA_HIGH_LOAD: A load of exceptional height.
    :cvar EXTRA_LONG_LOAD: A load of exceptional length.
    :cvar EXTRA_WIDE_LOAD: A load of exceptional width.
    :cvar FUEL: Fuel of unspecified type.
    :cvar GLASS: Glass.
    :cvar GOODS: Any goods of a commercial nature.
    :cvar HAZARDOUS_MATERIALS: Materials classed as being of a hazardous
        nature.
    :cvar LIQUID: Liquid of an unspecified nature.
    :cvar LIVESTOCK: Livestock.
    :cvar MATERIALS: General materials of unspecified type.
    :cvar MATERIALS_DANGEROUS_FOR_PEOPLE: Materials classed as being of
        a danger to people or animals.
    :cvar MATERIALS_DANGEROUS_FOR_THE_ENVIRONMENT: Materials classed as
        being potentially dangerous to the environment.
    :cvar MATERIALS_DANGEROUS_FOR_WATER: Materials classed as being
        dangerous when exposed to water (e.g. materials which may react
        exothermically with water).
    :cvar OIL: Oil.
    :cvar ORDINARY: Materials that present limited environmental or
        health risk. Non-combustible, non-toxic, non-corrosive.
    :cvar PERISHABLE_PRODUCTS: Products or produce that will
        significantly degrade in quality or freshness over a short
        period of time.
    :cvar PETROL: Petrol or petroleum.
    :cvar PHARMACEUTICAL_MATERIALS: Pharmaceutical materials.
    :cvar RADIOACTIVE_MATERIALS: Materials that emit significant
        quantities of electro-magnetic radiation that may present a risk
        to people, animals or the environment.
    :cvar REFUSE: Refuse.
    :cvar TOXIC_MATERIALS: Materials of a toxic nature which may damage
        the environment or endanger public health.
    :cvar VEHICLES: Vehicles of any type which are being transported.
    :cvar OTHER: Other than as defined in this enumeration.
    """

    ABNORMAL_LOAD = "abnormalLoad"
    AMMUNITION = "ammunition"
    CHEMICALS = "chemicals"
    COMBUSTIBLE_MATERIALS = "combustibleMaterials"
    CORROSIVE_MATERIALS = "corrosiveMaterials"
    DEBRIS = "debris"
    EMPTY = "empty"
    EXPLOSIVE_MATERIALS = "explosiveMaterials"
    EXTRA_HIGH_LOAD = "extraHighLoad"
    EXTRA_LONG_LOAD = "extraLongLoad"
    EXTRA_WIDE_LOAD = "extraWideLoad"
    FUEL = "fuel"
    GLASS = "glass"
    GOODS = "goods"
    HAZARDOUS_MATERIALS = "hazardousMaterials"
    LIQUID = "liquid"
    LIVESTOCK = "livestock"
    MATERIALS = "materials"
    MATERIALS_DANGEROUS_FOR_PEOPLE = "materialsDangerousForPeople"
    MATERIALS_DANGEROUS_FOR_THE_ENVIRONMENT = (
        "materialsDangerousForTheEnvironment"
    )
    MATERIALS_DANGEROUS_FOR_WATER = "materialsDangerousForWater"
    OIL = "oil"
    ORDINARY = "ordinary"
    PERISHABLE_PRODUCTS = "perishableProducts"
    PETROL = "petrol"
    PHARMACEUTICAL_MATERIALS = "pharmaceuticalMaterials"
    RADIOACTIVE_MATERIALS = "radioactiveMaterials"
    REFUSE = "refuse"
    TOXIC_MATERIALS = "toxicMaterials"
    VEHICLES = "vehicles"
    OTHER = "other"
