scores = [
    {'english' : 80, 'math' : 100},
    {'english' : 100, 'math' : 50},
    {'english' : 70, 'math' : 100},
    {'english' : 80, 'math' : 90}
]

scores.sort(key=lambda x : (-x['english'], -x['math']))

print(scores)