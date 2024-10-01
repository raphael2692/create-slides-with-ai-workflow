prompt_template = """
## Topic
Create a presentation about {topic}.

### Additional content guidelines

Keep in mind that: {additional_guidelines}

## Format
- Use Marp syntax, a specialized Markdown format for presentations.
- A Marp presentation includes front matter (special variables) and triple dash (---) to separate slides.
- Never envelop answer between ```markdown quotes. It should always trat with front matter.

## Structure
- Include a front matter block:
- Set Marp to true.
- Enable pagination.
- If using a layout with a side image be extremely concise or text will overflow.

## Content Guidelines
1. **Topic Elaboration**: Provide a clear and concise description of the topic, including specific subtopics to cover.
2. **Dynamic Content**: Use a mix of text, bullet points, images, and custom styles to keep the slides engaging.
3. **Slide Transitions**: Ensure smooth flow between slides by logically connecting topics.
4. **Examples**: Include real-world or hypothetical examples to illustrate points.

## Design Guidelines
- Use visual aids to support the topic content, leveraging placeholders from https://placehold.co/.
- A side image with ![bg left](https://placehold.co/300x400) or ![bg right](https://placehold.co/300x400)

## Marp Syntax Cheatsheet:

```markdown
---
marp: true
paginate: true
theme: default
---

# Presentation title
Additional info if given (date, meeting presenter, etc)
---

# Agenda

1. Example 1
2. Example 2
3. Example 3
4. Example 4

---

# Example 1
## Example 1 Subtitle

Long text

---

# Example 2
## Example 2 Subtitle

Short text

- Bullet point 1
- Bullet point 2
- Bullet point 3

---

# Example 3
## Example 3 Subtitle

Very short text

![bg left](https://placehold.co/300x400)
"""