from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "1305a3d5074e398d143807afff9362e6"  # Replace with your actual API key

# Route for displaying the form
@app.route('/')
def index():
    return render_template('index.html')

# Route for checking multiple phone numbers
@app.route('/check-numbers', methods=['POST'])
def check_numbers():
    data = request.get_json()  # Get the JSON data sent from the frontend
    numbers = data.get('numbers')

    results = []

    # Iterate over the numbers and check each one
    for number in numbers:
        # Make a request to the Numverify API
        response = requests.get(
            "http://apilayer.net/api/validate",
            params={
                "access_key": API_KEY,
                "number": number,
                "country_code": "US",
                "format": 1
            }
        )
        api_data = response.json()

        # Determine the status
        valid = api_data.get("valid", False)
        status = "Positive" if valid else "Negative"
        allowed = "Allowed" if valid else "Not Allowed"
        line_type = api_data.get("line_type", "Unknown")
        carrier = api_data.get("carrier", "Unknown")

        # Store the result for the current number
        results.append({
            "status": status,
            "allowed": allowed,
            "line_type": line_type,
            "carrier": carrier
        })
    
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
