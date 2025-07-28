from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        split_nodes = []
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Text must have an odd number of parts for delimiter splitting")
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                result.append(TextNode(parts[i], TextType.TEXT))
            else:
                result.append(TextNode(parts[i], text_type))
        result.extend(split_nodes)
    print(result)
    return result

node = TextNode("This is text with a `code block` word", TextType.TEXT)

split_nodes_delimiter([node], "`", TextType.CODE)