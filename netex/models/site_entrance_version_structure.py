from dataclasses import dataclass, field
from decimal import Decimal

from .entrance_enumeration import EntranceEnumeration
from .multilingual_string import MultilingualString
from .site_component_version_structure import SiteComponentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteEntranceVersionStructure(SiteComponentVersionStructure):
    class Meta:
        name = "SiteEntrance_VersionStructure"

    public_code: str | None = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    entrance_type: EntranceEnumeration | None = field(
        default=None,
        metadata={
            "name": "EntranceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_external: bool | None = field(
        default=None,
        metadata={
            "name": "IsExternal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_entry: bool | None = field(
        default=None,
        metadata={
            "name": "IsEntry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    is_exit: bool | None = field(
        default=None,
        metadata={
            "name": "IsExit",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    width: Decimal | None = field(
        default=None,
        metadata={
            "name": "Width",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    height: Decimal | None = field(
        default=None,
        metadata={
            "name": "Height",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    dropped_kerb_outside: bool | None = field(
        default=None,
        metadata={
            "name": "DroppedKerbOutside",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    drop_off_point_close: bool | None = field(
        default=None,
        metadata={
            "name": "DropOffPointClose",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
