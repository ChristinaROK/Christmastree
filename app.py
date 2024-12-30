from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Render가 제공하는 PORT 환경 변수 사용
    app.run(host="0.0.0.0", port=port)       # 모든 외부 요청을 수락