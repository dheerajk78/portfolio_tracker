import logging
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Function executed successfully.")
    return func.HttpResponse("Function is alive.", status_code=200)
