from dataclasses import dataclass, field
from typing import List, Optional
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.vms_pictogram_display_area_pictogram_sequencing_index_vms_pictogram import VmsPictogramDisplayAreaPictogramSequencingIndexVmsPictogram

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class VmsPictogramDisplayArea:
    """
    An area on a VMS used for the display of pictograms and associated
    supplemental information or instructions.

    :ivar synchronized_sequencing_with_text_pages: Indicates whether the
        sequence of pictograms are sequenced synchronously with the text
        pages. If there is a mismatch in the number of sequenced text
        pages and sequenced pictograms, the sequences are assumed to
        resynchronize at the start of each sequence.
    :ivar vms_pictogram:
    :ivar vms_pictogram_display_area_extension:
    """
    synchronized_sequencing_with_text_pages: Optional[bool] = field(
        default=None,
        metadata={
            "name": "synchronizedSequencingWithTextPages",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_pictogram: List[VmsPictogramDisplayAreaPictogramSequencingIndexVmsPictogram] = field(
        default_factory=list,
        metadata={
            "name": "vmsPictogram",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
    vms_pictogram_display_area_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "vmsPictogramDisplayAreaExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        }
    )
