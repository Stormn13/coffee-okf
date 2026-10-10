import frontmatter

with open('knowledge_base/menu.md', 'r', encoding='utf-8') as f:
    post = frontmatter.load(f)

metadata = post.metadata
print((metadata['tags']))