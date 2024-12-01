from flask import Flask, request, jsonify
from flask_cors import CORS
from user_management import UserManagementSystem
import pytest
import io
import sys

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests

user_management_system = UserManagementSystem()

# Existing routes...

# New route for running tests
@app.route('/run-tests', methods=['GET'])
def run_tests():
    # Capture stdout to get test results
    captured_output = io.StringIO()
    sys.stdout = captured_output

    # Run pytest
    pytest.main(['-v', 'test_user_management_system.py'])

    # Restore stdout
    sys.stdout = sys.__stdout__

    # Get the captured output
    test_results = captured_output.getvalue()

    return jsonify({"results": test_results}), 200

if __name__ == '__main__':
    app.run(debug=True)