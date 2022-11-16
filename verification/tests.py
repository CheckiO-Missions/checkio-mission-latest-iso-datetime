"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['2007-03-04T21:08:12', '2007-03-04T21:08:12'],
            "answer": '2007-03-04T21:08:12',
        },
        {
            "input": ['2027-09-01T01:03:10', '1997-04-15T11:18:14'],
            "answer": '2027-09-01T01:03:10',
        },
        {
            "input": ['0001-01-01T01:01:01', '3000-11-16T13:27:02'],
            "answer": '3000-11-16T13:27:02',
        },

    ],
    "Extra": [
        {
            "input": ['1993-04-23T23:51:16', '2000-02-16T23:17:54'],
            "answer": '2000-02-16T23:17:54',
        },
        {
            "input": ['1456-08-01T04:47:19', '1785-03-16T19:13:43'],
            "answer": '1785-03-16T19:13:43',
        },
    ]
}
