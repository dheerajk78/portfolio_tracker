import logging
import azure.functions as func
from . import tracker

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing portfolio tracker function.')

    try:
        summary = tracker.get_portfolio_summary()
        return func.HttpResponse(summary, mimetype="text/plain")
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
