from flask import jsonify

def register_routes(app):
    @app.route("/api/data")
    def get_data():
        return jsonify({"data": [1, 2, 3]})
