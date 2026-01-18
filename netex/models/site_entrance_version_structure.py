from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .entrance_enumeration import EntranceEnumeration
from .multilingual_string import MultilingualString
from .site_component_version_structure import SiteComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteEntranceVersionStructure(SiteComponentVersionStructure):
    class Meta:
        name = "SiteEntrance_VersionStructure"

    public_code: None | str = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_type: None | EntranceEnumeration = field(
        default=None,
        metadata={
            "name": "EntranceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_external: None | bool = field(
        default=None,
        metadata={
            "name": "IsExternal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_entry: None | bool = field(
        default=None,
        metadata={
            "name": "IsEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_exit: None | bool = field(
        default=None,
        metadata={
            "name": "IsExit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: None | Decimal = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: None | Decimal = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dropped_kerb_outside: None | bool = field(
        default=None,
        metadata={
            "name": "DroppedKerbOutside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    drop_off_point_close: None | bool = field(
        default=None,
        metadata={
            "name": "DropOffPointClose",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
