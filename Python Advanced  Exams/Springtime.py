def start_spring(**kwargs):
    spring_objects = {}
    for obj_name, obj_type in kwargs.items():
        if obj_type not in spring_objects:
            spring_objects[obj_type] = []
        spring_objects[obj_type].append(obj_name)

    sorted_collections = sorted(spring_objects.items(), key=lambda x: (-len(x[1]), x[0]))
    return '\n'.join([f"{obj_type}:\n" + '\n'.join([f"-{name}" for name in sorted(obj_names)]) for obj_type, obj_names in sorted_collections])

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird",}
print(start_spring(**example_objects))
example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
