import logging
import azure.functions as func

try:
    from . import tracker
except Exception as e:
    logging.exception("Failed to import tracker module")
    raise  # re-raise to get the error in logs and see the traceback

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        import os
        csv_path = os.path.join(os.path.dirname(__file__), "transactions.csv")
        logging.info(f"Using CSV path: {csv_path}")

        summary = tracker.get_portfolio_summary(csv_path=csv_path)
        return func.HttpResponse(summary, status_code=200)
    except Exception as e:
        logging.exception("Error while executing portfolio summary:")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
