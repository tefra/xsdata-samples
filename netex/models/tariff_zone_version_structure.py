from dataclasses import dataclass, field

from .presentation_structure import PresentationStructure
from .print_presentation_structure import PrintPresentationStructure
from .zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TariffZoneVersionStructure(ZoneVersionStructure):
    class Meta:
        name = "TariffZone_VersionStructure"

    presentation: PresentationStructure | None = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    printed_presentation: PrintPresentationStructure | None = field(
        default=None,
        metadata={
            "name": "PrintedPresentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
