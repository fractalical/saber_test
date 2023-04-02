"""Global point for collected routers."""

from app.internal.pkg.models import Routes
from app.internal.routes import build_tasks

__all__ = ["__routes__"]

__routes__ = Routes(
    routers=(
        build_tasks.router,
    ),
)
