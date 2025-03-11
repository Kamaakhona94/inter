from flask import Flask, request
import subprocess
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO, filename='webhook.log')

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        if request.method == 'POST':
            data = request.get_json()
            logging.info(f"Received webhook: {data}")
            if data.get('zen') or data.get('hook_id'):
                logging.info("Webhook ping received")
                return "Webhook ping received", 200
            elif data.get('ref') and 'push' in request.headers.get('X-GitHub-Event', ''):
                logging.info("Push event detected")
                subprocess.run(['python', 'gold_bot.py', '--test'], check=True)
                logging.info("gold_bot.py executed successfully")
                return "Webhook processed", 200
            else:
                logging.warning("Unknown event type")
                return "Unknown event", 400
        return "Method not allowed", 405
    except Exception as e:
        logging.error(f"Webhook error: {e}")
        return f"Error: {e}", 500

if __name__ == '__main__':
    app.run(port=5000, ssl_context='adhoc')
