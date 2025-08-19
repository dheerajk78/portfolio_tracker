import logging
import azure.functions as func
import os

try:
    import tracker
except Exception as e:
    logging.exception("Failed to import tracker module.")

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Use absolute path for CSV relative to this file
        csv_path = os.path.join(os.path.dirname(__file__), "transactions.csv")
        logging.info(f"Using CSV path: {csv_path}")

        summary = tracker.get_portfolio_summary(csv_path=csv_path)
        return func.HttpResponse(summary, status_code=200)
    except Exception as e:
        logging.exception("Error while executing portfolio summary:")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
