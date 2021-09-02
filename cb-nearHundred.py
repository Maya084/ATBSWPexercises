def front_back(str):
    a = str[0]
    b = str[-1]
    sredendel=str[1:-1]
    return b+sredendel+a

print(front_back("Marija"))