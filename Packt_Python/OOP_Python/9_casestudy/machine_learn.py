import csv
from random import randint
from collections import Counter

dataset_filename = "OOP_Python\9_casestudy\colors.csv"
output_filename = "OOP_Python\9_casestudy\output.csv"

def hex_to_rgb(hex_color):
    return tuple(int(hex_color[i : i + 2], 16) for i in range(1, 6, 2))

def load_colors(filename):
    with open(filename) as dataset_file:
        lines = csv.reader(dataset_file)    #csv.reader iterates over each line in the file
        for line in lines:
            label, hex_color = line
            yield (hex_to_rgb(hex_color), label)

def generate_colors(count=100):
    for i in range(count):
        yield (randint(0, 255), randint(0, 255), randint(0, 255))   #a generator uses fewer lines than a for loop in this case, "yield" acts as the initial empty list, the assignment of color tuples to that list and the return of the list

def color_distance(color1, color2):
    channels = zip(color1, color2)
    sum_distance_squared = 0
    for c1, c2 in channels:
        sum_distance_squared += (c1 - c2) ** 2      #based on pythagorean theorem (no sqrt because these are relative distances & sqrt is an expensive func)
    return sum_distance_squared

def nearest_neighbors(model_colors, target_colors, num_neighbors=5):
    model_colors = list(model_colors)
    for target in target_colors:
        distances = sorted(
            ((color_distance(c[0], target), c) for c in model_colors)
        )
        yield target, [d[1] for d in distances[:num_neighbors]]

def name_colors(model_colors, target_colors, num_neighbors=5):
    for target, near in nearest_neighbors(
        model_colors, target_colors, num_neighbors=5
    ):
        name_guess = Counter(n[1] for n in near).most_common()[0][0]
        yield target, name_guess

def write_results(colors, filename=output_filename):
    with open(filename, "w") as file:
        writer = csv.writer(file)
        for (r, g, b), name in colors:
            writer.writerow([name, f"#{r:02x}{g:02x}{b:02x}"])

def process_colors(dataset_filename=dataset_filename):
    model_colors = load_colors(dataset_filename)
    colors = name_colors(model_colors, generate_colors(), 5)
    write_results(colors)

if __name__ == "__main__":
    process_colors()