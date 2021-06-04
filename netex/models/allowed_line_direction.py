from dataclasses import dataclass
from netex.models.allowed_line_direction_version_structure import AllowedLineDirectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AllowedLineDirection(AllowedLineDirectionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
