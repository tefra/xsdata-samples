from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime, XmlTime

__NAMESPACE__ = "http://datex2.eu/schema/3/common"


class CalendarWeekWithinMonthEnum1(Enum):
    """
    Calendar week within month (see ISO8601).

    :cvar FIRST_WEEK: Calendar week containing the first of the month.
        Several days of the first week of the month may occur in the
        previous calendar month. By construction, the last week of a
        preceding month can also be the first week of a subsequent
        month.
    :cvar SECOND_WEEK: Second week of the month.
    :cvar THIRD_WEEK: Third week of the month.
    :cvar FOURTH_WEEK: Fourth week of the month.
    :cvar FIFTH_WEEK: Fifth week of the month.
    :cvar SIXTH_WEEK: Sixth week of the month.
    :cvar LAST_WEEK: Last calendar week within month, regardless of its
        actual number. The last calendar week is the week beginning with
        Monday and containing the last of the month.
    :cvar EXTENDED:
    """
    FIRST_WEEK = "firstWeek"
    SECOND_WEEK = "secondWeek"
    THIRD_WEEK = "thirdWeek"
    FOURTH_WEEK = "fourthWeek"
    FIFTH_WEEK = "fifthWeek"
    SIXTH_WEEK = "sixthWeek"
    LAST_WEEK = "lastWeek"
    EXTENDED = "_extended"


class ComparisonOperatorEnum1(Enum):
    """
    Logical comparison operations.

    :cvar EQUAL_TO: Logical comparison operator of "equal to".
    :cvar GREATER_THAN: Logical comparison operator of "greater than".
    :cvar GREATER_THAN_OR_EQUAL_TO: Logical comparison operator of
        "greater than or equal to".
    :cvar LESS_THAN: Logical comparison operator of "less than".
    :cvar LESS_THAN_OR_EQUAL_TO: Logical comparison operator of "less
        than or equal to".
    :cvar EXTENDED:
    """
    EQUAL_TO = "equalTo"
    GREATER_THAN = "greaterThan"
    GREATER_THAN_OR_EQUAL_TO = "greaterThanOrEqualTo"
    LESS_THAN = "lessThan"
    LESS_THAN_OR_EQUAL_TO = "lessThanOrEqualTo"
    EXTENDED = "_extended"


class ComputationMethodEnum1(Enum):
    """
    Types of computational methods used in deriving data values for data sets.

    :cvar
        ARITHMETIC_AVERAGE_OF_SAMPLES_BASED_ON_AFIXED_NUMBER_OF_SAMPLES:
        Arithmetic average of sample values based on a fixed number of
        samples.
    :cvar ARITHMETIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD: Arithmetic
        average of sample values in a time period.
    :cvar HARMONIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD: Harmonic average
        of sample values in a time period.
    :cvar MEDIAN_OF_SAMPLES_IN_ATIME_PERIOD: Median of sample values
        taken over a time period.
    :cvar MOVING_AVERAGE_OF_SAMPLES: Moving average of sample values.
    :cvar EXTENDED:
    """
    ARITHMETIC_AVERAGE_OF_SAMPLES_BASED_ON_AFIXED_NUMBER_OF_SAMPLES = "arithmeticAverageOfSamplesBasedOnAFixedNumberOfSamples"
    ARITHMETIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = "arithmeticAverageOfSamplesInATimePeriod"
    HARMONIC_AVERAGE_OF_SAMPLES_IN_ATIME_PERIOD = "harmonicAverageOfSamplesInATimePeriod"
    MEDIAN_OF_SAMPLES_IN_ATIME_PERIOD = "medianOfSamplesInATimePeriod"
    MOVING_AVERAGE_OF_SAMPLES = "movingAverageOfSamples"
    EXTENDED = "_extended"


class ConfidentialityValueEnum1(Enum):
    """
    Values of confidentiality.

    :cvar INTERNAL_USE: For internal use only of the recipient
        organisation.
    :cvar NO_RESTRICTION: No restriction on usage.
    :cvar RESTRICTED_TO_AUTHORITIES: Restricted for use only by
        authorities.
    :cvar RESTRICTED_TO_AUTHORITIES_AND_TRAFFIC_OPERATORS: Restricted
        for use only by authorities and traffic operators.
    :cvar EXTENDED:
    """
    INTERNAL_USE = "internalUse"
    NO_RESTRICTION = "noRestriction"
    RESTRICTED_TO_AUTHORITIES = "restrictedToAuthorities"
    RESTRICTED_TO_AUTHORITIES_AND_TRAFFIC_OPERATORS = "restrictedToAuthoritiesAndTrafficOperators"
    EXTENDED = "_extended"


class DangerousGoodsRegulationsEnum1(Enum):
    """
    Types of dangerous goods regulations.

    :cvar ADR: European agreement on the international carriage of
        dangerous goods on road.
    :cvar IATA_ICAO: Regulations covering the international
        transportation of dangerous goods issued by the International
        Air Transport Association and the International Civil Aviation
        Organisation.
    :cvar IMO_IMDG: Regulations regarding the transportation of
        dangerous goods on ocean-going vessels issued by the
        International Maritime Organisation.
    :cvar RAILROAD_DANGEROUS_GOODS_BOOK: International regulations
        concerning the international carriage of dangerous goods by
        rail.
    :cvar EXTENDED:
    """
    ADR = "adr"
    IATA_ICAO = "iataIcao"
    IMO_IMDG = "imoImdg"
    RAILROAD_DANGEROUS_GOODS_BOOK = "railroadDangerousGoodsBook"
    EXTENDED = "_extended"


class DayEnum1(Enum):
    """
    Days of the week.

    :cvar MONDAY: Monday.
    :cvar TUESDAY: Tuesday.
    :cvar WEDNESDAY: Wednesday.
    :cvar THURSDAY: Thursday.
    :cvar FRIDAY: Friday.
    :cvar SATURDAY: Saturday.
    :cvar SUNDAY: Sunday.
    :cvar EXTENDED:
    """
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"
    EXTENDED = "_extended"


class DirectionCompassEnum1(Enum):
    """
    Cardinal direction points of the compass.

    :cvar EAST: East.
    :cvar EAST_NORTH_EAST: East north east.
    :cvar EAST_SOUTH_EAST: East south east.
    :cvar NORTH: North.
    :cvar NORTH_EAST: North east.
    :cvar NORTH_NORTH_EAST: North north east.
    :cvar NORTH_NORTH_WEST: North north west.
    :cvar NORTH_WEST: North west.
    :cvar SOUTH: South.
    :cvar SOUTH_EAST: South east.
    :cvar SOUTH_SOUTH_EAST: South south east.
    :cvar SOUTH_SOUTH_WEST: South south west.
    :cvar SOUTH_WEST: South west.
    :cvar WEST: West.
    :cvar WEST_NORTH_WEST: West north west.
    :cvar WEST_SOUTH_WEST: West south west.
    :cvar EXTENDED:
    """
    EAST = "east"
    EAST_NORTH_EAST = "eastNorthEast"
    EAST_SOUTH_EAST = "eastSouthEast"
    NORTH = "north"
    NORTH_EAST = "northEast"
    NORTH_NORTH_EAST = "northNorthEast"
    NORTH_NORTH_WEST = "northNorthWest"
    NORTH_WEST = "northWest"
    SOUTH = "south"
    SOUTH_EAST = "southEast"
    SOUTH_SOUTH_EAST = "southSouthEast"
    SOUTH_SOUTH_WEST = "southSouthWest"
    SOUTH_WEST = "southWest"
    WEST = "west"
    WEST_NORTH_WEST = "westNorthWest"
    WEST_SOUTH_WEST = "westSouthWest"
    EXTENDED = "_extended"


class EmissionClassificationEuroEnum1(Enum):
    """Classification of emission according to the Euro emission classification
    (based on serveral amendments on 1970 Directive 70/220/EEC).

    Note htat vehicleType as well as fuelType are mandatory to provide
    to make this classification explicit.

    :cvar EURO5: Euro 5.
    :cvar EURO5A: Euro 5a.
    :cvar EURO5B: Euro 5b.
    :cvar EURO6: Euro 6.
    :cvar EURO6A: Euro 6a.
    :cvar EURO6B: Euro 6b.
    :cvar EURO6C: Euro 6c.
    :cvar EURO_V: Euro V.
    :cvar EURO_VI: Euro VI.
    :cvar OTHER: Any other level.
    :cvar EXTENDED:
    """
    EURO5 = "euro5"
    EURO5A = "euro5a"
    EURO5B = "euro5b"
    EURO6 = "euro6"
    EURO6A = "euro6a"
    EURO6B = "euro6b"
    EURO6C = "euro6c"
    EURO_V = "euroV"
    EURO_VI = "euroVI"
    OTHER = "other"
    EXTENDED = "_extended"


