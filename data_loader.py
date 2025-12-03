import json

class Scene:
    def __init__(self, name, description, actions):
        self.name = name
        self.description = description
        self.actions = actions


class Action:
    def __init__(self, command, next_scene):
        self.command = command
        self.next_scene = next_scene


def load_adventure(filename):
    with open(filename) as f:
        data = json.load(f)
        first_scene = data["start_scene"]
        scene_objects = {}
        for scene_data in data["scenes"]:
            actions = [Action(action_data["action_command"], action_data["next_scene"]) for action_data in scene_data["actions"]]
            scene_objects[scene_data["scene_name"]] = Scene(scene_data["scene_name"], scene_data["scene_description"], actions)

        return first_scene, scene_objects


if __name__ == "__main__":
    first_scene, scene_objects = load_adventure("adventure.json")
    pass