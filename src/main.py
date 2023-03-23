from fastapi import FastAPI
from src.settings import settings
from src.routes.v1.auth import auth_router
from src.routes.v1.reseller import reseller_router
from src.routes.v1.cashback import cashback_router
from src.routes.v1.purchase import purchase_router
from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute


# Core Application Instance
def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        description=settings.APP_DESCRIPTION,
        version=settings.API_VERSION,
    )

    # Add Health Checks
    _healthChecks = HealthCheckFactory()
    app.add_api_route(
        "/health",
        endpoint=healthCheckRoute(factory=_healthChecks),
        tags=["health"],
        name="health_check",
        description="Rota para validar o funcionamento da API.",
    )

    # Add Routers
    app.include_router(auth_router, prefix=settings.API_PREFIX)
    app.include_router(reseller_router, prefix=settings.API_PREFIX)
    app.include_router(cashback_router, prefix=settings.API_PREFIX)
    app.include_router(purchase_router, prefix=settings.API_PREFIX)

    # Initialise Data Model
    from src.models.base import init

    init()

    return app