class FaultSeverityEnum1(Enum):
    """
    Classification of the severity of faults.

    :cvar LOW: The fault is of low severity and has only limited impact
        on the usability of the equipment or the value of the data
        generated by the equipment.
    :cvar MEDIUM: The fault is of medium severity which will
        significantly limit the usability of the equipment or devalue
        the usefulness of the data generated by the equipment.
    :cvar HIGH: The fault is of high severity which will render the
        equipment unusable or any data generated by the equipment to be
        of no value.
    :cvar UNKNOWN: The fault is of unknown severity and hence its effect
        on the usability of the equipment or the usefulness of the data
        generated by the equipment can not be assessed.
    :cvar EXTENDED:
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    UNKNOWN = "unknown"
    EXTENDED = "_extended"


class FaultUrgencyEnum1(Enum):
    """
    Classification of the urgency to rectify a fault.

    :cvar NORMAL: The fault is of normal urgency.
    :cvar URGENT: The fault is to be rectified urgent.
    :cvar EXTREMELY_URGENT: The fault is to be rectified extremely
        urgency.
    :cvar UNKNOWN: The fault is of unknown urgency.
    :cvar EXTENDED:
    """
    NORMAL = "normal"
    URGENT = "urgent"
    EXTREMELY_URGENT = "extremelyUrgent"
    UNKNOWN = "unknown"
    EXTENDED = "_extended"


class FuelTypeEnum1(Enum):
    """
    Type of fuel used by a vehicle.

    :cvar ALL: All sort of fuel is accepted.
    :cvar BATTERY: Battery.
    :cvar BIODIESEL: Biodiesel.
    :cvar DIESEL: Fuel used for compression-ignition (CI) engines.
    :cvar DIESEL_BATTERY_HYBRID: Diesel and battery hybrid.
    :cvar ETHANOL: Ethanol.
    :cvar HYDROGEN: Hydrogen.
    :cvar LIQUID_GAS: Liquid gas of any type including LPG.
    :cvar LPG: Liquid petroleum gas.
    :cvar METHANE: Methane gas.
    :cvar PETROL: Fuel used for positive-ignition (PI) engines.
    :cvar PETROL95_OCTANE: Petrol with 95 octane.
    :cvar PETROL98_OCTANE: Petrol with 98 octane.
    :cvar PETROL_BATTERY_HYBRID: Petrol and battery hybrid.
    :cvar PETROL_LEADED: Leaded petrol.
    :cvar PETROL_UNLEADED: Unleaded petrol.
    :cvar UNKNOWN: The sort of fuel is not known.
    :cvar OTHER: Other.
    :cvar EXTENDED:
    """
    ALL = "all"
    BATTERY = "battery"
    BIODIESEL = "biodiesel"
    DIESEL = "diesel"
    DIESEL_BATTERY_HYBRID = "dieselBatteryHybrid"
    ETHANOL = "ethanol"
    HYDROGEN = "hydrogen"
    LIQUID_GAS = "liquidGas"
    LPG = "lpg"
    METHANE = "methane"
    PETROL = "petrol"
    PETROL95_OCTANE = "petrol95Octane"
    PETROL98_OCTANE = "petrol98Octane"
    PETROL_BATTERY_HYBRID = "petrolBatteryHybrid"
    PETROL_LEADED = "petrolLeaded"
    PETROL_UNLEADED = "petrolUnleaded"
    UNKNOWN = "unknown"
    OTHER = "other"
    EXTENDED = "_extended"


class InformationDeliveryServicesEnum1(Enum):
    """
    List of service channels or devices on which information or data exchanged
    can be delivered.

    :cvar ANY_GENERAL_DELIVERY_SERVICE: Includes any general delivery
        channel such as broadcast channels (e.g. radio, tv, RDS-TMC,
        TPEG services, etc.) or web publishing available to public or to
        specific users, depending on Service Provider policies.
    :cvar SAFETY_SERVICES: Specific services which deliver warning
        alerts to end users to enhance safety via any specific
        application available to drivers, including C-ITS services.
    :cvar VMS: Variable Message Signs or any other visual roadside
        devices which information are accessible to drivers which aim to
        affect driving style improving safety and road network LoS.
    :cvar EXTENDED:
    """
    ANY_GENERAL_DELIVERY_SERVICE = "anyGeneralDeliveryService"
    SAFETY_SERVICES = "safetyServices"
    VMS = "vms"
    EXTENDED = "_extended"


class InformationStatusEnum1(Enum):
    """
    Status of the related information (i.e. real, test or exercise).

    :cvar REAL: The information is real. It is not a test or exercise.
    :cvar SECURITY_EXERCISE: The information is part of an exercise
        which is for testing security.
    :cvar TECHNICAL_EXERCISE: The information is part of an exercise
        which includes tests of associated technical subsystems.
    :cvar TEST: The information is part of a test for checking the
        exchange of this type of information.
    :cvar EXTENDED:
    """
    REAL = "real"
    SECURITY_EXERCISE = "securityExercise"
    TECHNICAL_EXERCISE = "technicalExercise"
    TEST = "test"
    EXTENDED = "_extended"


class InstanceOfDayEnum1(Enum):
    """
    Instances of a day of the week in a month.

    :cvar FIRST_INSTANCE: First instance of specified day of week in
        month.
    :cvar SECOND_INSTANCE: Second instance of specified day of week in
        month.
    :cvar THIRD_INSTANCE: Third instance of specified day of week in
        month.
    :cvar FOURTH_INSTANCE: Fourth instance of specified day of week in
        month.
    :cvar FIFTH_INSTANCE: Fifth instance of specified day of week in
        month.
    :cvar LAST_INSTANCE: Last instance of specified day of week in month
        (regardless its actual instance number).
    :cvar EXTENDED:
    """
    FIRST_INSTANCE = "firstInstance"
    SECOND_INSTANCE = "secondInstance"
    THIRD_INSTANCE = "thirdInstance"
    FOURTH_INSTANCE = "fourthInstance"
    FIFTH_INSTANCE = "fifthInstance"
    LAST_INSTANCE = "lastInstance"
    EXTENDED = "_extended"


class LoadTypeEnum1(Enum):
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
    :cvar REFRIGERATED_GOODS: Refrigerated goods.
    :cvar REFUSE: Refuse.
    :cvar TOXIC_MATERIALS: Materials of a toxic nature which may damage
        the environment or endanger public health.
    :cvar VEHICLES: Vehicles of any type which are being transported.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
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
    MATERIALS_DANGEROUS_FOR_THE_ENVIRONMENT = "materialsDangerousForTheEnvironment"
    MATERIALS_DANGEROUS_FOR_WATER = "materialsDangerousForWater"
    OIL = "oil"
    ORDINARY = "ordinary"
    PERISHABLE_PRODUCTS = "perishableProducts"
    PETROL = "petrol"
    PHARMACEUTICAL_MATERIALS = "pharmaceuticalMaterials"
    RADIOACTIVE_MATERIALS = "radioactiveMaterials"
    REFRIGERATED_GOODS = "refrigeratedGoods"
    REFUSE = "refuse"
    TOXIC_MATERIALS = "toxicMaterials"
    VEHICLES = "vehicles"
    OTHER = "other"
    EXTENDED = "_extended"


class LowEmissionLevelEnum1(Enum):
    """
    The emission level of a vehicle.

    :cvar LOW_LEVEL_EMISSION: Vehicles with low level emission.
    :cvar FREE_OF_EMISSION: Only vehicles that do not produce emissions
        (e.g. electric driven). Hybrid driven cars are allowed, when
        they switch to emission free mode within the considered
        situation.
    :cvar EXTENDED:
    """
    LOW_LEVEL_EMISSION = "lowLevelEmission"
    FREE_OF_EMISSION = "freeOfEmission"
    EXTENDED = "_extended"


class MonthOfYearEnum1(Enum):
    """
    A list of the months of the year.

    :cvar JANUARY: The month of January.
    :cvar FEBRUARY: The month of February.
    :cvar MARCH: The month of March.
    :cvar APRIL: The month of April.
    :cvar MAY: The month of May.
    :cvar JUNE: The month of June.
    :cvar JULY: The month of July.
    :cvar AUGUST: The month of August.
    :cvar SEPTEMBER: The month of September.
    :cvar OCTOBER: The month of October.
    :cvar NOVEMBER: The month of November.
    :cvar DECEMBER: The month of December.
    :cvar EXTENDED:
    """
    JANUARY = "january"
    FEBRUARY = "february"
    MARCH = "march"
    APRIL = "april"
    MAY = "may"
    JUNE = "june"
    JULY = "july"
    AUGUST = "august"
    SEPTEMBER = "september"
    OCTOBER = "october"
    NOVEMBER = "november"
    DECEMBER = "december"
    EXTENDED = "_extended"


@dataclass
class MultilingualStringValue:
    value: Optional[str] = field(
        default=None,
        metadata={
            "max_length": 1024,
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


class PollutantTypeEnum1(Enum):
    """
    Types of pollutant that can be measured in the atmosphere.

    :cvar BENZENE_TOLUENE_XYLENE: Benzene, toluene or xylene.
    :cvar CARBON_MONOXIDE: Carbon monoxide.
    :cvar LEAD: Lead.
    :cvar METHANE: Methane.
    :cvar NITRIC_OXIDE: Nitric oxide.
    :cvar NITROGEN_DIOXIDE: Nitrogen dioxide.
    :cvar NITROGEN_MONOXIDE: Nitrogen monoxide.
    :cvar NITROGEN_OXIDES: Nitrogen oxides.
    :cvar NON_METHANE_HYDROCARBONS: Non-methane hydrocarbons.
    :cvar OZONE: Ozone.
    :cvar PARTICULATES10: Particulate matter which passes through a
        size-selective inlet with a 50% cut-off efficiency at an
        aerodynamic diameter of 10 µm (micrometres).
    :cvar POLYCYCLIC_AROMATIC_HYDROCARBONS: Polycyclic aromatic
        hydrocarbons.
    :cvar PRIMARY_PARTICULATE: Primary particulate particles.
    :cvar SULPHUR_DIOXIDE: Sulphur dioxide.
    :cvar TOTAL_HYDROCARBONS: Total hydrocarbons, i.e. including methane
        and non-methane.
    :cvar EXTENDED:
    """
    BENZENE_TOLUENE_XYLENE = "benzeneTolueneXylene"
    CARBON_MONOXIDE = "carbonMonoxide"
    LEAD = "lead"
    METHANE = "methane"
    NITRIC_OXIDE = "nitricOxide"
    NITROGEN_DIOXIDE = "nitrogenDioxide"
    NITROGEN_MONOXIDE = "nitrogenMonoxide"
    NITROGEN_OXIDES = "nitrogenOxides"
    NON_METHANE_HYDROCARBONS = "nonMethaneHydrocarbons"
    OZONE = "ozone"
    PARTICULATES10 = "particulates10"
    POLYCYCLIC_AROMATIC_HYDROCARBONS = "polycyclicAromaticHydrocarbons"
    PRIMARY_PARTICULATE = "primaryParticulate"
    SULPHUR_DIOXIDE = "sulphurDioxide"
    TOTAL_HYDROCARBONS = "totalHydrocarbons"
    EXTENDED = "_extended"


class PrecipitationIntensityEnum1(Enum):
    """
    Intensity of precipitation.

    :cvar NO_PHENOMENA: No precipitation phenomena.
    :cvar LIGHT: Light precipitation.
    :cvar MODERATE: Moderate precipitation.
    :cvar HEAVY: Heavy precipitation.
    :cvar VIOLENT: Violent precipitation.
    :cvar SEVERE: #
    :cvar EXTENDED:
    """
    NO_PHENOMENA = "noPhenomena"
    LIGHT = "light"
    MODERATE = "moderate"
    HEAVY = "heavy"
    VIOLENT = "violent"
    SEVERE = "severe"
    EXTENDED = "_extended"


class PrecipitationTypeEnum1(Enum):
    """
    Types of precipitation.

    :cvar CLEAR_ICE: Clear ice.
    :cvar DEW: Dew.
    :cvar DIAMOND_DUST: Diamond dust.
    :cvar DRIZZLE: Light, fine rain.
    :cvar FREEZING_RAIN: Freezing rain.
    :cvar GLAZE: Glaze.
    :cvar HAIL: Small balls of ice and compacted snow.
    :cvar HARD_RIME: Hard rime.
    :cvar HOAR_FROST: Hoar frost.
    :cvar ICE_CRYSTALS: Ice crystals.
    :cvar ICE_PELLETS: Ice pellets.
    :cvar LIQUID_FREEZING: Liquid, freezing precipitation.
    :cvar LIQUID_NOT_FREEZING: Liquid precipitation but not freezing.
    :cvar NO_PRECIPITATION: No precipitation.
    :cvar RAIN: Rain.
    :cvar RIME: Rime.
    :cvar SLEET: Wet snow mixed with rain.
    :cvar SMALL_HAIL: Small Hail.
    :cvar SNOW: Snow.
    :cvar SNOW_GRAINS: Snow grains.
    :cvar SNOW_PELLETS: Snow pellets.
    :cvar SOFT_RIME: Soft rime.
    :cvar SOLID: Solid precipitation.
    :cvar WET_SNOW: Wet snow.
    :cvar WHITE_DEV: White Dev.
    :cvar UNKNOWN: Unknown type of precipitation.
    :cvar EXTENDED:
    """
    CLEAR_ICE = "clearIce"
    DEW = "dew"
    DIAMOND_DUST = "diamondDust"
    DRIZZLE = "drizzle"
    FREEZING_RAIN = "freezingRain"
    GLAZE = "glaze"
    HAIL = "hail"
    HARD_RIME = "hardRime"
    HOAR_FROST = "hoarFrost"
    ICE_CRYSTALS = "iceCrystals"
    ICE_PELLETS = "icePellets"
    LIQUID_FREEZING = "liquidFreezing"
    LIQUID_NOT_FREEZING = "liquidNotFreezing"
    NO_PRECIPITATION = "noPrecipitation"
    RAIN = "rain"
    RIME = "rime"
    SLEET = "sleet"
    SMALL_HAIL = "smallHail"
    SNOW = "snow"
    SNOW_GRAINS = "snowGrains"
    SNOW_PELLETS = "snowPellets"
    SOFT_RIME = "softRime"
    SOLID = "solid"
    WET_SNOW = "wetSnow"
    WHITE_DEV = "whiteDev"
    UNKNOWN = "unknown"
    EXTENDED = "_extended"


class PublicEventTypeEnum1(Enum):
    """
    Types of public events.

    :cvar AGRICULTURAL_SHOW: Agricultural show or event which could
        disrupt traffic.
    :cvar AIR_SHOW: Air show or other aeronautical event which could
        disrupt traffic.
    :cvar ART_EVENT: Art event
    :cvar ATHLETICS_MEETING: Athletics event that could disrupt traffic.
    :cvar COMMERCIAL_EVENT: Commercial event which could disrupt
        traffic.
    :cvar CULTURAL_EVENT: Cultural event which could disrupt traffic.
    :cvar BALL_GAME: Ball game event that could disrupt traffic.
    :cvar BASEBALL_GAME: Baseball game event that could disrupt traffic.
    :cvar BASKETBALL_GAME: Basketball game event that could disrupt
        traffic.
    :cvar BEER_FESTIVAL: Beer festival
    :cvar BICYCLE_RACE: Bicycle race that could disrupt traffic.
    :cvar BOAT_RACE: Regatta (boat race event of sailing, powerboat or
        rowing) that could disrupt traffic.
    :cvar BOAT_SHOW: Boat show which could disrupt traffic.
    :cvar BOXING_TOURNAMENT: Boxing event that could disrupt traffic.
    :cvar BULL_FIGHT: Bull fighting event that could disrupt traffic.
    :cvar CEREMONIAL_EVENT: Formal or religious act, rite or ceremony
        that could disrupt traffic.
    :cvar CONCERT: Concert event that could disrupt traffic.
    :cvar CRICKET_MATCH: Cricket match that could disrupt traffic.
    :cvar EXHIBITION: Major display or trade show which could disrupt
        traffic.
    :cvar FAIR: Periodic (e.g. annual), often traditional, gathering for
        entertainment or trade promotion, which could disrupt traffic.
    :cvar FESTIVAL: Celebratory event or series of events which could
        disrupt traffic.
    :cvar FILM_FESTIVAL: Film festival
    :cvar FILM_TVMAKING: Film or TV making event which could disrupt
        traffic.
    :cvar FIREWORK_DISPLAY: Firework display
    :cvar FLOWER_EVENT: Flower event
    :cvar FOOD_FESTIVAL: Food festival
    :cvar FOOTBALL_MATCH: Football match that could disrupt traffic.
    :cvar FUNFAIR: Periodic (e.g. annual), often traditional, gathering
        for entertainment, which could disrupt traffic.
    :cvar GARDENING_OR_FLOWER_SHOW: Gardening and/or flower show or
        event which could disrupt traffic.
    :cvar GOLF_TOURNAMENT: Golf tournament event that could disrupt
        traffic.
    :cvar HOCKEY_GAME: Hockey game event that could disrupt traffic.
    :cvar HORSE_RACE_MEETING: Horse race meeting that could disrupt
        traffic.
    :cvar INTERNATIONAL_SPORTS_MEETING: Large sporting event of an
        international nature that could disrupt traffic.
    :cvar MAJOR_EVENT: Significant organised event either on or near the
        roadway which could disrupt traffic.
    :cvar MARATHON: Marathon, cross-country or road running event that
        could disrupt traffic.
    :cvar MARKET: Periodic (e.g. weekly) gathering for buying and
        selling, which could disrupt traffic.
    :cvar MATCH: Sports match of unspecified type that could disrupt
        traffic.
    :cvar MOTOR_SHOW: Motor show which could disrupt traffic.
    :cvar MOTOR_SPORT_RACE_MEETING: Motor sport race meeting that could
        disrupt traffic.
    :cvar OPEN_AIR_CONCERT: Open air concert
    :cvar PARADE: Formal display or organised procession which could
        disrupt traffic.
    :cvar PROCESSION: An organised procession which could disrupt
        traffic.
    :cvar RACE_MEETING: Race meeting (other than horse or motor sport)
        that could disrupt traffic.
    :cvar RUGBY_MATCH: Rugby match that could disrupt traffic.
    :cvar SEVERAL_MAJOR_EVENTS: A series of significant organised events
        either on or near the roadway which could disrupt traffic.
    :cvar SHOW: Entertainment event that could disrupt traffic.
    :cvar SHOW_JUMPING: Horse showing jumping and tournament event that
        could disrupt traffic.
    :cvar SOUND_AND_LIGHT_SHOW: Sound and light show.
    :cvar SPORTS_MEETING: Sports event of unspecified type that could
        disrupt traffic.
    :cvar STATE_OCCASION: Public ceremony or visit of national or
        international significance which could disrupt traffic.
    :cvar STREET_FESTIVAL: Street festival
    :cvar TENNIS_TOURNAMENT: Tennis tournament that could disrupt
        traffic.
    :cvar THEATRICAL_EVENT: Theatrical event
    :cvar TOURNAMENT: Sporting event or series of events of unspecified
        type lasting more than one day which could disrupt traffic.
    :cvar TRADE_FAIR: A periodic (e.g. annual), often traditional,
        gathering for trade promotion, which could disrupt traffic.
    :cvar WATER_SPORTS_MEETING: Water sports meeting that could disrupt
        traffic.
    :cvar WINE_FESTIVAL: Wine festival
    :cvar WINTER_SPORTS_MEETING: Winter sports meeting or event (e.g.
        skiing, ski jumping, skating) that could disrupt traffic.
    :cvar UNKNOWN: Service provider does not know at time of message
        generation.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    AGRICULTURAL_SHOW = "agriculturalShow"
    AIR_SHOW = "airShow"
    ART_EVENT = "artEvent"
    ATHLETICS_MEETING = "athleticsMeeting"
    COMMERCIAL_EVENT = "commercialEvent"
    CULTURAL_EVENT = "culturalEvent"
    BALL_GAME = "ballGame"
    BASEBALL_GAME = "baseballGame"
    BASKETBALL_GAME = "basketballGame"
    BEER_FESTIVAL = "beerFestival"
    BICYCLE_RACE = "bicycleRace"
    BOAT_RACE = "boatRace"
    BOAT_SHOW = "boatShow"
    BOXING_TOURNAMENT = "boxingTournament"
    BULL_FIGHT = "bullFight"
    CEREMONIAL_EVENT = "ceremonialEvent"
    CONCERT = "concert"
    CRICKET_MATCH = "cricketMatch"
    EXHIBITION = "exhibition"
    FAIR = "fair"
    FESTIVAL = "festival"
    FILM_FESTIVAL = "filmFestival"
    FILM_TVMAKING = "filmTVMaking"
    FIREWORK_DISPLAY = "fireworkDisplay"
    FLOWER_EVENT = "flowerEvent"
    FOOD_FESTIVAL = "foodFestival"
    FOOTBALL_MATCH = "footballMatch"
    FUNFAIR = "funfair"
    GARDENING_OR_FLOWER_SHOW = "gardeningOrFlowerShow"
    GOLF_TOURNAMENT = "golfTournament"
    HOCKEY_GAME = "hockeyGame"
    HORSE_RACE_MEETING = "horseRaceMeeting"
    INTERNATIONAL_SPORTS_MEETING = "internationalSportsMeeting"
    MAJOR_EVENT = "majorEvent"
    MARATHON = "marathon"
    MARKET = "market"
    MATCH = "match"
    MOTOR_SHOW = "motorShow"
    MOTOR_SPORT_RACE_MEETING = "motorSportRaceMeeting"
    OPEN_AIR_CONCERT = "openAirConcert"
    PARADE = "parade"
    PROCESSION = "procession"
    RACE_MEETING = "raceMeeting"
    RUGBY_MATCH = "rugbyMatch"
    SEVERAL_MAJOR_EVENTS = "severalMajorEvents"
    SHOW = "show"
    SHOW_JUMPING = "showJumping"
    SOUND_AND_LIGHT_SHOW = "soundAndLightShow"
    SPORTS_MEETING = "sportsMeeting"
    STATE_OCCASION = "stateOccasion"
    STREET_FESTIVAL = "streetFestival"
    TENNIS_TOURNAMENT = "tennisTournament"
    THEATRICAL_EVENT = "theatricalEvent"
    TOURNAMENT = "tournament"
    TRADE_FAIR = "tradeFair"
    WATER_SPORTS_MEETING = "waterSportsMeeting"
    WINE_FESTIVAL = "wineFestival"
    WINTER_SPORTS_MEETING = "winterSportsMeeting"
    UNKNOWN = "unknown"
    OTHER = "other"
    EXTENDED = "_extended"


