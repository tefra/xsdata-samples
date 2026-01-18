from __future__ import annotations

from dataclasses import dataclass, field

from datexii.models.eu.datexii.v2.extension_type import ExtensionType
from datexii.models.eu.datexii.v2.multilingual_string import MultilingualString
from datexii.models.eu.datexii.v2.point_coordinates import PointCoordinates
from datexii.models.eu.datexii.v2.referent_type_enum import ReferentTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


@dataclass
class Referent:
    """
    A referent on a linear object that has a known location such as a node,
    a reference marker (e.g. a markerpost), an intersection etc.

    :ivar referent_identifier: The identifier of the referent, unique on
        the specified linear element (i.e. road or part of).
    :ivar referent_name: The name of the referent, e.g. a junction or
        intersection name.
    :ivar referent_type: The type of the referent.
    :ivar referent_description: Description of the referent.
    :ivar point_coordinates:
    :ivar referent_extension:
    """

    referent_identifier: None | str = field(
        default=None,
        metadata={
            "name": "referentIdentifier",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
            "max_length": 1024,
        },
    )
    referent_name: None | str = field(
        default=None,
        metadata={
            "name": "referentName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "max_length": 1024,
        },
    )
    referent_type: None | ReferentTypeEnum = field(
        default=None,
        metadata={
            "name": "referentType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
            "required": True,
        },
    )
    referent_description: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "referentDescription",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    point_coordinates: None | PointCoordinates = field(
        default=None,
        metadata={
            "name": "pointCoordinates",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
    referent_extension: None | ExtensionType = field(
        default=None,
        metadata={
            "name": "referentExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2/2_0",
        },
    )
