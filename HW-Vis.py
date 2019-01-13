# Import statements
import unittest
import sqlite3
import twitter_info # still need this in the same directory, filled out
import matplotlib.pyplot as plt

## [PART 1]
# Finish writing the function getDayDict which takes a database cursor and returns a
# dictionary that has the days of the weeks as the keys (using "Sun", "Mon", "Tue",
# "Wed", "Thu", "Fri", "Sat") and the number of tweets on the named day as the values
#
# cur - the database cursor
def getDayDict(cur):
    cur.execute('SELECT * FROM Tweets')
    rows = cur.fetchall()
    days_of_week = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    lst = []
    d = {}
    for row in rows:
        lst.append(row[2][:3])
    for date in lst:
        if date not in d.keys():
            d[date] = 1
        else:
            d[date] += 1
    for day in days_of_week:
        if day not in d.keys():
            d[day] = 0
    return d
## [Part 2]
# Finish writing the function drawBarChart which takes the dictionary and draws a bar
# chart with the days of the week on the x axis and the number of tweets on the named day on
# the y axis.  The chart must have an x label, y label, and title.  Save the chart to
# "bar.png" and submit it on canvas.
#
# dayDict - a dictionary with the days of the week and the number of tweets per day
def drawBarChart(dayDict):
    x = []
    y = []
    for tup in dayDict.items():
        x.append(tup[0])
        y.append(tup[1])
    plt.bar(x,y)
    plt.xlabel('Day')
    plt.ylabel('Nmber of Tweets')
    plt.title('Twitter Tweets by day')
    plt.show()
## [Part 3]
## Create unittests to test the function
# Finish writing the unittests.  Write the setUp function which will create the database connection
# to 'tweets.sqlite' and the cursor.  Write the tearDown function which closes the database connection.
# Write the test_getDayDict function to test getDayDict by comparing the returned dictionary to the
# expected value.  Also call drawBarChart in test_getDayDict.
class TestHW10(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect('/Users/Georg/Downloads/tweets.sqlite')
        self.cur = self.conn.cursor()

    def test_getDayDict(self):
        self.values = getDayDict(self.cur)
        drawBarChart(self.values)
        self.assertEqual(len(self.values.keys()), 7)

    def tearDown(self):
        self.cur.close()



# run the main method
if __name__ == "__main__":
    unittest.main(verbosity=2)