@dataclass
class Reference:
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


class SourceTypeEnum1(Enum):
    """
    Type of sources from which situation information may be derived.

    :cvar AUTOMOBILE_CLUB_PATROL: A patrol of an automobile club.
    :cvar CAMERA_OBSERVATION: A camera observation (either still or
        video camera).
    :cvar FREIGHT_VEHICLE_OPERATOR: An operator of freight vehicles.
    :cvar INDUCTION_LOOP_MONITORING_STATION: A station dedicated to the
        monitoring of the road network by processing inductive loop
        information.
    :cvar INFRARED_MONITORING_STATION: A station dedicated to the
        monitoring of the road network by processing infrared image
        information.
    :cvar MICROWAVE_MONITORING_STATION: A station dedicated to the
        monitoring of the road network by processing microwave
        information.
    :cvar MOBILE_TELEPHONE_CALLER: A caller using a mobile telephone
        (who may be or not on the road network).
    :cvar NON_POLICE_EMERGENCY_SERVICE_PATROL: Emergency service patrols
        other than police.
    :cvar OTHER_INFORMATION: Other sources of information.
    :cvar OTHER_OFFICIAL_VEHICLE: Personnel from a vehicle belonging to
        the road operator or authority or any emergency service,
        including authorised breakdown service organisations.
    :cvar POLICE_PATROL: A police patrol.
    :cvar PRIVATE_BREAKDOWN_SERVICE: A private breakdown service.
    :cvar PUBLIC_AND_PRIVATE_UTILITIES: A utility organisation, either
        public or private.
    :cvar REGISTERED_MOTORIST_OBSERVER: A motorist who is an officially
        registered observer.
    :cvar ROAD_AUTHORITIES: A road authority.
    :cvar ROAD_OPERATOR_PATROL: A patrol of the road operator or
        authority.
    :cvar ROADSIDE_TELEPHONE_CALLER: A caller who is using an emergency
        roadside telephone.
    :cvar SPOTTER_AIRCRAFT: A spotter aircraft of an organisation
        specifically assigned to the monitoring of the traffic network.
    :cvar TRAFFIC_MONITORING_STATION: A station, usually automatic,
        dedicated to the monitoring of the road network.
    :cvar TRANSIT_OPERATOR: An operator of a transit service, e.g. bus
        link operator.
    :cvar VEHICLE_PROBE_MEASUREMENT: A specially equipped vehicle used
        to provide measurements.
    :cvar VIDEO_PROCESSING_MONITORING_STATION: A station dedicated to
        the monitoring of the road network by processing video image
        information.
    :cvar EXTENDED:
    """
    AUTOMOBILE_CLUB_PATROL = "automobileClubPatrol"
    CAMERA_OBSERVATION = "cameraObservation"
    FREIGHT_VEHICLE_OPERATOR = "freightVehicleOperator"
    INDUCTION_LOOP_MONITORING_STATION = "inductionLoopMonitoringStation"
    INFRARED_MONITORING_STATION = "infraredMonitoringStation"
    MICROWAVE_MONITORING_STATION = "microwaveMonitoringStation"
    MOBILE_TELEPHONE_CALLER = "mobileTelephoneCaller"
    NON_POLICE_EMERGENCY_SERVICE_PATROL = "nonPoliceEmergencyServicePatrol"
    OTHER_INFORMATION = "otherInformation"
    OTHER_OFFICIAL_VEHICLE = "otherOfficialVehicle"
    POLICE_PATROL = "policePatrol"
    PRIVATE_BREAKDOWN_SERVICE = "privateBreakdownService"
    PUBLIC_AND_PRIVATE_UTILITIES = "publicAndPrivateUtilities"
    REGISTERED_MOTORIST_OBSERVER = "registeredMotoristObserver"
    ROAD_AUTHORITIES = "roadAuthorities"
    ROAD_OPERATOR_PATROL = "roadOperatorPatrol"
    ROADSIDE_TELEPHONE_CALLER = "roadsideTelephoneCaller"
    SPOTTER_AIRCRAFT = "spotterAircraft"
    TRAFFIC_MONITORING_STATION = "trafficMonitoringStation"
    TRANSIT_OPERATOR = "transitOperator"
    VEHICLE_PROBE_MEASUREMENT = "vehicleProbeMeasurement"
    VIDEO_PROCESSING_MONITORING_STATION = "videoProcessingMonitoringStation"
    EXTENDED = "_extended"


class SpecialDayTypeEnum1(Enum):
    """
    Collection of special types of days.

    :cvar DAY_BEFORE_PUBLIC_HOLIDAY: The day preceding a public holiday.
    :cvar PUBLIC_HOLIDAY: A public holiday in general. You may use the
        PublicHoliday class to refer on a specific public holiday.
    :cvar DAY_FOLLOWING_PUBLIC_HOLIDAY: A day following a public
        holiday.
    :cvar LONG_WEEKEND_DAY: A day between a public holiday and the
        weekend.
    :cvar IN_LIEU_OF_PUBLIC_HOLIDAY: A holiday in lieu of a public
        holiday that falls on a weekend.
    :cvar SCHOOL_DAY: A school day.
    :cvar SCHOOL_HOLIDAYS: A day within the school holidays.
    :cvar PUBLIC_EVENT_DAY: A day of a public event. You may use the
        publicEvent attribute to specify the corresponding event.
    :cvar OTHER: Some other special day.
    :cvar EXTENDED:
    """
    DAY_BEFORE_PUBLIC_HOLIDAY = "dayBeforePublicHoliday"
    PUBLIC_HOLIDAY = "publicHoliday"
    DAY_FOLLOWING_PUBLIC_HOLIDAY = "dayFollowingPublicHoliday"
    LONG_WEEKEND_DAY = "longWeekendDay"
    IN_LIEU_OF_PUBLIC_HOLIDAY = "inLieuOfPublicHoliday"
    SCHOOL_DAY = "schoolDay"
    SCHOOL_HOLIDAYS = "schoolHolidays"
    PUBLIC_EVENT_DAY = "publicEventDay"
    OTHER = "other"
    EXTENDED = "_extended"


class TimePrecisionEnum1(Enum):
    """
    List of precisions to which times can be given.

    :cvar TENTHS_OF_SECOND: Time given to the nearest tenth of a second.
    :cvar SECOND: Time given to the nearest second.
    :cvar MINUTE: Time given to the nearest minute.
    :cvar QUARTER_HOUR: Time given to the nearest quarter hour.
    :cvar HALF_HOUR: Time given to the nearest half hour.
    :cvar HOUR: Time given to the nearest hour.
    :cvar EXTENDED:
    """
    TENTHS_OF_SECOND = "tenthsOfSecond"
    SECOND = "second"
    MINUTE = "minute"
    QUARTER_HOUR = "quarterHour"
    HALF_HOUR = "halfHour"
    HOUR = "hour"
    EXTENDED = "_extended"


class TrafficTrendTypeEnum1(Enum):
    """
    List of terms used to describe the trend in traffic conditions.

    :cvar TRAFFIC_BUILDING_UP: Traffic conditions are changing from
        free-flow to heavy or slow service levels.  Queues may also be
        expected.
    :cvar TRAFFIC_EASING: Traffic conditions are changing from heavy or
        slow service levels to free-flow.
    :cvar TRAFFIC_STABLE: Traffic conditions are currently stable.
    :cvar UNKNOWN: The trend of traffic conditions is currently unknown.
    :cvar EXTENDED:
    """
    TRAFFIC_BUILDING_UP = "trafficBuildingUp"
    TRAFFIC_EASING = "trafficEasing"
    TRAFFIC_STABLE = "trafficStable"
    UNKNOWN = "unknown"
    EXTENDED = "_extended"


