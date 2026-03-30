from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)


def classify_age(age):
    """Classify student based on age."""
    if age < 18:
        return "Junior Student"
    elif age < 25:
        return "Undergraduate Student"
    elif age < 35:
        return "Graduate / Postgraduate Student"
    else:
        return "Continuing Education Student"


def generate_message(name, subject, interests):
    """Generate a personalized message for the student."""
    interest_str = ", ".join(interests) if isinstance(interests, list) else interests
    msg = (
        f"Welcome, {name}! Your registration in {subject} has been recorded. "
    )
    if interest_str:
        msg += f"Your interest in {interest_str} will be a great asset. "
    msg += "We look forward to your journey with us!"
    return msg


@app.route("/", methods=["GET"])
def index():
    """Health check / welcome route."""
    return jsonify({
        "service": "Flask Backend",
        "status": "running",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })


@app.route("/process", methods=["POST"])
def process():
    """Process form data sent from the Express frontend."""
    payload = request.get_json(force=True)

    if not payload:
        return jsonify({"error": "No JSON payload received"}), 400

    # Extract fields
    name = payload.get("name", "").strip()
    email = payload.get("email", "").strip()
    age_raw = payload.get("age", 0)
    subject = payload.get("subject", "").strip()
    message = payload.get("message", "").strip()
    gender = payload.get("gender", "").strip()
    interest = payload.get("interest", [])

    # Validate required fields
    if not name or not email:
        return jsonify({"error": "Name and email are required."}), 422

    # Convert age safely
    try:
        age = int(age_raw)
        if age <= 0 or age > 120:
            return jsonify({"error": "Age must be between 1 and 120."}), 422
    except (ValueError, TypeError):
        return jsonify({"error": "Age must be a valid number."}), 422

    # Normalize interests to a list
    if isinstance(interest, str):
        interest = [interest] if interest else []

    # Build response data
    processed = {
        "name": name,
        "email": email,
        "age": age,
        "age_category": classify_age(age),
        "subject": subject,
        "gender": gender,
        "interest": ", ".join(interest) if interest else "Not specified",
        "message": message,
        "submitted_at": datetime.utcnow().isoformat() + "Z",
        "processed_by": "Flask Backend v1.0"
    }

    personalized_message = generate_message(name, subject, interest)

    return jsonify({
        "status": "success",
        "message": personalized_message,
        "data": processed
    }), 200


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint for Docker/orchestration."""
    return jsonify({"status": "ok", "service": "backend", "timestamp": datetime.utcnow().isoformat() + "Z"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
