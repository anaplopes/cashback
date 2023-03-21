from fastapi import FastAPI
from src.routers.v1.auth import auth_router
from src.routers.v1.dealer import dealer_router
from src.routers.v1.cashback import cashback_router
from src.routers.v1.purchase import purchase_router
from fastapi_healthcheck import HealthCheckFactory, healthCheckRoute


# Core Application Instance
app = FastAPI(
    title="Cashback",
    description="Sistema de cashback para compra de revendedoras.",
    version="0.1.0",
    debug=True,
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
app.include_router(auth_router)
app.include_router(dealer_router)
app.include_router(cashback_router)
app.include_router(purchase_router)
