from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class OpenlrGridAttributes:
    """
    attributes required for the grid method.

    :ivar openlr_num_columns: the number that the base rectangle should
        be multiplied in the east direction
    :ivar openlr_num_rows: the number that the base rectangle should be
        multiplied in the north direction
    :ivar openlr_grid_attributes_extension:
    """

    openlr_num_columns: int | None = field(
        default=None,
        metadata={
            "name": "openlrNumColumns",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_num_rows: int | None = field(
        default=None,
        metadata={
            "name": "openlrNumRows",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    openlr_grid_attributes_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "openlrGridAttributesExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
