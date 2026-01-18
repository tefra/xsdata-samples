from dataclasses import dataclass, field
from typing import Optional

from .entity_in_version_structure import DataManagedObjectStructure
from .info_links_rel_structure import InfoLinksRelStructure
from .multilingual_string import MultilingualString
from .private_code import PrivateCode
from .purpose_of_grouping_ref import PurposeOfGroupingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class GroupOfEntitiesVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "GroupOfEntities_VersionStructure"

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
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    purpose_of_grouping_ref: PurposeOfGroupingRef | None = field(
        default=None,
        metadata={
            "name": "PurposeOfGroupingRef",
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
    info_links: InfoLinksRelStructure | None = field(
        default=None,
        metadata={
            "name": "infoLinks",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
