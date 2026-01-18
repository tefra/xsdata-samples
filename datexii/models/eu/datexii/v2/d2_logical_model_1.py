from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.exchange import Exchange
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.payload_publication import PayloadPublication

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class D2LogicalModel1:
    """
    The DATEX II logical model comprising exchange, content payload and
    management sub-models.
    """

    class Meta:
        name = "D2LogicalModel"

    exchange: None | Exchange = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    payload_publication: None | PayloadPublication = field(
        default=None,
        metadata={
            "name": "payloadPublication",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    d2_logical_model_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "d2LogicalModelExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    model_base_version: str = field(
        init=False,
        default="2",
        metadata={
            "name": "modelBaseVersion",
            "type": "Attribute",
            "required": True,
        },
    )
