from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class PollutantTypeEnum(Enum):
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
