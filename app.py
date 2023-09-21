from pyopa import Client
from functools import wraps
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize OPA client and load policy
client = Client()
policy = """
package example
default allow = false
allow {
   input.method == "GET"
}
"""
client.load_policy(policy)

# Custom decorator for access control
def enforce_access(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        input_data = {
            "method": request.method,
            # Add other input data as needed
        }

        if client.evaluate("example.allow", input_data):
            return func(*args, **kwargs)
        else:
            return jsonify({"error": "Access denied"})

    return wrapper

# Apply access control to routes using the decorator
@app.route('/resource', methods=['GET'])
@enforce_access
def get_resource():
    # Implement your resource retrieval logic here
    return jsonify({"message": "Resource data"})

if __name__ == '__main__':
    app.run(debug=True)
