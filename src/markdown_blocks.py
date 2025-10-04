def markdown_to_blocks(markdown):
    split_text = markdown.split("\n\n")
    blocks = []
    for text in split_text:
        text = text.strip()
        if text == "":
            continue

        split_lines = text.split("\n")
        aux = []
        for p in split_lines:
            aux.append(p.strip())

        text = "\n".join(aux)
        blocks.append(text)
    return blocks