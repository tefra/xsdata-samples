from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PublicEventType2Enum(Enum):
    """
    Additional types for a public event.

    :cvar OPEN_AIR_CONCERT: Open air concert
    :cvar SOUND_AND_LIGHT_SHOW: Sound and light show.
    :cvar ART_EVENT: Art event
    :cvar FLOWER_EVENT: Flower event
    :cvar BEER_FESTIVAL: Beer festival
    :cvar FOOD_FESTIVAL: Food festival
    :cvar WINE_FESTIVAL: Wine festival
    :cvar THEATRICAL_EVENT: Theatrical event
    :cvar FIREWORK_DISPLAY: Firework display
    :cvar STREET_FESTIVAL: Street festival
    :cvar FILM_FESTIVAL: Film festival
    :cvar UNKNOWN: Service provider does not know at time of message
        generation.
    :cvar OTHER: Some other kind of public event.
    """
    OPEN_AIR_CONCERT = "openAirConcert"
    SOUND_AND_LIGHT_SHOW = "soundAndLightShow"
    ART_EVENT = "artEvent"
    FLOWER_EVENT = "flowerEvent"
    BEER_FESTIVAL = "beerFestival"
    FOOD_FESTIVAL = "foodFestival"
    WINE_FESTIVAL = "wineFestival"
    THEATRICAL_EVENT = "theatricalEvent"
    FIREWORK_DISPLAY = "fireworkDisplay"
    STREET_FESTIVAL = "streetFestival"
    FILM_FESTIVAL = "filmFestival"
    UNKNOWN = "unknown"
    OTHER = "other"
