from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "1305a3d5074e398d143807afff9362e6"  # Replace with your actual API key

@app.route('/check-number', methods=['POST'])
def check_number():
    data = request.get_json()
    number = data.get('number')

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

    # Prepare the response
    result = {
        "valid": valid,
        "status": status,
        "allowed": allowed,
        "line_type": line_type,
        "carrier": carrier
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
