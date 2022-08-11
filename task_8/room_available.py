class RoomAvailable:
    def __init__(self):
        self.time_slot_list = []

    def isRoomAvailable(self, timeslot=0, duration=1):
        if not isinstance(timeslot, int) or not isinstance(duration, int):
            return False
        if timeslot == 0 or timeslot + duration > 17:
            return False
        order_list = [slot for slot in range(timeslot, timeslot + duration)]
        if any(slot in order_list for slot in self.time_slot_list):
            return False
        for slot in order_list:
            self.time_slot_list.append(slot)
        return True

