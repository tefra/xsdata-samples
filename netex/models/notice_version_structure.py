from dataclasses import dataclass, field

from .delivery_variants_rel_structure import DeliveryVariantsRelStructure
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .private_code import PrivateCode
from .type_of_notice_ref import TypeOfNoticeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NoticeVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Notice_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    text: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Text",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: str | None = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_code: str | None = field(
        default=None,
        metadata={
            "name": "ShortCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: PrivateCode | None = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_notice_ref: TypeOfNoticeRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfNoticeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    can_be_advertised: bool | None = field(
        default=None,
        metadata={
            "name": "CanBeAdvertised",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    driver_display_text: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "DriverDisplayText",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    variants: DeliveryVariantsRelStructure | None = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
