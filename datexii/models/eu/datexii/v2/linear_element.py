from dataclasses import dataclass, field
from typing import Optional

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.linear_element_nature_enum import (
    LinearElementNatureEnum,
)
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class LinearElement:
    """
    A linear element along a single linear object, consistent with ISO
    19148 definitions.

    :ivar road_name: Name of the road of which the linear element forms
        a part.
    :ivar road_number: Identifier/number of the road of which the linear
        element forms a part.
    :ivar linear_element_reference_model: The identifier of a road
        network reference model which segments the road network
        according to specific business rules.
    :ivar linear_element_reference_model_version: The version of the
        identified road network reference model.
    :ivar linear_element_nature: An indication of the nature of the
        linear element.
    :ivar linear_element_extension:
    """

    road_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "roadName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    road_number: str | None = field(
        default=None,
        metadata={
            "name": "roadNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    linear_element_reference_model: str | None = field(
        default=None,
        metadata={
            "name": "linearElementReferenceModel",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    linear_element_reference_model_version: str | None = field(
        default=None,
        metadata={
            "name": "linearElementReferenceModelVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    linear_element_nature: LinearElementNatureEnum | None = field(
        default=None,
        metadata={
            "name": "linearElementNature",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    linear_element_extension: ExtensionType | None = field(
        default=None,
        metadata={
            "name": "linearElementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
