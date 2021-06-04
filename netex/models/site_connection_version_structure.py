from dataclasses import dataclass, field
from typing import Optional
from netex.models.navigation_paths_rel_structure import NavigationPathsRelStructure
from netex.models.site_connection_end_structure import SiteConnectionEndStructure
from netex.models.transfer_version_structure import TransferVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteConnectionVersionStructure(TransferVersionStructure):
    class Meta:
        name = "SiteConnection_VersionStructure"

    from_value: Optional[SiteConnectionEndStructure] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to: Optional[SiteConnectionEndStructure] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    navigation_paths: Optional[NavigationPathsRelStructure] = field(
        default=None,
        metadata={
            "name": "navigationPaths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
