from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.linear_element import LinearElement

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LinearElementByCode(LinearElement):
    """
    A linear element along a single linear object defined by its identifier
    or code in a road network reference model (specified in LinearElement
    class) which segments the road network according to specific business
    rules.

    :ivar linear_element_identifier: An identifier or code of a linear
        element (or link) in the road network reference model that is
        specified in the LinearElement class.
    :ivar linear_element_by_code_extension:
    """

    linear_element_identifier: Optional[str] = field(
        default=None,
        metadata={
            "name": "linearElementIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    linear_element_by_code_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "linearElementByCodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
