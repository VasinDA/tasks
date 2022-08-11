import unittest
from room_available import RoomAvailable

class TestRoomAvailable(unittest.TestCase):
    def test_suite_1(self):
        test_dict = {'test_1':{1:True}, 'test_2':{1:False}, 'test_3':{(2, 3):True}, 
        'test_4':{3:False}, 'test_5':{5:True}}
        test_room_available = RoomAvailable()
        for key in test_dict:
            for slot in test_dict[key]:
                if not isinstance(slot, tuple):
                    self.assertEqual(test_room_available.isRoomAvailable(slot), test_dict[key][slot])
                else:
                    timeslot, duration = slot
                    self.assertEqual(test_room_available.isRoomAvailable(timeslot, duration), test_dict[key][slot])
    
    def test_suite_2(self):
        test_dict = {'test_1':{16:True}, 'test_2':{15:True}, 'test_3':{(1, 16):False}, 
        'test_4':{(1, 14):True}}
        test_room_available = RoomAvailable()
        for key in test_dict:
            for slot in test_dict[key]:
                if not isinstance(slot, tuple):
                    self.assertEqual(test_room_available.isRoomAvailable(slot), test_dict[key][slot])
                else:
                    timeslot, duration = slot
                    self.assertEqual(test_room_available.isRoomAvailable(timeslot, duration), test_dict[key][slot])

    def test_suite_3(self):
        test_dict = {'test_1':{(3, 2):True}, 'test_2':{(8, 3):True}, 'test_3':{4:False}, 
        'test_4':{(7, 2):False}}
        test_room_available = RoomAvailable()
        for key in test_dict:
            for slot in test_dict[key]:
                if not isinstance(slot, tuple):
                    self.assertEqual(test_room_available.isRoomAvailable(slot), test_dict[key][slot])
                else:
                    timeslot, duration = slot
                    self.assertEqual(test_room_available.isRoomAvailable(timeslot, duration), test_dict[key][slot])
    
    def test_wrong_data(self):
        test_dict = {'test_1':{('3', '3'):False}, 'test_2':{(0, 16):False}, 'test_3':{(2, 16):False}}
        test_room_available = RoomAvailable()
        for key in test_dict:
            for slot in test_dict[key]:
                timeslot, duration = slot
                self.assertEqual(test_room_available.isRoomAvailable(timeslot, duration), test_dict[key][slot])


            
            
unittest.main()