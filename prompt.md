# Slide generation prompt template

## Topic
Create a presentation about ... **edit this section**

## Format
- Use Marp syntax, a specialized Markdown format for presentations.
- A Marp presentation includes front matter (special variables) and triple dash (---) to separate slides.

## Structure
- Include a front matter block:
- Set Marp to true.
- Enable pagination.
- Choose a theme (default theme used here).
- Add a header (title of the presentation) and a footer (company name).

## Design Guidelines
Use images as much as possible, leveraging placeholders from https://placehold.co/.
- An image background with ![bg](https://placehold.co/600x400)
- A side image with ![bg left](https://placehold.co/300x400) or ![bg right](https://placehold.co/300x400)


## Marp Syntax Cheatsheet:


```markdown
---
marp: true
paginate: true
theme: default
header: Presentation title
footer: Name of the company
---

# Presentation title
Presented by **Name of presentee**

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
## Example 2 Subtitle

Short text

![bg](https://placehold.co/600x400)

---

# Example 4
## Example 4 Subtitle

Short text
![bg left](https://placehold.co/300x400)


```


