import logging
import traceback
import azure.functions as func

try:
    from . import tracker
except Exception:
    logging.error("Failed to import tracker module")
    logging.error(traceback.format_exc())
    raise

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        import os
        csv_path = os.path.join(os.path.dirname(__file__), "transactions.csv")
        logging.info(f"Using CSV path: {csv_path}")

        summary = tracker.get_portfolio_summary(csv_path=csv_path)
        return func.HttpResponse(summary, status_code=200)
    except Exception:
        logging.error("Error while executing portfolio summary:")
        logging.error(traceback.format_exc())
        return func.HttpResponse("Internal Server Error", status_code=500)
