from flask import Flask, request, jsonify

app = Flask(__name__)

notes = []

# CREATE
@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json(silent=True) or {}
    text = data.get("text")

    if not text:
        return jsonify({"error": "text is required"}), 400

    note = {
        "id": len(notes) + 1,
        "text": text
    }

    notes.append(note)
    return jsonify(note), 201


# READ ALL
@app.route("/notes", methods=["GET"])
def get_notes():
    return jsonify(notes)


# READ ONE
@app.route("/notes/<int:id>", methods=["GET"])
def get_note(id):
    for note in notes:
        if note["id"] == id:
            return jsonify(note)

    return jsonify({"error": "note not found"}), 404


# UPDATE
@app.route("/notes/<int:id>", methods=["PUT"])
def update_note(id):
    data = request.get_json(silent=True) or {}
    text = data.get("text")

    if not text:
        return jsonify({"error": "text is required"}), 400

    for note in notes:
        if note["id"] == id:
            note["text"] = text
            return jsonify(note)

    return jsonify({"error": "note not found"}), 404


# DELETE
@app.route("/notes/<int:id>", methods=["DELETE"])
def delete_note(id):
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            return jsonify({"message": "note deleted"})

    return jsonify({"error": "note not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)