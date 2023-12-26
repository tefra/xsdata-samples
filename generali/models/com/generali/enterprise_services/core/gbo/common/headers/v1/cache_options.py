from enum import Enum

__NAMESPACE__ = (
    "http://generali.com/enterprise-services/core/gbo/common/headers/v1"
)


class CacheOptions(Enum):
    """
    :cvar YES: <description xmlns="">Use cache during queries by default
        (code may override this).</description>
    :cvar NO: <description xmlns="">Cache must be ignored, retrieve data
        from the back-end instead</description>
    :cvar DEFAULT: <description xmlns="">The service can decide whether
        or not to use a cache</description>
    """

    YES = "yes"
    NO = "no"
    DEFAULT = "default"
