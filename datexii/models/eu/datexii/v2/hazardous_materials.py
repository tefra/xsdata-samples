from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.dangerous_goods_regulations_enum import (
    DangerousGoodsRegulationsEnum,
)
from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class HazardousMaterials:
    """
    Details of hazardous materials.

    :ivar chemical_name: The chemical name of the hazardous substance
        carried by the vehicle.
    :ivar dangerous_goods_flash_point: The temperature at which the
        vapour from a hazardous substance will ignite in air.
    :ivar dangerous_goods_regulations: The code defining the
        regulations, international or national, applicable for a means
        of transport.
    :ivar hazard_code_identification: The dangerous goods description
        code.
    :ivar hazard_code_version_number: The version/revision number of
        date of issuance of the hazardous material code used.
    :ivar hazard_substance_item_page_number: A number giving additional
        hazard code classification of a goods item within the applicable
        dangerous goods regulation.
    :ivar trem_card_number: The identification of a transport emergency
        card giving advice for emergency actions.
    :ivar undg_number: A unique serial number assigned within the United
        Nations to substances and articles contained in a list of the
        dangerous goods most commonly carried.
    :ivar volume_of_dangerous_goods: The volume of dangerous goods on
        the vehicle(s) reported in a traffic/travel situation.
    :ivar weight_of_dangerous_goods: The weight of dangerous goods on
        the vehicle(s) reported in a traffic/travel situation.
    :ivar hazardous_materials_extension:
    """

    chemical_name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "chemicalName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    dangerous_goods_flash_point: None | float = field(
        default=None,
        metadata={
            "name": "dangerousGoodsFlashPoint",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    dangerous_goods_regulations: None | DangerousGoodsRegulationsEnum = field(
        default=None,
        metadata={
            "name": "dangerousGoodsRegulations",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    hazard_code_identification: None | str = field(
        default=None,
        metadata={
            "name": "hazardCodeIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    hazard_code_version_number: None | int = field(
        default=None,
        metadata={
            "name": "hazardCodeVersionNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    hazard_substance_item_page_number: None | str = field(
        default=None,
        metadata={
            "name": "hazardSubstanceItemPageNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    trem_card_number: None | str = field(
        default=None,
        metadata={
            "name": "tremCardNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    undg_number: None | str = field(
        default=None,
        metadata={
            "name": "undgNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    volume_of_dangerous_goods: None | float = field(
        default=None,
        metadata={
            "name": "volumeOfDangerousGoods",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    weight_of_dangerous_goods: None | float = field(
        default=None,
        metadata={
            "name": "weightOfDangerousGoods",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    hazardous_materials_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "hazardousMaterialsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
