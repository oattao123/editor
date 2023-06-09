from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json.get('code', '')
    result = execute_code(code)
    return jsonify({'output': result})

def execute_code(code):
    try:
        process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, error = process.communicate()
        if output:
            return output.strip()
        elif error:
            return error.strip()
        else:
            return "No output"
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
