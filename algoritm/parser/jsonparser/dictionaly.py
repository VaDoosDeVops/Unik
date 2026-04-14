ru_en_dict = {}

with open("algoritm/parser/jsonparser/en-ru.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        
        if not line:
            continue
        
        eng, rus = line.split(" - ")
        rus_words = rus.split(", ")
        
        for word in rus_words:
            if word not in ru_en_dict:
                ru_en_dict[word] = []
            
            ru_en_dict[word].append(eng)

sorted_words = sorted(ru_en_dict.keys())
with open("algoritm/parser/jsonparser/ru-en.txt", "w", encoding="utf-8") as file:
    for word in sorted_words:
        translations = ", ".join(ru_en_dict[word])
        file.write(f"{word} - {translations}\n")