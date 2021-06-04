from dataclasses import dataclass
from netex.models.branding_version_structure import BrandingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class Branding(BrandingVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