class UrlLinkTypeEnum1(Enum):
    """
    Types of URL links.

    :cvar DOCUMENT_PDF: URL link to a pdf document.
    :cvar HTML: URL link to an html page.
    :cvar IMAGE: URL link to an image.
    :cvar RSS: URL link to an RSS feed.
    :cvar VIDEO_STREAM: URL link to a video stream.
    :cvar VOICE_STREAM: URL link to a voice stream.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    DOCUMENT_PDF = "documentPdf"
    HTML = "html"
    IMAGE = "image"
    RSS = "rss"
    VIDEO_STREAM = "videoStream"
    VOICE_STREAM = "voiceStream"
    OTHER = "other"
    EXTENDED = "_extended"


class ValidityStatusEnum1(Enum):
    """
    Values of validity status that can be assigned to a described event, action
    or item.

    :cvar ACTIVE: The described event, action or item is currently
        active regardless of the definition of the validity time
        specification.
    :cvar PLANNED: The described event, action or item is currently
        planned regardless of the definition of the validity time
        specification.
    :cvar SUSPENDED: The described event, action or item is currently
        suspended, that is inactive, regardless of the definition of the
        validity time specification.
    :cvar DEFINED_BY_VALIDITY_TIME_SPEC: The validity status of the
        described event, action or item is in accordance with the
        definition of the validity time specification.
    :cvar EXTENDED:
    """
    ACTIVE = "active"
    PLANNED = "planned"
    SUSPENDED = "suspended"
    DEFINED_BY_VALIDITY_TIME_SPEC = "definedByValidityTimeSpec"
    EXTENDED = "_extended"


class VehicleEquipmentEnum1(Enum):
    """
    Types of vehicle equipment in use or on board.

    :cvar NOT_USING_SNOW_CHAINS: Vehicle not using snow chains.
    :cvar NOT_USING_SNOW_CHAINS_OR_TYRES: Vehicle not using either snow
        tyres or snow chains.
    :cvar SNOW_CHAINS_IN_USE: Vehicle using snow chains.
    :cvar SNOW_TYRES_IN_USE: Vehicle using snow tyres.
    :cvar SNOW_CHAINS_OR_TYRES_IN_USE: Vehicle using snow tyres or snow
        chains.
    :cvar WITHOUT_SNOW_TYRES_OR_CHAINS_ON_BOARD: Vehicle which is not
        carrying on board snow tyres or chains.
    :cvar EXTENDED:
    """
    NOT_USING_SNOW_CHAINS = "notUsingSnowChains"
    NOT_USING_SNOW_CHAINS_OR_TYRES = "notUsingSnowChainsOrTyres"
    SNOW_CHAINS_IN_USE = "snowChainsInUse"
    SNOW_TYRES_IN_USE = "snowTyresInUse"
    SNOW_CHAINS_OR_TYRES_IN_USE = "snowChainsOrTyresInUse"
    WITHOUT_SNOW_TYRES_OR_CHAINS_ON_BOARD = "withoutSnowTyresOrChainsOnBoard"
    EXTENDED = "_extended"


class VehicleStatusEnum1(Enum):
    """
    The status of a vehicle.

    :cvar ABANDONED: Abandoned vehicle.
    :cvar BROKEN_DOWN: Broken down vehicle (i.e. it is immobile due to
        mechanical breakdown).
    :cvar BURNT_OUT: Burnt out vehicle, but fire is extinguished.
    :cvar DAMAGED: Vehicle is damaged following an incident or
        collision. It may be able or not to move by itself.
    :cvar DAMAGED_AND_IMMOBILIZED: Vehicle is damaged following an
        incident or collision. It is immobilized and therefore needs
        assistance to be moved.
    :cvar IN_DITCH: Vehicle has left roadway and ended in a ditch next
        to the roadway
    :cvar JACKNIFED: The pulling vehicle is in a jackknifed position
        with its trailer
    :cvar OFF_ROAD: Vehicle has left the carriageway
    :cvar ON_FIRE: Vehicle is on fire.
    :cvar ON_TOP_OF_CRASH_BARRIER: Vehicle is on top of the crash
        barrier, and cannot leave that position autonomously
    :cvar ON_WHEELS: Vehicle is in its upright position after the
        accident. No special lifting equipment is needed to put it on
        its wheels
    :cvar OVERTURNED: Vehicle is on its side or upside down
    :cvar ROLLABLE: The vehicle can be rolled on its own wheels. There
        is no special equipment needed to lift the vehicle, because of
        blocked wheels or other mechanical problems.
    :cvar SPUN_AROUND: Vehicle has come to rest not facing its intended
        line of travel.
    :cvar EXTENDED:
    """
    ABANDONED = "abandoned"
    BROKEN_DOWN = "brokenDown"
    BURNT_OUT = "burntOut"
    DAMAGED = "damaged"
    DAMAGED_AND_IMMOBILIZED = "damagedAndImmobilized"
    IN_DITCH = "inDitch"
    JACKNIFED = "jacknifed"
    OFF_ROAD = "offRoad"
    ON_FIRE = "onFire"
    ON_TOP_OF_CRASH_BARRIER = "onTopOfCrashBarrier"
    ON_WHEELS = "onWheels"
    OVERTURNED = "overturned"
    ROLLABLE = "rollable"
    SPUN_AROUND = "spunAround"
    EXTENDED = "_extended"


class VehicleTypeEnum1(Enum):
    """
    Types of vehicle.

    :cvar AGRICULTURAL_VEHICLE: Vehicle normally used for agricultural
        purposes, e.g. tractor, combined harvester etc.
    :cvar ANY_VEHICLE: Vehicle of any type.
    :cvar ARTICULATED_BUS: Articulated bus
    :cvar ARTICULATED_TROLLEY_BUS: Articulated trolley bus
    :cvar ARTICULATED_VEHICLE: Articulated vehicle.
    :cvar BICYCLE: Bicycle.
    :cvar BUS: Bus.
    :cvar CAR: Vehicles designed and constructed for the carriage of
        passengers and comprising no more than eight seats in addition
        to the driver’s seat, and having a maximum mass (“technically
        permissible maximum laden mass”) not exceeding 3.5 tons (M1).
    :cvar CARAVAN: Caravan.
    :cvar CAR_OR_LIGHT_VEHICLE: Car or light vehicle.
    :cvar CAR_WITH_CARAVAN: Car towing a caravan.
    :cvar CAR_WITH_TRAILER: Car towing a trailer.
    :cvar CONSTRUCTION_OR_MAINTENANCE_VEHICLE: Vehicle normally used for
        construction or maintenance purposes, e.g. digger, excavator,
        bulldozer, lorry mounted crane etc.
    :cvar FOUR_WHEEL_DRIVE: Four wheel drive vehicle.
    :cvar HEAVY_GOODS_VEHICLE: Vehicles with a total weight above 3,500
        kg (vehicle and load).
    :cvar HEAVY_GOODS_VEHICLE_WITH_TRAILER: Heavy goods vehicle with
        trailer
    :cvar HEAVY_DUTY_TRANSPORTER: A transporter for heavy duty (usually
        with abnormal dimensions).
    :cvar HEAVY_VEHICLE: Vehicle whose weight means it should be classed
        as a heavy vehicle
    :cvar HIGH_SIDED_VEHICLE: High sided vehicle.
    :cvar LIGHT_COMMERCIAL_VEHICLE: Vehicles for the carriage of goods
        and having a maximum mass not exceeding 3.5 tonnes (class N1).
    :cvar LARGE_CAR: Large car
    :cvar LARGE_GOODS_VEHICLE: Vehicles for the carriage of goods and
        having a maximum mass exceeding 3.5 tonnes (belonging to class
        N2 when not exceeding 12 tonnes, otherwise class N3).
    :cvar LIGHT_COMMERCIAL_VEHICLE_WITH_TRAILER: Light goods vehicle
        with trailer
    :cvar LONG_HEAVY_LORRY: A heavy lorry that is longer than normal.
    :cvar LORRY: Lorry of any type.
    :cvar METRO: Metro
    :cvar MINIBUS: Vehicles designed and constructed for the carriage of
        passengers, comprising more than eight seats in addition to the
        driver’s seat, and having a maximum mass not exceeding 5 tonnes
        (class M2).
    :cvar MOPED: Moped (a two wheeled motor vehicle characterized by a
        small engine typically less than 50cc and by normally having
        pedals).
    :cvar MOTORCYCLE: Motorcycle.
    :cvar MOTORCYCLE_WITH_SIDE_CAR: Three wheeled vehicle comprising a
        motorcycle with an attached side car.
    :cvar MOTORHOME: Motorhome
    :cvar MOTORSCOOTER: Motorscooter (a two wheeled motor vehicle
        characterized by a step-through frame and small diameter
        wheels).
    :cvar PASSENGER_CAR: Passenger car
    :cvar SMALL_CAR: Small car
    :cvar TANKER: Vehicle with large tank for carrying bulk liquids.
    :cvar THREE_WHEELED_VEHICLE: Three wheeled vehicle of unspecified
        type.
    :cvar TRAILER: Trailer.
    :cvar TRAM: Tram.
    :cvar TROLLEY_BUS: Trolley bus
    :cvar TWO_WHEELED_VEHICLE: Two wheeled vehicle of unspecified type.
    :cvar VAN: Van.
    :cvar VEHICLE_WITH_CARAVAN: Vehicle (of unspecified type) towing a
        caravan.
    :cvar VEHICLE_WITH_CATALYTIC_CONVERTER: Vehicle with catalytic
        converter.
    :cvar VEHICLE_WITHOUT_CATALYTIC_CONVERTER: Vehicle without catalytic
        converter.
    :cvar VEHICLE_WITH_TRAILER: Vehicle (of unspecified type) towing a
        trailer.
    :cvar WITH_EVEN_NUMBERED_REGISTRATION_PLATES: Vehicle with even
        numbered registration plate.
    :cvar WITH_ODD_NUMBERED_REGISTRATION_PLATES: Vehicle with odd
        numbered registration plate.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    AGRICULTURAL_VEHICLE = "agriculturalVehicle"
    ANY_VEHICLE = "anyVehicle"
    ARTICULATED_BUS = "articulatedBus"
    ARTICULATED_TROLLEY_BUS = "articulatedTrolleyBus"
    ARTICULATED_VEHICLE = "articulatedVehicle"
    BICYCLE = "bicycle"
    BUS = "bus"
    CAR = "car"
    CARAVAN = "caravan"
    CAR_OR_LIGHT_VEHICLE = "carOrLightVehicle"
    CAR_WITH_CARAVAN = "carWithCaravan"
    CAR_WITH_TRAILER = "carWithTrailer"
    CONSTRUCTION_OR_MAINTENANCE_VEHICLE = "constructionOrMaintenanceVehicle"
    FOUR_WHEEL_DRIVE = "fourWheelDrive"
    HEAVY_GOODS_VEHICLE = "heavyGoodsVehicle"
    HEAVY_GOODS_VEHICLE_WITH_TRAILER = "heavyGoodsVehicleWithTrailer"
    HEAVY_DUTY_TRANSPORTER = "heavyDutyTransporter"
    HEAVY_VEHICLE = "heavyVehicle"
    HIGH_SIDED_VEHICLE = "highSidedVehicle"
    LIGHT_COMMERCIAL_VEHICLE = "lightCommercialVehicle"
    LARGE_CAR = "largeCar"
    LARGE_GOODS_VEHICLE = "largeGoodsVehicle"
    LIGHT_COMMERCIAL_VEHICLE_WITH_TRAILER = "lightCommercialVehicleWithTrailer"
    LONG_HEAVY_LORRY = "longHeavyLorry"
    LORRY = "lorry"
    METRO = "metro"
    MINIBUS = "minibus"
    MOPED = "moped"
    MOTORCYCLE = "motorcycle"
    MOTORCYCLE_WITH_SIDE_CAR = "motorcycleWithSideCar"
    MOTORHOME = "motorhome"
    MOTORSCOOTER = "motorscooter"
    PASSENGER_CAR = "passengerCar"
    SMALL_CAR = "smallCar"
    TANKER = "tanker"
    THREE_WHEELED_VEHICLE = "threeWheeledVehicle"
    TRAILER = "trailer"
    TRAM = "tram"
    TROLLEY_BUS = "trolleyBus"
    TWO_WHEELED_VEHICLE = "twoWheeledVehicle"
    VAN = "van"
    VEHICLE_WITH_CARAVAN = "vehicleWithCaravan"
    VEHICLE_WITH_CATALYTIC_CONVERTER = "vehicleWithCatalyticConverter"
    VEHICLE_WITHOUT_CATALYTIC_CONVERTER = "vehicleWithoutCatalyticConverter"
    VEHICLE_WITH_TRAILER = "vehicleWithTrailer"
    WITH_EVEN_NUMBERED_REGISTRATION_PLATES = "withEvenNumberedRegistrationPlates"
    WITH_ODD_NUMBERED_REGISTRATION_PLATES = "withOddNumberedRegistrationPlates"
    UNKNOWN = "unknown"
    OTHER = "other"
    EXTENDED = "_extended"


class VehicleUsageEnum1(Enum):
    """
    Types of usage of a vehicle.

    :cvar AGRICULTURAL: Vehicle used for agricultural purposes.
    :cvar CAR_SHARING: Vehicles operated by a car-sharing company.
    :cvar CITY_LOGISTICS: Vehicles that are used to deliver goods in a
        city area.
    :cvar COMMERCIAL: Vehicle which is limited to non-private usage or
        public transport usage.
    :cvar EMERGENCY_SERVICES: Vehicle used by the emergency services.
    :cvar MILITARY: Vehicle used by the military.
    :cvar NON_COMMERCIAL: Vehicle used for non-commercial or private
        purposes.
    :cvar PATROL: Vehicle used as part of a patrol service, e.g. road
        operator or automobile association patrol vehicle.
    :cvar RECOVERY_SERVICES: Vehicle used to provide a recovery service.
    :cvar ROAD_MAINTENANCE_OR_CONSTRUCTION: Vehicle used for road
        maintenance or construction work purposes.
    :cvar ROAD_OPERATOR: Vehicle used by the road operator.
    :cvar TAXI: Vehicle used to provide an authorised taxi service.
    :cvar EXTENDED:
    """
    AGRICULTURAL = "agricultural"
    CAR_SHARING = "carSharing"
    CITY_LOGISTICS = "cityLogistics"
    COMMERCIAL = "commercial"
    EMERGENCY_SERVICES = "emergencyServices"
    MILITARY = "military"
    NON_COMMERCIAL = "nonCommercial"
    PATROL = "patrol"
    RECOVERY_SERVICES = "recoveryServices"
    ROAD_MAINTENANCE_OR_CONSTRUCTION = "roadMaintenanceOrConstruction"
    ROAD_OPERATOR = "roadOperator"
    TAXI = "taxi"
    EXTENDED = "_extended"


