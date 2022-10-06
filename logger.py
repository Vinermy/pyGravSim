import json


class LogEntry(object):
    def __init__(self, frame_size: tuple[int, int], body_count: int, initial_pos: list, initial_vel: list) -> None:
        self.log = {
            "frame_size": frame_size,
            "frame_count": 0,
            "body_count": body_count,
            "positions": {
                "0": initial_pos
            },
            "velocities": {
                "0": initial_vel
            }
        }

    def addframe(self, positions: list, velocities: list) -> None:
        self.log["frame_count"] += 1  # Update frame counter
        self.log["positions"][str(self.log["frame_count"])] = positions
        self.log["velocities"][str(self.log["frame_count"])] = velocities

    def dump(self) -> None:
        with open('log.json', 'w') as f:
            json.dump(self.log, f, indent=True)
