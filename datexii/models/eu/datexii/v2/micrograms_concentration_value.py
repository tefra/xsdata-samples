from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class MicrogramsConcentrationValue(DataValue):
    """
    A measured or calculated value of concentration of a substance in micrograms
    per unit volume.

    :ivar micrograms_concentration: A value of the amount of a substance
        in a given volume (concentration) expressed in µg/m3
        (microgrammes/cubic metre).
    :ivar micrograms_concentration_value_extension:
    """

    micrograms_concentration: Optional[float] = field(
        default=None,
        metadata={
            "name": "microgramsConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    micrograms_concentration_value_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "microgramsConcentrationValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