@dataclass
class VersionedReference:
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
        }
    )


class WeatherRelatedRoadConditionTypeEnum1(Enum):
    """
    Types of road surface conditions which are related to the weather.

    :cvar BLACK_ICE: Severe skid risk due to black ice (i.e. clear ice,
        which is impossible or very difficult to see).
    :cvar DEEP_SNOW: Deep snow on the roadway.
    :cvar DRY: There is no humidity over the sensor.
    :cvar FREEZING_OF_WET_ROADS: The wet road surface is subject to
        freezing.
    :cvar FREEZING_PAVEMENTS: The pavements for pedestrians are subject
        to freezing.
    :cvar FREEZING_RAIN: Severe skid risk due to rain falling on sub-
        zero temperature road surface and freezing.
    :cvar FRESH_SNOW: Fresh snow (with little or no traffic yet) on the
        roadway.
    :cvar GLAZE: Glaze of the road surface.
    :cvar ICE: Increased skid risk due to ice (of any kind).
    :cvar ICE_BUILD_UP: Ice is building up on the roadway causing a
        serious skid hazard.
    :cvar ICE_WITH_WHEEL_BAR_TRACKS: Ice on the road frozen in the form
        of wheel tracks.
    :cvar ICY_PATCHES: Severe skid risk due to icy patches (i.e.
        intermittent ice on roadway).
    :cvar LOOSE_SNOW: Powdery snow on the road which is subject to being
        blown by the wind.
    :cvar MOIST: From (0,01 mm) water film thickness over the sensor
    :cvar NORMAL_WINTER_CONDITIONS_FOR_PEDESTRIANS: Conditions for
        pedestrians are consistent with those normally expected in
        winter.
    :cvar NOT_DRY: The road surface is not dry.
    :cvar PACKED_SNOW: Packed snow (heavily trafficked) on the roadway.
    :cvar RIME: Fresh snow (with little or no traffic yet) on the
        roadway.
    :cvar ROAD_SURFACE_MELTING: The road surface is melting, or has
        melted due to abnormally high temperatures.
    :cvar SLIPPERY: Detection at least of the presence of partly or
        wholly solidified aqueous solution over the sensor.
    :cvar SLUSH_ON_ROAD: Increased skid risk due to melting snow (slush)
        on road.
    :cvar SLUSH_STRINGS: Melting snow (slush) on the roadway is formed
        into wheel tracks.
    :cvar SNOW: Fresh snow (with little or no traffic yet) on the
        roadway.
    :cvar SNOW_DRIFTS: Snow drifting is in progress or patches of deep
        snow are present due to earlier drifting.
    :cvar SNOW_ON_PAVEMENT: Snow is on the pedestrian pavement.
    :cvar WET_AND_ICY_ROAD: Increased skid risk due to partly thawed,
        wet road with packed snow and ice, or rain falling on packed
        snow and ice.
    :cvar SNOW_ON_THE_ROAD: Snow is lying on the road surface.
    :cvar WET_ICY_PAVEMENT: Partly thawed, wet pedestrian pavement with
        packed snow and ice, or rain falling on packed snow and ice.
    :cvar STREAMING_WATER: From (2 mm) water film thickness over the
        sensor.
    :cvar SURFACE_WATER: Water is resting on the roadway which provides
        an increased hazard to vehicles.
    :cvar WET: From (0,2 mm) water film thickness over the sensor
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    BLACK_ICE = "blackIce"
    DEEP_SNOW = "deepSnow"
    DRY = "dry"
    FREEZING_OF_WET_ROADS = "freezingOfWetRoads"
    FREEZING_PAVEMENTS = "freezingPavements"
    FREEZING_RAIN = "freezingRain"
    FRESH_SNOW = "freshSnow"
    GLAZE = "glaze"
    ICE = "ice"
    ICE_BUILD_UP = "iceBuildUp"
    ICE_WITH_WHEEL_BAR_TRACKS = "iceWithWheelBarTracks"
    ICY_PATCHES = "icyPatches"
    LOOSE_SNOW = "looseSnow"
    MOIST = "moist"
    NORMAL_WINTER_CONDITIONS_FOR_PEDESTRIANS = "normalWinterConditionsForPedestrians"
    NOT_DRY = "notDry"
    PACKED_SNOW = "packedSnow"
    RIME = "rime"
    ROAD_SURFACE_MELTING = "roadSurfaceMelting"
    SLIPPERY = "slippery"
    SLUSH_ON_ROAD = "slushOnRoad"
    SLUSH_STRINGS = "slushStrings"
    SNOW = "snow"
    SNOW_DRIFTS = "snowDrifts"
    SNOW_ON_PAVEMENT = "snowOnPavement"
    WET_AND_ICY_ROAD = "wetAndIcyRoad"
    SNOW_ON_THE_ROAD = "snowOnTheRoad"
    WET_ICY_PAVEMENT = "wetIcyPavement"
    STREAMING_WATER = "streamingWater"
    SURFACE_WATER = "surfaceWater"
    WET = "wet"
    OTHER = "other"
    EXTENDED = "_extended"


class WeightTypeEnum1(Enum):
    """Type of weight - describing the meaning of a vehicle weight value

    :cvar ACTUAL: The weight is the actual weight of a specific vehicle
    :cvar MAXIMUM_PERMITTED: The weight is the maximum permitted weight
        for a vehicle
    :cvar EXTENDED:
    """
    ACTUAL = "actual"
    MAXIMUM_PERMITTED = "maximumPermitted"
    EXTENDED = "_extended"


class WinterEquipmentManagementTypeEnum1(Enum):
    """
    Instructions relating to the use of winter equipment.

    :cvar DO_NOT_USE_STUD_TYRES: Do not use stud tyres.
    :cvar USE_SNOW_CHAINS: Use snow chains.
    :cvar USE_SNOW_CHAINS_OR_TYRES: Use snow chains or snow tyres.
    :cvar USE_SNOW_TYRES: Use snow tyres.
    :cvar WINTER_EQUIPMENT_ON_BOARD_REQUIRED: The carrying of winter
        equipment (snow chains and/or snow tyres) is required.
    :cvar OTHER: Other than as defined in this enumeration.
    :cvar EXTENDED:
    """
    DO_NOT_USE_STUD_TYRES = "doNotUseStudTyres"
    USE_SNOW_CHAINS = "useSnowChains"
    USE_SNOW_CHAINS_OR_TYRES = "useSnowChainsOrTyres"
    USE_SNOW_TYRES = "useSnowTyres"
    WINTER_EQUIPMENT_ON_BOARD_REQUIRED = "winterEquipmentOnBoardRequired"
    OTHER = "other"
    EXTENDED = "_extended"


@dataclass
class ExtensionType:
    class Meta:
        name = "_ExtensionType"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )


@dataclass
class AxleSpacing:
    """
    The spacing details between the axle sets of an individual vehicle numbered
    from the front to the back of the vehicle.

    :ivar axle_spacing: The spacing interval, indicated by the
        axleSpacingSequenceIdentifier, between the axles of an
        individual vehicle from front to back of the vehicle.
    :ivar axle_spacing_sequence_identifier: Indicates the sequence
        number of the interval between the axles of the individual
        vehicle from front to back (e.g. 1, 2, 3...). This cannot exceed
        (numberOfAxles -1) if the numberOfAxles is also given as part of
        the VehicleCharacteristics.
    :ivar axle_spacing_extension:
    """
    axle_spacing: Optional[float] = field(
        default=None,
        metadata={
            "name": "axleSpacing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    axle_spacing_sequence_identifier: Optional[int] = field(
        default=None,
        metadata={
            "name": "axleSpacingSequenceIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    axle_spacing_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_axleSpacingExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class AxleWeight:
    """
    The weight details of a specific axle on the vehicle.

    :ivar axle_position_identifier: Indicates the position of the axle
        on the vehicle numbered from front to back (i.e. 1, 2, 3...).
        This cannot exceed the numberOfAxles if provided as part of
        VehicleCharacteristics.
    :ivar axle_weight: The weight of the specific axle, indicated by the
        axleSequenceIdentifier, on the vehicle numbered from front to
        back of the vehicle.
    :ivar maximum_permitted_axle_weight: The maximum permitted weight of
        this specific axle on the vehicle.
    :ivar axle_weight_extension:
    """
    axle_position_identifier: Optional[int] = field(
        default=None,
        metadata={
            "name": "axlePositionIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "axleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    maximum_permitted_axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "maximumPermittedAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    axle_weight_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_axleWeightExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class InternationalIdentifier:
    """
    An identifier/name whose range is specific to the particular country.

    :ivar country: EN ISO 3166-1 two-character country code.
    :ivar national_identifier: Identifier or name unique within the
        specified country.
    :ivar international_identifier_extension:
    """
    country: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
            "max_length": 2,
        }
    )
    national_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "nationalIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
            "max_length": 1024,
        }
    )
    international_identifier_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_internationalIdentifierExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class MultilingualString:
    values: Optional["MultilingualString.Values"] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )

    @dataclass
    class Values:
        value: List[MultilingualStringValue] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "http://datex2.eu/schema/3/common",
                "min_occurs": 1,
            }
        )


@dataclass
class NamedArea:
    """
    An abstract hook class to hook in a model for a named area.
    """
    named_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_namedAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class TimePeriodOfDay:
    """
    Specification of a continuous period of time within a 24 hour period.

    :ivar start_time_of_period: Start of time period.
    :ivar end_time_of_period: End of time period.
    :ivar time_period_of_day_extension:
    """
    start_time_of_period: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "startTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    end_time_of_period: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "endTimeOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    time_period_of_day_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_timePeriodOfDayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class CalendarWeekWithinMonthEnum2:
    class Meta:
        name = "_CalendarWeekWithinMonthEnum"

    value: Optional[CalendarWeekWithinMonthEnum1] = field(
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
class ComparisonOperatorEnum2:
    class Meta:
        name = "_ComparisonOperatorEnum"

    value: Optional[ComparisonOperatorEnum1] = field(
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
class ComputationMethodEnum2:
    class Meta:
        name = "_ComputationMethodEnum"

    value: Optional[ComputationMethodEnum1] = field(
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
class ConfidentialityValueEnum2:
    class Meta:
        name = "_ConfidentialityValueEnum"

    value: Optional[ConfidentialityValueEnum1] = field(
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
class DangerousGoodsRegulationsEnum2:
    class Meta:
        name = "_DangerousGoodsRegulationsEnum"

    value: Optional[DangerousGoodsRegulationsEnum1] = field(
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
class DayEnum2:
    class Meta:
        name = "_DayEnum"

    value: Optional[DayEnum1] = field(
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
class DirectionCompassEnum2:
    class Meta:
        name = "_DirectionCompassEnum"

    value: Optional[DirectionCompassEnum1] = field(
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
class EmissionClassificationEuroEnum2:
    class Meta:
        name = "_EmissionClassificationEuroEnum"

    value: Optional[EmissionClassificationEuroEnum1] = field(
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
class FaultSeverityEnum2:
    class Meta:
        name = "_FaultSeverityEnum"

    value: Optional[FaultSeverityEnum1] = field(
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
class FaultUrgencyEnum2:
    class Meta:
        name = "_FaultUrgencyEnum"

    value: Optional[FaultUrgencyEnum1] = field(
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
class FuelTypeEnum2:
    class Meta:
        name = "_FuelTypeEnum"

    value: Optional[FuelTypeEnum1] = field(
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
class InformationDeliveryServicesEnum2:
    class Meta:
        name = "_InformationDeliveryServicesEnum"

    value: Optional[InformationDeliveryServicesEnum1] = field(
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
class InformationStatusEnum2:
    class Meta:
        name = "_InformationStatusEnum"

    value: Optional[InformationStatusEnum1] = field(
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
class InstanceOfDayEnum2:
    class Meta:
        name = "_InstanceOfDayEnum"

    value: Optional[InstanceOfDayEnum1] = field(
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
class LoadTypeEnum2:
    class Meta:
        name = "_LoadTypeEnum"

    value: Optional[LoadTypeEnum1] = field(
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
class LowEmissionLevelEnum2:
    class Meta:
        name = "_LowEmissionLevelEnum"

    value: Optional[LowEmissionLevelEnum1] = field(
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
class MonthOfYearEnum2:
    class Meta:
        name = "_MonthOfYearEnum"

    value: Optional[MonthOfYearEnum1] = field(
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
class PollutantTypeEnum2:
    class Meta:
        name = "_PollutantTypeEnum"

    value: Optional[PollutantTypeEnum1] = field(
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
class PrecipitationIntensityEnum2:
    class Meta:
        name = "_PrecipitationIntensityEnum"

    value: Optional[PrecipitationIntensityEnum1] = field(
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
class PrecipitationTypeEnum2:
    class Meta:
        name = "_PrecipitationTypeEnum"

    value: Optional[PrecipitationTypeEnum1] = field(
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
class PublicEventTypeEnum2:
    class Meta:
        name = "_PublicEventTypeEnum"

    value: Optional[PublicEventTypeEnum1] = field(
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
class SourceTypeEnum2:
    class Meta:
        name = "_SourceTypeEnum"

    value: Optional[SourceTypeEnum1] = field(
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
class SpecialDayTypeEnum2:
    class Meta:
        name = "_SpecialDayTypeEnum"

    value: Optional[SpecialDayTypeEnum1] = field(
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
class TimePrecisionEnum2:
    class Meta:
        name = "_TimePrecisionEnum"

    value: Optional[TimePrecisionEnum1] = field(
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
class TrafficTrendTypeEnum2:
    class Meta:
        name = "_TrafficTrendTypeEnum"

    value: Optional[TrafficTrendTypeEnum1] = field(
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
class UrlLinkTypeEnum2:
    class Meta:
        name = "_UrlLinkTypeEnum"

    value: Optional[UrlLinkTypeEnum1] = field(
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
class ValidityStatusEnum2:
    class Meta:
        name = "_ValidityStatusEnum"

    value: Optional[ValidityStatusEnum1] = field(
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
class VehicleEquipmentEnum2:
    class Meta:
        name = "_VehicleEquipmentEnum"

    value: Optional[VehicleEquipmentEnum1] = field(
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
class VehicleStatusEnum2:
    class Meta:
        name = "_VehicleStatusEnum"

    value: Optional[VehicleStatusEnum1] = field(
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
class VehicleTypeEnum2:
    class Meta:
        name = "_VehicleTypeEnum"

    value: Optional[VehicleTypeEnum1] = field(
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
class VehicleUsageEnum2:
    class Meta:
        name = "_VehicleUsageEnum"

    value: Optional[VehicleUsageEnum1] = field(
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
class WeatherRelatedRoadConditionTypeEnum2:
    class Meta:
        name = "_WeatherRelatedRoadConditionTypeEnum"

    value: Optional[WeatherRelatedRoadConditionTypeEnum1] = field(
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
class WeightTypeEnum2:
    class Meta:
        name = "_WeightTypeEnum"

    value: Optional[WeightTypeEnum1] = field(
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
class WinterEquipmentManagementTypeEnum2:
    class Meta:
        name = "_WinterEquipmentManagementTypeEnum"

    value: Optional[WinterEquipmentManagementTypeEnum1] = field(
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
class DataValue:
    """A data value of something that can be measured or calculated.

    Any provided meta-data values specified in the attributes override
    any specified generic characteristics such as defined for a specific
    measurement in the MeasurementSiteTable.

    :ivar data_error: Indication of whether the value is deemed to be
        erroneous by the supplier (true = erroneous). If not present,
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
        in the sampling or measurement period to determine the data
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
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    reason_for_data_error: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "reasonForDataError",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    data_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_dataValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    accuracy: Optional[float] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    computational_method: Optional[ComputationMethodEnum1] = field(
        default=None,
        metadata={
            "name": "computationalMethod",
            "type": "Attribute",
        }
    )
    number_of_incomplete_inputs: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfIncompleteInputs",
            "type": "Attribute",
        }
    )
    number_of_input_values_used: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfInputValuesUsed",
            "type": "Attribute",
        }
    )
    smoothing_factor: Optional[float] = field(
        default=None,
        metadata={
            "name": "smoothingFactor",
            "type": "Attribute",
        }
    )
    standard_deviation: Optional[float] = field(
        default=None,
        metadata={
            "name": "standardDeviation",
            "type": "Attribute",
        }
    )
    supplier_calculated_data_quality: Optional[float] = field(
        default=None,
        metadata={
            "name": "supplierCalculatedDataQuality",
            "type": "Attribute",
        }
    )


