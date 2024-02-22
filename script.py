# paintings
paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]
dates = [1939, 1933, 1946, 1940]

# zipping together paintings and dates
paintings = list(zip(paintings, dates))

# adding more paintings to list
paintings.append(("The Broken Column", 1944))
paintings.append(("The Wounded Deer", 1946))
paintings.append(("Me and My Doll", 1937))

len_of_paintings = len(paintings)

audio_tour_number = list(range(1, len(paintings) + 1))

master_list = list(zip(audio_tour_number, paintings))

print(master_list)
