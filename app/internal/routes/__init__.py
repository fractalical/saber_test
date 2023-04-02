"""Global point for collected routers."""

from app.internal.pkg.models import Routes

__all__ = ["__routes__"]

__routes__ = Routes(
    routers=(
        ...
    ),
)
