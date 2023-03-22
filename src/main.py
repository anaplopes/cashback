from fastapi import FastAPI
from src.settings import settings
from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute


# Core Application Instance
def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.NAME, description=settings.DESCRIPTION, version=settings.VERSION
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
    from src.routes.v1.auth import auth_router

    app.include_router(auth_router, prefix=settings.PREFIX_API)

    from src.routes.v1.reseller import reseller_router

    app.include_router(reseller_router, prefix=settings.PREFIX_API)

    from src.routes.v1.cashback import cashback_router

    app.include_router(cashback_router, prefix=settings.PREFIX_API)

    from src.routes.v1.purchase import purchase_router

    app.include_router(purchase_router, prefix=settings.PREFIX_API)

    return app
