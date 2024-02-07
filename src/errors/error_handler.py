from src.views.http_types.http_response import HttpResponse
from .errors_types.http_unprocessable_entity_error import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):
        # Enviar um log
        # Enviar um e-mail
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [{
                    "tittle": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "tittle": "Server Error",
                "detail": str(error) 
            }]
        }
    )
