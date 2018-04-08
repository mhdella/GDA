import json
import pygal
""" intro """
json_file = open('/Users/MEHRA/Documents/Notebooks/Takeout/Location History/Location History.json')
gdic_zero = json.load(json_file)
json_file.close()
gdic_one = gdic_zero['locations']
coords = []
i = 0
for rec in gdic_one:
    if i < 10:
        loc = (rec['longitudeE7'],rec['latitudeE7'])
        coords.append(loc)
    i += 1
print(coords)
xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Correlation'
xy_chart.add('A', coords)
xy_chart.render()
#print(len(coords))
