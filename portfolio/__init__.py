import logging
import azure.functions as func
import os
from . import tracker

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Processing portfolio tracker function.')

    try:

        csv_path = os.path.join(os.path.dirname(__file__), "transactions.csv")
        summary = tracker.get_portfolio_summary(csv_path=csv_path)
        return func.HttpResponse(summary, mimetype="text/plain")
    except Exception as e:
        logging.exception("Unhandled exception in portfolio function:")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
