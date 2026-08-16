from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
app.route("/events", methods = ["GET"])
def get_events():
    event_list = []
    for event in events:
        event_list.append(event.to_dict())
    return jsonify(event_list)

app.route("/events/<int:id>", methods = ["GET"])
def get_oneEvent(event_id):
    for event in events:
        if event.id == event_id:
            return (event.to_dict())
    return "event not found",404

@app.route("/events", methods=["POST"])
def create_event():
   
    data = request.get_json()
    new_id = events[len(events)-1].id +1

    new_event = Event(new_id,data["title"])
    events.append(new_event)

    return jsonify(new_event.to_dict()),201




# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):

    data = request.get_json()

    for event in events:
        if event.id == event_id:
            event.title = data["title"]
            return jsonify(event.to_dict())
    return "Event not Found",404



@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    for event in events:
        if event.id == event_id:
            events.remove(event)
            return "",204
    return "Event not Found", 404

if __name__ == "__main__":
    app.run(debug=True)
