from flask import Flask, request, jsonify
import subprocess
import json
import os
import tempfile

app = Flask(__name__)

@app.route('/execute', methods=['POST'])
def execute_script():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    script = request.json.get('script')
    if not script:
        return jsonify({"error": "No script provided"}), 400

    if 'def main():' not in script:
        return jsonify({"error": "Script must contain a main() function"}), 400

    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False, dir='/tmp') as temp_file:
        temp_file.write(script)
        temp_file_path = temp_file.name

    try:
        result = subprocess.run(
            ['/usr/local/bin/python3', temp_file_path],
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            return jsonify({"error": f"Script execution failed: {result.stderr}"}), 500

        try:
            output = json.loads(result.stdout)
            return jsonify(output)
        except json.JSONDecodeError:
            return jsonify({
                "error": "Script output is not valid JSON",
                "stdout": result.stdout,
                "stderr": result.stderr
            }), 500

    except subprocess.TimeoutExpired:
        return jsonify({"error": "Script execution timed out"}), 500
    finally:
        os.unlink(temp_file_path)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
