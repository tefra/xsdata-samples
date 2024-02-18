from dataclasses import dataclass
from .responsibility_role_version_structure import (
    ResponsibilityRoleVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class ResponsibilityRole(ResponsibilityRoleVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
