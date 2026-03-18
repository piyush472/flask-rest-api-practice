'''from flask import Flask,request,jsonify
app=Flask(__name__)
notes=[]
@app.route("/create_note",methods=["POST"])

def create():
    
    text=request.args.get("text")
    note={
        "id":len(notes)+1,
        "text":text
    }
    notes.append(note)
    return jsonify(notes)

@app.route("/read_notes")
def read_notes():
    return notes

@app.route("/del_note/<int:id>",methods=["DELETE"])
def delete_note(id):
    for note in notes:
        if note["id"] == id:
            notes.remove(note)
            return jsonify({"message": "note deleted"})

    return jsonify({"message": "note not found"})'''