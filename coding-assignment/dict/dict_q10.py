#colors
color_dict = {}

name = input("Enter your name: ").strip()

colors = []

while True:
    color = input(f"Hello, {name}! What's your favorite color? (Enter 'done' to finish) ").strip()
    
    # If the user enters 'done', stop asking for colors
    if color.lower() == 'done':
        break
    colors.append(color)

color_dict[name] = colors

print(f"\n{name}'s favorite colors are: {', '.join(color_dict[name])}.")

