[[Topic]]:

## Topic
Create a presentation about ...


[[Instructions]]:

## Format
Use Marp syntax, a specialized Markdown format for presentations.
A Marp presentation includes front matter (special variables), HTML comments (<!-- -->), and triple dash (---) to separate slides.

## Structure
Include a front matter block:
Set Marp to true.
Enable pagination.
Choose a theme (default theme used here).
Add a header (title of the presentation) and a footer (company name).

## Images
You can set:
An image background with ![bg](https://placehold.co/600x400)
A side image with ![bg left](https://placehold.co/300x400)

## Design Guidelines

Be creative and use color themes that are relevant to the topic>.
Use images as much as possible, leveraging placeholders from https://placehold.co/.
Make sure images are sized appropriately for each slide’s layout.


## Color themes

Use color schemes aligned with the topic.
Images: Incorporate relevant images using https://placehold.co/ and specify the image resolution for proper fitting.
Ensure your presentation is visually engaging and communicates the critical aspects of global warming.

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
Presented by **Name**

---

# Agenda

1. Topic 1
2. Topic 2
3. Topic 3
4. Topic 4

---

<!-- 
_backgroundImage: "linear-gradient(to bottom, #67b8e3, #0288d1)" 
_color: white
-->

# Topic 1
## Topic 1 Subtitle

Lorem Ipsum è un testo segnaposto utilizzato nel settore della tipografia e della stampa...

---

<!--
_backgroundColor: black
_color: white
-->

# Topic 2
## Topic 2 Subtitle

Brief introduction...

- Bullet point 1
- Bullet point 2
- Bullet point 3

---

# Topic 3

Slide with image background

![bg](https://placehold.co/600x400)

---

# Topic 4
## Topic 4 Subtitle

Lorem Ipsum è un testo segnaposto...

![bg left](https://placehold.co/300x400)
Additional Instructions:
```


