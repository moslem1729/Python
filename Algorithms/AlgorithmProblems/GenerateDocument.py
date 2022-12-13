def generate_document(characters, document):
    for item in document:
        if search_in_characters(characters, item):
            characters = remove_item_from_characters(characters, item)
        else:
            return False

    return True


def search_in_characters(characters, character):
    for item in characters:
        if item == character:
            return True

    return False


def remove_item_from_characters(characters, character):
    flag = 0
    new_characters = ""
    for item in characters:
        if item == character and flag == 0:
            flag = flag + 1
        else:
            new_characters = new_characters + item
    return new_characters


def generate_document_using_hashmap(characters,document):
    character_counts={}
    for item in characters:
        if item not in character_counts:
            character_counts[item]=1
        else:
            character_counts[item]+=1

    for item in document:
        if item not in character_counts or character_counts[item]==0:
            return False
        else:
            character_counts[item]-=1
    return True


characters="a    moslemghbc"
document="caghmosmel     b"
print(generate_document_using_hashmap(characters,document))
print(generate_document(characters,document))