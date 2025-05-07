# Phone Number Validation API

This project is a **Flask-based web application** that allows users to validate phone numbers using the **Numverify API**. It provides a simple interface where users can input a phone number, and the app returns detailed information such as:
- Validity of the number
- Status (Positive/Negative)
- Whether the number is allowed or not
- Line type (Mobile, Landline, VoIP, etc.)
- Carrier information (Telecom provider)

## Features
- **Validate multiple phone numbers at once**: Users can paste multiple numbers in the input field and get the results for each one.
- **User-friendly interface**: Simple, clean UI that displays the validation results clearly.
- **Built with Flask**: The backend is powered by Flask, and the frontend is a responsive HTML form.

## Technologies Used
- **Backend**: Python, Flask
- **API**: Numverify API
- **Frontend**: HTML, CSS, JavaScript
- **External Libraries**: 
  - `requests` (for making HTTP requests to the API)
  - `Flask` (web framework)

## Prerequisites
Before running this application, you need to install the following dependencies:
- Python 3.x
- Flask
- requests

You can install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
