class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.props == None:
            return ""
        htmlnode = ""
        for i in self.props:
            htmlnode += f' {i}="{self.props[i]}"'
        return htmlnode

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("value field is empty")
        if self.tag is None:
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag field is empty")
        if self.children is None:
            raise ValueError("children field is empty")
        res = f'<{self.tag}{self.props_to_html()}>'
        for child in self.children:
            res += child.to_html()
        res += f'</{self.tag}>'
        return res

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.children}, {self.props})"