from flask import Blueprint, request, current_app, jsonify
from flask_cors import cross_origin
from flask_mail import Mail, Message

mail = Mail()

api_bp = Blueprint('api_bp', __name__, url_prefix="/api")

@api_bp.route("/message", methods=["GET", "POST"])
@cross_origin()
def message():
    data = request.get_json()
    key = request.headers["x-access"]

    # only allowing requests from a specific origin dictated in Config.py
    if request.headers['origin'] == current_app.config['CORS_ORIGIN']:
        if key == current_app.config["API_KEY"]:
            msg = Message(
                  'New SoftServv Message!',
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[current_app.config['MAIL_USERNAME']]
                  )
            msg.html = "New message from " + data["email"] + ":<br/><br/> " + data["message"]
            mail.send(msg)
            return jsonify({'message': 'Message Sent!'}, 200)
        else:
            print("key")
            return jsonify({'message': 'Invalid API Key'}, 403)
    else:
        print("origin")
        return jsonify({'message': 'Access Forbidden'}, 403)