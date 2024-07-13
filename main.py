from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    os_info = parse_user_agent(user_agent)
    return f"<p>Seu sistema operacional é: {os_info}</p>"

def parse_user_agent(user_agent):
    if 'Windows' in user_agent:
        return 'Windows'
    elif 'Android' in user_agent:
        return 'Android'
    elif 'iPhone' in user_agent or 'iPad' in user_agent:
        return 'iOS'
    else:
        return 'Desconhecido'

if __name__ == '__main__':
    app.run(debug=True)
