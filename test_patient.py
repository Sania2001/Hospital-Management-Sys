import unittest
import sqlite3

class Patients(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect("Hospital.db")
        self.id = "1"
        self.name="Sania Shinde"

    def tearDown(self):
        self.id = "0"
        self.connection.close()

    def test_pt1(self):
        result = (self.connection.execute("SELECT name FROM Patient_table WHERE Patient_id = "+ self.id))
        for i in result:
            fetchname= i[0]
        self.assertEqual(fetchname,self.name)



if __name__ == "__main__":
    unittest.main()