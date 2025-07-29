def markdown_to_blocks(markdown):
    lines = markdown.split('\n\n')
    processed_lines = []
    for line in lines:
        processed_lines.append(line.strip())
    return processed_lines

markdown_to_blocks(
'''# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item'''
)