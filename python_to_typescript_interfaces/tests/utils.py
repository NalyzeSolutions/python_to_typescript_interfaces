import sys


def get_version() -> float:
    if sys.version_info.major < 3 or sys.version_info.minor < 8:
        raise Exception(
            "python-to-typescript-interfaces only supports Python 3.8 or above."
        )

    return float(sys.version_info.major) + (sys.version_info.minor / 10)