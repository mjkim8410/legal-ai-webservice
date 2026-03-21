from flask import Blueprint, request, jsonify, current_app

main_routes = Blueprint("main_routes", __name__)

@main_routes.route("/", methods=["GET"])
def home():
    return "<h1>Welcome to your LLM web service!</h1>"

@main_routes.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_query = data.get("query")
    if not user_query:
        return jsonify({"error": "query field is required"}), 400

    answer = current_app.qwen.answer_query(user_query)

    return jsonify({
        "query": user_query,
        "answer": answer
    })