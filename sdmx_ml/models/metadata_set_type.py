from __future__ import annotations

from dataclasses import dataclass, field
from typing import ForwardRef, Optional, Union

from xsdata.models.datatype import XmlDate, XmlDateTime, XmlPeriod

from sdmx_ml.models.action_type import ActionType
from sdmx_ml.models.attribute_type_1 import Attribute1
from sdmx_ml.models.metadata_set_base_type import MetadataSetBaseType

__NAMESPACE__ = (
    "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/metadata/generic"
)


@dataclass(frozen=True)
class MetadataSetType(MetadataSetBaseType):
    """
    MetadataSetType describes the structure for a metadata set, which
    contains a collection of reported metadata against a set of targets.

    The targets should conform to the restrictions described by the
    metadata provision or the metadataflow. Note that this is maintainble,
    and as such must specify in agency. In this case, the agency is the
    metadata provider. If a metadata provision agreement is referenced, it
    is assumed that the metadata provider described in the provision will
    be the same as the agency for this set.

    :ivar metadata_provision_agreement_or_metadataflow:
    :ivar target: Target references the target structures for which
        metadata is being reported. These must conform with the
        constraints defined by the metadata provision agreement and/or
        the metadataflow.
    :ivar attribute: Att elements hold the reported metadata attribute
        values being reported in the metadata set. These conform to the
        metadata structure defintion
    :ivar action: The action attribute indicates whether the file is
        appending, replacing, or deleting.
    :ivar reporting_begin_date: The reportingBeginDate indicates the
        inclusive start time of the data reported in the data or
        metadata set.
    :ivar reporting_end_date: The reportingEndDate indicates the
        inclusive end time of the data reported in the data or metadata
        set.
    :ivar publication_year: The publicationYear holds the ISO 8601 four-
        digit year.
    :ivar publication_period: The publicationPeriod specifies the period
        of publication of the data or metadata in terms of whatever
        provisioning agreements might be in force (i.e., "Q1 2005" if
        that is the time of publication for a data set published on a
        quarterly basis).
    """

    metadata_provision_agreement_or_metadataflow: MetadataSetType.MetadataProvisionAgreement | MetadataSetType.Metadataflow | None = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MetadataProvisionAgreement",
                    "type": ForwardRef(
                        "MetadataSetType.MetadataProvisionAgreement"
                    ),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/metadata/generic",
                },
                {
                    "name": "Metadataflow",
                    "type": ForwardRef("MetadataSetType.Metadataflow"),
                    "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/metadata/generic",
                },
            ),
        },
    )
    target: tuple[str, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Target",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/metadata/generic",
            "pattern": r".+\)(\.[A-Za-z0-9_@$\-]+(\.[A-Za-z0-9_@$\-]+)*)?|.+\)(\.\*(\.\*)*)?",
        },
    )
    attribute: tuple[Attribute1, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/metadata/generic",
        },
    )
    action: ActionType | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    reporting_begin_date: XmlPeriod | XmlDate | XmlDateTime | None = (
        field(
            default=None,
            metadata={
                "name": "reportingBeginDate",
                "type": "Attribute",
            },
        )
    )
    reporting_end_date: XmlPeriod | XmlDate | XmlDateTime | None = (
        field(
            default=None,
            metadata={
                "name": "reportingEndDate",
                "type": "Attribute",
            },
        )
    )
    publication_year: XmlPeriod | None = field(
        default=None,
        metadata={
            "name": "publicationYear",
            "type": "Attribute",
        },
    )
    publication_period: XmlPeriod | XmlDate | XmlDateTime | str | None = field(
        default=None,
        metadata={
            "name": "publicationPeriod",
            "type": "Attribute",
            "pattern": r".{5}A1.*",
        },
    )

    @dataclass(frozen=True)
    class MetadataProvisionAgreement:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.registry\.MetadataProvisionAgreement=.+",
            },
        )

    @dataclass(frozen=True)
    class Metadataflow:
        value: str | None = field(
            default=None,
            metadata={
                "required": True,
                "pattern": r".+\.metadatastructure\.Metadataflow=.+",
            },
        )
