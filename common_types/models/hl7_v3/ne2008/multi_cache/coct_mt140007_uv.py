from __future__ import annotations

from dataclasses import dataclass, field

from ..core.datatypes_base import (
    Ce,
    Cs,
    Ii,
    Sc,
)
from ..core.voc import (
    EntityClassDevice,
    EntityDeterminer,
    NullFlavor,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass(kw_only=True)
class CoctMt140007UvDevice:
    class Meta:
        name = "COCT_MT140007UV.Device"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: None | Ce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    manufacturer_model_name: None | Sc = field(
        default=None,
        metadata={
            "name": "manufacturerModelName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    software_name: None | Sc = field(
        default=None,
        metadata={
            "name": "softwareName",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: None | NullFlavor = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: EntityClassDevice = field(
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        }
    )
    determiner_code: EntityDeterminer = field(
        init=False,
        default=EntityDeterminer.INSTANCE,
        metadata={
            "name": "determinerCode",
            "type": "Attribute",
            "required": True,
        },
    )