@dataclass
class DayWeekMonth:
    """
    Specification of periods defined by the intersection of days or instances
    of them, calendar weeks and months.

    :ivar applicable_day: Applicable day of the week. "All days of the
        week" is expressed by non-inclusion of this attribute.
    :ivar applicable_month: Applicable month of the year.  "All months
        of the year" is expressed by non-inclusion of this attribute.
    :ivar day_week_month_extension:
    """
    applicable_day: List[DayEnum2] = field(
        default_factory=list,
        metadata={
            "name": "applicableDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_occurs": 7,
        }
    )
    applicable_month: List[MonthOfYearEnum2] = field(
        default_factory=list,
        metadata={
            "name": "applicableMonth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_occurs": 12,
        }
    )
    day_week_month_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_dayWeekMonthExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class Emissions:
    """
    Emission characteristics of vehicles.

    :ivar emission_classification_euro: The minimum Euro emission
        classification the vehicle(s) have to comply with according to
        the 1970 Directive 70/220/EEC and its several amendments. Note
        that vehicleType and fuelType need to be provided in order to
        make this classification explicit.
    :ivar emission_classification_other: Some other (probably locally
        defined) value(s) for emission classification.
    :ivar emission_level: The low emission level of a vehicle.
    :ivar emissions_extension:
    """
    emission_classification_euro: Optional[EmissionClassificationEuroEnum2] = field(
        default=None,
        metadata={
            "name": "emissionClassificationEuro",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    emission_classification_other: List[str] = field(
        default_factory=list,
        metadata={
            "name": "emissionClassificationOther",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    emission_level: Optional[LowEmissionLevelEnum2] = field(
        default=None,
        metadata={
            "name": "emissionLevel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    emissions_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_emissionsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class Fault:
    """
    Information about a fault relating to a specific piece of equipment or
    process.

    :ivar fault_identifier: Unique identifier of the fault.
    :ivar fault_description: Textual description of the fault.
    :ivar fault_creation_time: The date and time at which the fault was
        originally recorded/reported.
    :ivar fault_last_update_time: The date and time at which the fault
        information as specified in this instance was last updated.
    :ivar fault_impact_severity: The severity of the fault in terms of
        how it affects the usability of the equipment or the reliability
        of the data generated by the equipment.
    :ivar fault_urgency_to_rectify: The urgency to rectify the fault.
    :ivar manufacturer_fault_code: A manufacturer specific code for the
        fault.
    :ivar fault_extension:
    """
    fault_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "faultIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    fault_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "faultDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    fault_creation_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "faultCreationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    fault_last_update_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "faultLastUpdateTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    fault_impact_severity: Optional[FaultSeverityEnum2] = field(
        default=None,
        metadata={
            "name": "faultImpactSeverity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    fault_urgency_to_rectify: Optional[FaultUrgencyEnum2] = field(
        default=None,
        metadata={
            "name": "faultUrgencyToRectify",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    manufacturer_fault_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "manufacturerFaultCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    fault_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_faultExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class GlobalReference:
    """
    A versioned reference to an object that may be in another publication from
    another publisher.

    :ivar external_publication_identifier: Identifier for an external
        DATEX II publication
    :ivar external_publisher: Identifier for an external DATEX II
        publisher
    :ivar global_reference_extension:
    """
    external_publication_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "externalPublicationIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    external_publisher: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "externalPublisher",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    global_reference_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_globalReferenceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class GrossWeightCharacteristic:
    """
    Gross weight characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar gross_vehicle_weight: The gross weight of the vehicle and its
        load, including any trailers.
    :ivar type_of_weight: The meaning of the weight value
    :ivar gross_weight_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum2] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    gross_vehicle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "grossVehicleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    type_of_weight: Optional[WeightTypeEnum2] = field(
        default=None,
        metadata={
            "name": "typeOfWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    gross_weight_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_grossWeightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class HazardousMaterials:
    """
    Details of hazardous materials.

    :ivar chemical_name: The chemical name of the hazardous substance
        carried by the vehicle.
    :ivar dangerous_goods_flash_point: The temperature at which the
        vapour from a hazardous substance will ignite in air.
    :ivar dangerous_goods_regulations: The code defining the
        regulations, international or national, applicable for a means
        of transport.
    :ivar hazard_code_identification: The dangerous goods description
        code.
    :ivar hazard_code_version_number: The version/revision number of
        date of issuance of the hazardous material code used.
    :ivar hazard_substance_item_page_number: A number giving additional
        hazard code classification of a goods item within the applicable
        dangerous goods regulation.
    :ivar trem_card_number: The identification of a transport emergency
        card giving advice for emergency actions.
    :ivar undg_number: A unique serial number assigned within the United
        Nations to substances and articles contained in a list of the
        dangerous goods most commonly carried.
    :ivar volume_of_dangerous_goods: The volume of dangerous goods on
        the vehicle(s) reported in a traffic/travel situation.
    :ivar weight_of_dangerous_goods: The weight of dangerous goods on
        the vehicle(s) reported in a traffic/travel situation.
    :ivar hazardous_materials_extension:
    """
    chemical_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "chemicalName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    dangerous_goods_flash_point: Optional[float] = field(
        default=None,
        metadata={
            "name": "dangerousGoodsFlashPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    dangerous_goods_regulations: Optional[DangerousGoodsRegulationsEnum2] = field(
        default=None,
        metadata={
            "name": "dangerousGoodsRegulations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    hazard_code_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "hazardCodeIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    hazard_code_version_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "hazardCodeVersionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    hazard_substance_item_page_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "hazardSubstanceItemPageNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    trem_card_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "tremCardNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    undg_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "undgNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    volume_of_dangerous_goods: Optional[float] = field(
        default=None,
        metadata={
            "name": "volumeOfDangerousGoods",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    weight_of_dangerous_goods: Optional[float] = field(
        default=None,
        metadata={
            "name": "weightOfDangerousGoods",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    hazardous_materials_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_hazardousMaterialsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class HeaderInformation:
    """
    Management information relating to the data contained within a publication.

    :ivar confidentiality: The extent to which the related information
        may be circulated, according to the recipient type.
    :ivar allowed_delivery_channel: The allowed delivery channel.
    :ivar information_status: The status of the related information
        (real, test, exercise ....).
    :ivar header_information_extension:
    """
    confidentiality: Optional[ConfidentialityValueEnum2] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    allowed_delivery_channel: List[InformationDeliveryServicesEnum2] = field(
        default_factory=list,
        metadata={
            "name": "allowedDeliveryChannel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    information_status: Optional[InformationStatusEnum2] = field(
        default=None,
        metadata={
            "name": "informationStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    header_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_headerInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class HeaviestAxleWeightCharacteristic:
    """
    Weight characteristic of the heaviest axle on the vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar heaviest_axle_weight: The weight of the heaviest axle on the
        vehicle.
    :ivar heaviest_axle_weight_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum2] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    heaviest_axle_weight: Optional[float] = field(
        default=None,
        metadata={
            "name": "heaviestAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    heaviest_axle_weight_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_heaviestAxleWeightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class HeightCharacteristic:
    """
    Height characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar vehicle_height: The height of the highest part, excluding
        antennae, of an individual vehicle above the road surface, in
        metres.
    :ivar height_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum2] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    vehicle_height: Optional[float] = field(
        default=None,
        metadata={
            "name": "vehicleHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    height_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_heightCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class LengthCharacteristic:
    """
    Length characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar vehicle_length: The overall distance between the front and
        back of an individual vehicle, including the length of any
        trailers, couplings, embedded features etc.
    :ivar length_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum2] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    vehicle_length: Optional[float] = field(
        default=None,
        metadata={
            "name": "vehicleLength",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    length_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_lengthCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class NumberOfAxlesCharacteristic:
    """
    Number of axles characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar number_of_axles: The total number of axles of an individual
        vehicle.
    :ivar number_of_axles_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum2] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    number_of_axles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfAxles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    number_of_axles_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_numberOfAxlesCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class PayloadPublication:
    """
    A payload publication of traffic related information or associated
    management information created at a specific point in time that can be
    exchanged via a DATEX II interface.

    :ivar feed_description: A description of the information which is to
        be found in the publications originating from the particular
        feed (URL).
    :ivar feed_type: A classification of the information which is to be
        found in the publications originating from the particular feed.
    :ivar publication_time: Date/time at which the payload publication
        was created.
    :ivar publication_creator:
    :ivar payload_publication_extension:
    :ivar lang: The default language used throughout the payload
        publication.
    :ivar model_base_version:
    :ivar extension_name:
    :ivar extension_version:
    :ivar profile_name:
    :ivar profile_version:
    """
    feed_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "feedDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    feed_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "feedType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    publication_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "publicationTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    publication_creator: Optional[InternationalIdentifier] = field(
        default=None,
        metadata={
            "name": "publicationCreator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    payload_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_payloadPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    lang: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    model_base_version: str = field(
        init=False,
        default="3",
        metadata={
            "name": "modelBaseVersion",
            "type": "Attribute",
            "required": True,
        }
    )
    extension_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "extensionName",
            "type": "Attribute",
        }
    )
    extension_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "extensionVersion",
            "type": "Attribute",
        }
    )
    profile_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "profileName",
            "type": "Attribute",
        }
    )
    profile_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "profileVersion",
            "type": "Attribute",
        }
    )


@dataclass
class Source:
    """
    Details of the source from which the information was obtained.

    :ivar source_country: EN ISO 3166-1 two-character country code of
        the source of the information.
    :ivar source_identification: Language independent textual code or
        identifier for the organisation or the equipment that has
        produced the information.
    :ivar source_name: The name of the organisation which has produced
        the information relating to this version of the information.
    :ivar source_type: Information about the technology used for
        measuring the data or the method used for obtaining qualitative
        descriptions relating to this version of the information.
    :ivar reliable: An indication as to whether the source deems the
        associated information to be reliable/correct. "True" indicates
        it is deemed reliable.
    :ivar source_extension:
    """
    source_country: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceCountry",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 2,
        }
    )
    source_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "sourceIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    source_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    source_type: Optional[SourceTypeEnum2] = field(
        default=None,
        metadata={
            "name": "sourceType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    reliable: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    source_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_sourceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class SpecialDay:
    """Specification of a special type of day, possibly also a public holiday.

    Can be country or region specific.

    :ivar intersect_with_applicable_days: When true, the period is the
        intersection of applicable days and this special day. When
        false, the period is the union of applicable days and this
        special day.
    :ivar special_day_type: Specification of a special day, for example
        schoolDay, publicHoliday, ...
    :ivar public_event: Type of public event on this special day.
    :ivar named_area:
    :ivar special_day_extension:
    """
    intersect_with_applicable_days: Optional[bool] = field(
        default=None,
        metadata={
            "name": "intersectWithApplicableDays",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    special_day_type: Optional[SpecialDayTypeEnum2] = field(
        default=None,
        metadata={
            "name": "specialDayType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    public_event: Optional[PublicEventTypeEnum2] = field(
        default=None,
        metadata={
            "name": "publicEvent",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    named_area: List[NamedArea] = field(
        default_factory=list,
        metadata={
            "name": "namedArea",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    special_day_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_specialDayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class UrlLink:
    """
    Details of a Uniform Resource Locator (URL) address pointing to a resource
    available on the Internet from where further relevant information may be
    obtained.

    :ivar url_link_address: A Uniform Resource Locator (URL) address
        pointing to a resource available on the Internet from where
        further relevant information may be obtained.
    :ivar url_link_description: Description of the relevant information
        available on the Internet from the URL link.
    :ivar url_link_type: Details of the type of relevant information
        available on the Internet from the URL link.
    :ivar url_link_extension:
    """
    url_link_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "urlLinkAddress",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    url_link_description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "urlLinkDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    url_link_type: Optional[UrlLinkTypeEnum2] = field(
        default=None,
        metadata={
            "name": "urlLinkType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    url_link_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_urlLinkExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class WidthCharacteristic:
    """
    Width characteristic of a vehicle.

    :ivar comparison_operator: The operator to be used in the vehicle
        characteristic comparison operation.
    :ivar vehicle_width: The maximum width of an individual vehicle,
        including any features embedded or fixed on it, in metres.
    :ivar width_characteristic_extension:
    """
    comparison_operator: Optional[ComparisonOperatorEnum2] = field(
        default=None,
        metadata={
            "name": "comparisonOperator",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    vehicle_width: Optional[float] = field(
        default=None,
        metadata={
            "name": "vehicleWidth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    width_characteristic_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_widthCharacteristicExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class ApplicationRateValue(DataValue):
    """
    A measured or calculated value of the application rate of a substance.

    :ivar application_rate: A value of the rate of application of a
        substance expressed in kilogrammes per square metre.
    :ivar application_rate_value_extension:
    """
    application_rate: Optional[float] = field(
        default=None,
        metadata={
            "name": "applicationRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    application_rate_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_applicationRateValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class CalendarWeekWithinMonth(DayWeekMonth):
    """Specification of periods defined by relevant calendar weeks in a month,
    see ISO8601.

    Note: Calendar weeks start with Monday. First week is the week containing the first of the month.

    :ivar applicable_calender_week_within_month: Calender week in month.
        See ISO8601.  "All weeks of the month" is expressed by not using
        the CalendarWeekOfMonth class. Note: Calendar weeks start with
        Monday. First week is the week containing the first of the
        month.
    :ivar calendar_week_within_month_extension:
    """
    applicable_calender_week_within_month: List[CalendarWeekWithinMonthEnum2] = field(
        default_factory=list,
        metadata={
            "name": "applicableCalenderWeekWithinMonth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "min_occurs": 1,
            "max_occurs": 6,
        }
    )
    calendar_week_within_month_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_calendarWeekWithinMonthExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class DirectionBearingValue(DataValue):
    """
    A measured or calculated value of direction as a bearing.

    :ivar direction_bearing: A value of direction expressed in terms of
        a bearing measured in whole degrees. Unless otherwise specified
        the reference direction corresponding to 0 degrees is North.
    :ivar direction_bearing_value_extension:
    """
    direction_bearing: Optional[int] = field(
        default=None,
        metadata={
            "name": "directionBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 359,
        }
    )
    direction_bearing_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_directionBearingValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class DirectionCompassValue(DataValue):
    """
    A measured or calculated value of direction as a point of the compass.

    :ivar direction_compass: A value of direction expressed in terms of
        points of the compass.
    :ivar direction_compass_value_extension:
    """
    direction_compass: Optional[DirectionCompassEnum2] = field(
        default=None,
        metadata={
            "name": "directionCompass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    direction_compass_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_directionCompassValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class FloatingPointMetreDistanceValue(DataValue):
    """
    A measured or calculated value of distance in metres in a floating point
    format.

    :ivar distance: A value of distance expressed in metres in a
        floating point format.
    :ivar floating_point_metre_distance_value_extension:
    """
    distance: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    floating_point_metre_distance_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_floatingPointMetreDistanceValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class FrictionValue(DataValue):
    """
    A measured or calculated value of road surface friction.

    :ivar friction: Friction, usually a value between 0 and 1.
    :ivar friction_value_extension:
    """
    friction: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    friction_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_frictionValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class GenericPublication(PayloadPublication):
    """
    A publication used to make level B extensions at the publication level.

    :ivar generic_publication_name: The name of the generic publication.
    :ivar generic_publication_extension:
    """
    generic_publication_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "genericPublicationName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
            "max_length": 1024,
        }
    )
    generic_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_genericPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class InstanceOfDayWithinMonth(DayWeekMonth):
    """
    Specification of periods defined by the instance of a specific weekday
    within a month (e.g. 3rd Tuesday in May)

    :ivar applicable_instance_of_day_within_month: The specified integer
        instance of the specified applicable day within a month.
    :ivar instance_of_day_within_month_extension:
    """
    applicable_instance_of_day_within_month: List[InstanceOfDayEnum2] = field(
        default_factory=list,
        metadata={
            "name": "applicableInstanceOfDayWithinMonth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "min_occurs": 1,
            "max_occurs": 5,
        }
    )
    instance_of_day_within_month_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_instanceOfDayWithinMonthExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class IntegerMetreDistanceValue(DataValue):
    """
    A measured or calculated value of distance in whole metres.

    :ivar integer_metre_distance: A value of distance expressed in
        metres in a non-negative integer format.
    :ivar integer_metre_distance_value_extension:
    """
    integer_metre_distance: Optional[int] = field(
        default=None,
        metadata={
            "name": "integerMetreDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    integer_metre_distance_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_integerMetreDistanceValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class KilogramsConcentrationValue(DataValue):
    """
    A measured or calculated value of concentration of a substance in kilograms
    per unit volume.

    :ivar kilograms_concentration: A value defining the amount of a
        substance in a given volume (concentration) expressed in
        kilograms per cubic metre.
    :ivar kilograms_concentration_value_extension:
    """
    kilograms_concentration: Optional[float] = field(
        default=None,
        metadata={
            "name": "kilogramsConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    kilograms_concentration_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_kilogramsConcentrationValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class MicrogramsConcentrationValue(DataValue):
    """
    A measured or calculated value of concentration of a substance in
    micrograms per unit volume.

    :ivar micrograms_concentration: A value of the amount of a substance
        in a given volume (concentration) expressed in µg/m3
        (micrograms/cubic metre).
    :ivar micrograms_concentration_value_extension:
    """
    micrograms_concentration: Optional[float] = field(
        default=None,
        metadata={
            "name": "microgramsConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    micrograms_concentration_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_microgramsConcentrationValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class PercentageValue(DataValue):
    """
    A measured or calculated value expressed as a percentage.

    :ivar percentage: A value expressed as a percentage.
    :ivar percentage_value_extension:
    """
    percentage: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    percentage_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_percentageValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class Period:
    """
    A continuous time period or a set of discontinuous time periods defined by
    the intersection of a set of criteria all within an overall delimiting
    interval.

    :ivar start_of_period: Start of period.
    :ivar end_of_period: End of a period.
    :ivar period_name: The name of the period.
    :ivar recurring_time_period_of_day: A recurring period of a day.
    :ivar recurring_day_week_month_period: A recurring period defined in
        terms of days of the week, weeks of the month and months of the
        year.
    :ivar recurring_special_day: A recurring period in terms of special
        days.
    :ivar period_extension:
    """
    start_of_period: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "startOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    end_of_period: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "endOfPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    period_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "periodName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    recurring_time_period_of_day: List[TimePeriodOfDay] = field(
        default_factory=list,
        metadata={
            "name": "recurringTimePeriodOfDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    recurring_day_week_month_period: List[DayWeekMonth] = field(
        default_factory=list,
        metadata={
            "name": "recurringDayWeekMonthPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    recurring_special_day: List[SpecialDay] = field(
        default_factory=list,
        metadata={
            "name": "recurringSpecialDay",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    period_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_periodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class PrecipitationIntensityValue(DataValue):
    """
    A measured or calculated value of the accumulation rate of precipitation.

    :ivar millimetres_per_hour_intensity: A value of precipitation
        intensity expressed in units of millimetres per hour.
    :ivar precipitation_intensity_value_extension:
    """
    millimetres_per_hour_intensity: Optional[float] = field(
        default=None,
        metadata={
            "name": "millimetresPerHourIntensity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    precipitation_intensity_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_precipitationIntensityValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class PressureValue(DataValue):
    """
    A measured or calculated value of atmospheric pressure.

    :ivar pressure: Atmospheric pressure.
    :ivar pressure_value_extension:
    """
    pressure: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    pressure_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pressureValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class PublicHoliday(SpecialDay):
    """
    Specification of a specific public holiday in case specialDayType is set to
    'publicHoliday'.

    :ivar public_holiday_name: Specification of a specific public
        holiday by its name.
    :ivar public_holiday_extension:
    """
    public_holiday_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "publicHolidayName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    public_holiday_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_publicHolidayExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class SpeedValue(DataValue):
    """
    A measured or calculated value of speed.

    :ivar speed: A value of speed expressed in kilometres per hour.
    :ivar speed_value_extension:
    """
    speed: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    speed_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_speedValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class TemperatureValue(DataValue):
    """
    A measured or calculated value of temperature.

    :ivar temperature: A value of temperature expressed in degrees
        Celsius.
    :ivar temperature_value_extension:
    """
    temperature: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    temperature_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_temperatureValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class VehicleCharacteristics:
    """
    The characteristics of a vehicle, e.g. lorry of gross weight greater than
    30 tonnes.

    :ivar fuel_type: The type of fuel used by the vehicle.
    :ivar load_type: The type of load carried by the vehicle, especially
        in respect of hazardous loads.
    :ivar vehicle_equipment: The type of equipment in use or on board
        the vehicle.
    :ivar vehicle_type: Vehicle type.
    :ivar vehicle_usage: The type of usage of the vehicle (i.e. for what
        purpose is the vehicle being used).
    :ivar year_of_first_registration: Year of first registration of the
        vehicle
    :ivar gross_weight_characteristic:
    :ivar height_characteristic:
    :ivar length_characteristic:
    :ivar width_characteristic:
    :ivar heaviest_axle_weight_characteristic:
    :ivar number_of_axles_characteristic:
    :ivar emissions:
    :ivar vehicle_characteristics_extension:
    """
    fuel_type: List[FuelTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "fuelType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    load_type: Optional[LoadTypeEnum2] = field(
        default=None,
        metadata={
            "name": "loadType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    vehicle_equipment: Optional[VehicleEquipmentEnum2] = field(
        default=None,
        metadata={
            "name": "vehicleEquipment",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    vehicle_type: List[VehicleTypeEnum2] = field(
        default_factory=list,
        metadata={
            "name": "vehicleType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    vehicle_usage: Optional[VehicleUsageEnum2] = field(
        default=None,
        metadata={
            "name": "vehicleUsage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    year_of_first_registration: Optional[int] = field(
        default=None,
        metadata={
            "name": "yearOfFirstRegistration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    gross_weight_characteristic: List[GrossWeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "grossWeightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_occurs": 2,
        }
    )
    height_characteristic: List[HeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "heightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_occurs": 2,
        }
    )
    length_characteristic: List[LengthCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "lengthCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_occurs": 2,
        }
    )
    width_characteristic: List[WidthCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "widthCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_occurs": 2,
        }
    )
    heaviest_axle_weight_characteristic: List[HeaviestAxleWeightCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "heaviestAxleWeightCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_occurs": 2,
        }
    )
    number_of_axles_characteristic: List[NumberOfAxlesCharacteristic] = field(
        default_factory=list,
        metadata={
            "name": "numberOfAxlesCharacteristic",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_occurs": 2,
        }
    )
    emissions: Optional[Emissions] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    vehicle_characteristics_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vehicleCharacteristicsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class VehicleFlowValue(DataValue):
    """
    A measured or calculated value of the flow rate of vehicles.

    :ivar vehicle_flow_rate: A value of vehicle flow rate expressed in
        vehicles per hour.
    :ivar vehicle_flow_value_extension:
    """
    vehicle_flow_rate: Optional[int] = field(
        default=None,
        metadata={
            "name": "vehicleFlowRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    vehicle_flow_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vehicleFlowValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class WindSpeedValue(DataValue):
    """
    A measured or calculated value of wind speed.

    :ivar wind_speed: A value of wind speed expressed in metres per
        second.
    :ivar wind_speed_value_extension:
    """
    wind_speed: Optional[float] = field(
        default=None,
        metadata={
            "name": "windSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    wind_speed_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_windSpeedValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class GroupOfVehiclesInvolved:
    """
    Group of the vehicles involved having common characteristics and/or status.

    :ivar number_of_vehicles: The number of vehicles of this group that
        are involved.
    :ivar vehicle_status: Vehicle status.
    :ivar vehicle_characteristics:
    :ivar group_of_vehicles_involved_extension:
    """
    number_of_vehicles: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfVehicles",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    vehicle_status: Optional[VehicleStatusEnum2] = field(
        default=None,
        metadata={
            "name": "vehicleStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    group_of_vehicles_involved_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_groupOfVehiclesInvolvedExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class Humidity:
    """
    Details of atmospheric humidity.

    :ivar relative_humidity: The amount of water vapour in the air, as a
        percentage of the amount of water vapour in saturated air at the
        same temperature and at atmospheric pressure. The measurement is
        taken between 1.5 and 2 m above the ground and behind a
        meteorological screen.
    :ivar humidity_extension:
    """
    relative_humidity: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "name": "relativeHumidity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    humidity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_humidityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class OverallPeriod:
    """
    A continuous or discontinuous period of validity defined by overall
    bounding start and end times and the possible intersection of valid periods
    (potentially recurring) with the complement of exception periods (also
    potentially recurring).

    :ivar overall_start_time: Start of bounding period of validity
        defined by date and time.
    :ivar overall_end_time: End of bounding period of validity defined
        by date and time.
    :ivar valid_period: A single time period, a recurring time period or
        a set of different recurring time periods during which validity
        is true.
    :ivar exception_period: A single time period, a recurring time
        period or a set of different recurring time periods during which
        validity is false.
    :ivar overall_period_extension:
    """
    overall_start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "overallStartTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    overall_end_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "overallEndTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    valid_period: List[Period] = field(
        default_factory=list,
        metadata={
            "name": "validPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    exception_period: List[Period] = field(
        default_factory=list,
        metadata={
            "name": "exceptionPeriod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    overall_period_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_overallPeriodExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class Pollution:
    """
    Details of atmospheric pollution.

    :ivar pollutant_type: The type of pollutant in the air.
    :ivar pollutant_concentration: The average concentration of the
        pollutant in the air.
    :ivar pollution_extension:
    """
    pollutant_type: Optional[PollutantTypeEnum2] = field(
        default=None,
        metadata={
            "name": "pollutantType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    pollutant_concentration: Optional[MicrogramsConcentrationValue] = field(
        default=None,
        metadata={
            "name": "pollutantConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    pollution_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pollutionExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class PrecipitationDetail:
    """
    Details of precipitation (rain, snow etc.).

    :ivar precipitation_type: The type of precipitation which is
        affecting the driving conditions.
    :ivar precipitation_intensity_grade: The intensity of precipitation
        expressed by enumerated value,
    :ivar precipitation_intensity: The height of the precipitation
        received per unit time.
    :ivar deposition_depth: The equivalent depth of the water layer
        resulting from precipitation or deposition on a non-porous
        horizontal surface. Non liquid precipitation is considered as
        melted in water form.
    :ivar precipitation_detail_extension:
    """
    precipitation_type: Optional[PrecipitationTypeEnum2] = field(
        default=None,
        metadata={
            "name": "precipitationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    precipitation_intensity_grade: Optional[PrecipitationIntensityEnum2] = field(
        default=None,
        metadata={
            "name": "precipitationIntensityGrade",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    precipitation_intensity: Optional[PrecipitationIntensityValue] = field(
        default=None,
        metadata={
            "name": "precipitationIntensity",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    deposition_depth: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "depositionDepth",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    precipitation_detail_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_precipitationDetailExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class Pressure:
    """
    Details of atmospheric pressure.
    """
    pressure_value: Optional[PressureValue] = field(
        default=None,
        metadata={
            "name": "pressureValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    pressure_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_pressureExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class Temperature:
    """
    Details of atmospheric temperature.

    :ivar air_temperature: The air temperature measured in the shade
        between 1.5 and 2 metres above ground level.
    :ivar dew_point_temperature: The temperature to which the air would
        have to cool (at constant pressure and water vapour content) in
        order to reach saturation.
    :ivar maximum_temperature: The maximum temperature during the
        forecast or measurement period.
    :ivar minimum_temperature: The minimum temperature during the
        forecast or measurement period.
    :ivar temperature_extension:
    """
    air_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "airTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    dew_point_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "dewPointTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    maximum_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "maximumTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    minimum_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "minimumTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    temperature_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_temperatureExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class TemperatureBelowOrAboveRoadSurface:
    """
    Mesurement of temperature below or above the road surface.

    :ivar height_below_or_above_road_surface: The height of the
        measurement either below (negative value) or above (positive
        value) the road surface.
    :ivar temperature_below_or_above_road_surface: The temperature
        measured at the specified height below or above the road
        surface.
    :ivar temperature_below_or_above_road_surface_extension:
    """
    height_below_or_above_road_surface: Optional[float] = field(
        default=None,
        metadata={
            "name": "heightBelowOrAboveRoadSurface",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    temperature_below_or_above_road_surface: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "temperatureBelowOrAboveRoadSurface",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    temperature_below_or_above_road_surface_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_temperatureBelowOrAboveRoadSurfaceExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class Vehicle:
    """
    Details of an individual vehicle.

    :ivar anonymized_vehicle_reference: A reference for a vehicle
        derived from vehicle properties such as registration number but
        encoded so that it does not allow a human to identify the
        vehicle directly from the encoded value
    :ivar vehicle_colour: The colour of the vehicle.
    :ivar vehicle_country_of_origin: Specification of the country in
        which the vehicle is registered. The code is the 2-alpha code as
        given in EN ISO 3166-1 which is updated by the ISO 3166
        Maintenance Agency.
    :ivar vehicle_identifier: A vehicle identification number (VIN)
        comprising 17 characters that is based on either ISO 3779 or ISO
        3780 and uniquely identifies the individual vehicle. This is
        normally securely attached to the vehicle chassis.
    :ivar vehicle_manufacturer: Indicates the stated manufacturer of the
        vehicle, e.g. Ford.
    :ivar vehicle_model: Indicates the model (or range name) of the
        vehicle, e.g. Mondeo.
    :ivar vehicle_registration_plate_identifier: An identifier or code
        displayed on a vehicle registration plate attached to the
        vehicle used for official identification purposes. The
        registration identifier is numeric or alphanumeric and is unique
        within the issuing authority's region.
    :ivar vehicle_status: Vehicle status.
    :ivar vehicle_characteristics:
    :ivar axle_spacing_on_vehicle: The spacing between axles on the
        vehicles.
    :ivar specific_axle_weight: The weight details relating to a
        specific axle on the vehicle.
    :ivar hazardous_goods_associated_with_vehicle: Details of hazardous
        goods carried by the vehicle.
    :ivar vehicle_extension:
    """
    anonymized_vehicle_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "anonymizedVehicleReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    vehicle_colour: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "vehicleColour",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    vehicle_country_of_origin: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleCountryOfOrigin",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 2,
        }
    )
    vehicle_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    vehicle_manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleManufacturer",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    vehicle_model: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleModel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    vehicle_registration_plate_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "vehicleRegistrationPlateIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "max_length": 1024,
        }
    )
    vehicle_status: Optional[VehicleStatusEnum2] = field(
        default=None,
        metadata={
            "name": "vehicleStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    vehicle_characteristics: Optional[VehicleCharacteristics] = field(
        default=None,
        metadata={
            "name": "vehicleCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    axle_spacing_on_vehicle: List[AxleSpacing] = field(
        default_factory=list,
        metadata={
            "name": "axleSpacingOnVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    specific_axle_weight: List[AxleWeight] = field(
        default_factory=list,
        metadata={
            "name": "specificAxleWeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    hazardous_goods_associated_with_vehicle: Optional[HazardousMaterials] = field(
        default=None,
        metadata={
            "name": "hazardousGoodsAssociatedWithVehicle",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    vehicle_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_vehicleExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class Visibility:
    """
    Details of atmospheric visibility.

    :ivar minimum_visibility_distance: The minimum distance, measured or
        estimated, beyond which drivers may be unable to clearly see a
        vehicle or an obstacle.
    :ivar visibility_extension:
    """
    minimum_visibility_distance: Optional[IntegerMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "minimumVisibilityDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    visibility_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_visibilityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class Wind:
    """
    Wind conditions on the road.

    :ivar wind_measurement_height: The height in metres above the road
        surface at which the wind is measured.
    :ivar wind_speed: The wind speed averaged over at least 10 minutes,
        measured at a default height of10 metres (meteorological
        standard) above the road surface, unless measurement height is
        specified.
    :ivar maximum_wind_speed: The maximum wind speed in a measurement
        period of 10 minutes.
    :ivar wind_direction_bearing: The average direction from which the
        wind blows, in terms of a bearing measured in degrees (0 - 359).
    :ivar maximum_wind_direction_bearing: The direction from which the
        maximum wind blows, in terms of a bearing measured in degrees (0
        - 359).
    :ivar wind_direction_compass: The average direction from which the
        wind blows, in terms of points of the compass.
    :ivar maximum_wind_direction_compass: The direction from which the
        maximum wind blows, in terms of points of the compass.
    :ivar wind_extension:
    """
    wind_measurement_height: Optional[int] = field(
        default=None,
        metadata={
            "name": "windMeasurementHeight",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    wind_speed: Optional[WindSpeedValue] = field(
        default=None,
        metadata={
            "name": "windSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    maximum_wind_speed: Optional[WindSpeedValue] = field(
        default=None,
        metadata={
            "name": "maximumWindSpeed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    wind_direction_bearing: Optional[DirectionBearingValue] = field(
        default=None,
        metadata={
            "name": "windDirectionBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    maximum_wind_direction_bearing: Optional[DirectionBearingValue] = field(
        default=None,
        metadata={
            "name": "maximumWindDirectionBearing",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    wind_direction_compass: Optional[DirectionCompassValue] = field(
        default=None,
        metadata={
            "name": "windDirectionCompass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    maximum_wind_direction_compass: Optional[DirectionCompassValue] = field(
        default=None,
        metadata={
            "name": "maximumWindDirectionCompass",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    wind_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_windExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class RoadSurfaceConditionMeasurements:
    """
    Measurements of the road surface condition which relate specifically to the
    weather.

    :ivar temperature_below_or_above_road_surface: Temperature
        measurements below or above the road surface.
    :ivar road_surface_temperature: The temperature measured on the road
        surface.
    :ivar protection_temperature: The road surface temperature down to
        which the surface is protected from freezing.
    :ivar de_icing_application_rate: Indicates the rate at which de-
        icing agents have been applied to the specified road.
    :ivar de_icing_concentration: Indicates the concentration of de-
        icing agent present in surface water on the specified road.
    :ivar friction: The friction value of the road.
    :ivar depth_of_snow: The depth of snow recorded on the road surface.
    :ivar water_film_thickness: The depth of standing water to be found
        on the road surface.
    :ivar ice_layer_thickness: The depth of ice to be found on the road
        surface.
    :ivar ice_percentage: The percentage of ice in the water.
    :ivar road_surface_condition_measurements_extension:
    """
    temperature_below_or_above_road_surface: List[TemperatureBelowOrAboveRoadSurface] = field(
        default_factory=list,
        metadata={
            "name": "temperatureBelowOrAboveRoadSurface",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    road_surface_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "roadSurfaceTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    protection_temperature: Optional[TemperatureValue] = field(
        default=None,
        metadata={
            "name": "protectionTemperature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    de_icing_application_rate: Optional[ApplicationRateValue] = field(
        default=None,
        metadata={
            "name": "deIcingApplicationRate",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    de_icing_concentration: Optional[KilogramsConcentrationValue] = field(
        default=None,
        metadata={
            "name": "deIcingConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    friction: Optional[FrictionValue] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    depth_of_snow: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "depthOfSnow",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    water_film_thickness: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "waterFilmThickness",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    ice_layer_thickness: Optional[FloatingPointMetreDistanceValue] = field(
        default=None,
        metadata={
            "name": "iceLayerThickness",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    ice_percentage: Optional[PercentageValue] = field(
        default=None,
        metadata={
            "name": "icePercentage",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    road_surface_condition_measurements_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_roadSurfaceConditionMeasurementsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )


@dataclass
class Validity:
    """
    Specification of validity, either explicitly or by a validity time period
    specification which may be discontinuous.

    :ivar validity_status: Specification of validity, either explicitly
        overriding the validity time specification or confirming it.
    :ivar overrunning: The activity or action described by the
        SituationRecord is still in progress, overrunning its planned
        duration as indicated in a previous version of this record or
        even in current version.
    :ivar validity_time_specification: A specification of periods of
        validity defined by overall bounding start and end times and the
        possible intersection of valid periods with exception periods
        (exception periods overriding valid periods).
    :ivar validity_extension:
    """
    validity_status: Optional[ValidityStatusEnum2] = field(
        default=None,
        metadata={
            "name": "validityStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    overrunning: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
    validity_time_specification: Optional[OverallPeriod] = field(
        default=None,
        metadata={
            "name": "validityTimeSpecification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
            "required": True,
        }
    )
    validity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "_validityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/3/common",
        }
    )
