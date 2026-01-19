from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from sdmx_ml.models.data_source_type import DataSourceType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry"


@dataclass(frozen=True, kw_only=True)
class RegistrationType:
    """
    Registration provides the information needed for data and reference
    metadata set registration.

    A data source must be supplied here if not already provided in the
    provision agreement. The data set or metadata set must be associated
    with a provision agreement, a metadata flow, or a dataflow definition.
    If possible, the provision agreement should be specified. Only in cases
    where this is not possible should the dataflow or metadata flow be
    used.

    :ivar provision_agreement: ProvisionAgreement provides a reference
        to the provision agreement that the data is being registered
        against.
    :ivar datasource: Datasource identifies the data source(s) where the
        registered data can be retrieved.
    :ivar id: The id attribute holds a registry assigned identification
        for the registration. This must be provided in a response
        message (unless an error occurred while submitting a new
        registration), and should be included when updating or deleting
        a registration.
    :ivar valid_from: The validFrom attribute provides an inclusive
        start date for providing supplemental validity information about
        the registration, so that data visibility from the registry can
        be controlled by the registrant.
    :ivar valid_to: The validFrom attribute provides an inclusive end
        date for providing supplemental validity information about the
        registration, so that data visibility from the registry can be
        controlled by the registrant.
    :ivar last_updated: The lastUpdated attribute provides a timestamp
        for the last time the data source was updated.
    :ivar index_time_series: The indexTimeSeries, if true, indicates
        that the registry must index all time series for the registered
        data. The default value is false, and the attribute will always
        be assumed false when the provision agreement references a
        metadata flow.
    :ivar index_data_set: The indexDataSet, if true, indicates that the
        registry must index the range of actual (present) values for
        each dimension of the data set or identifier component of the
        metadata set (as indicated in the set's structure definition).
        The default value is false.
    :ivar index_attributes: The indexAttributes, if true, indicates that
        the registry must index the range of actual (present) values for
        each attribute of the data set or the presence of the metadata
        attributes of the metadata set (as indicated in the set's
        structure definition). The default value is false.
    :ivar index_reporting_period: The indexReportingPeriod, if true,
        indicates that the registry must index the time period ranges
        for which data is present for the data source. The default value
        is false, and the attribute will always be assumed false when
        the provision agreement references a metadata flow.
    """

    provision_agreement: str = field(
        metadata={
            "name": "ProvisionAgreement",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry",
            "required": True,
            "pattern": r".+\.registry\.ProvisionAgreement=.+",
        }
    )
    datasource: DataSourceType = field(
        metadata={
            "name": "Datasource",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/registry",
            "required": True,
        }
    )
    id: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[A-Za-z0-9_@$\-]+",
        },
    )
    valid_from: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "validFrom",
            "type": "Attribute",
        },
    )
    valid_to: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "validTo",
            "type": "Attribute",
        },
    )
    last_updated: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "lastUpdated",
            "type": "Attribute",
        },
    )
    index_time_series: bool = field(
        default=False,
        metadata={
            "name": "indexTimeSeries",
            "type": "Attribute",
        },
    )
    index_data_set: bool = field(
        default=False,
        metadata={
            "name": "indexDataSet",
            "type": "Attribute",
        },
    )
    index_attributes: bool = field(
        default=False,
        metadata={
            "name": "indexAttributes",
            "type": "Attribute",
        },
    )
    index_reporting_period: bool = field(
        default=False,
        metadata={
            "name": "indexReportingPeriod",
            "type": "Attribute",
        },
    )
