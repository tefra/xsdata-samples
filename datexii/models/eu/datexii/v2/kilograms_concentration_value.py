from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.data_value import DataValue
from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass(kw_only=True)
class KilogramsConcentrationValue(DataValue):
    """
    A measured or calculated value of concentration of a substance in grams
    per unit volume.

    :ivar kilograms_concentration: A value defining the amount of a
        substance in a given volume (concentration) expressed in
        kilograms per cubic metre.
    :ivar kilograms_concentration_value_extension:
    """

    kilograms_concentration: float = field(
        metadata={
            "name": "kilogramsConcentration",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        }
    )
    kilograms_concentration_value_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "kilogramsConcentrationValueExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
