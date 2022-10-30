# Belajar Keyword Argument List

from cgitb import html, text
from tkinter.ttk import Style
from turtle import ht


def create_html(tag, text):
    html = f"</{tag}>{text}</{tag}>"
    return html


html = create_html("p", "Hello Python")
print(html)

html = create_html("a", "ini link")
print(html)


# <a href="> ini link</a>"
def create_html(tag, text, **atributes):
    html = f"</{tag}>{text}</{tag}>"
    print(atributes)
    return html


html = create_html("p", "Hello Python", style="paragraft")
print(html)

html = create_html("a", "ini link", href="www.google.com", style="link")
print(html)

# tag html


def create_html(tag, text, **atributes):
    html = f"<{tag}"

    for key, value in atributes.items():
        html = html + f" {key}='{value}'"

    html = html + f">{text}</{tag}>"
    return html


html = create_html("p", "Hello Python", style="paragraft")
print(html)

html = create_html("a", "ini link", href="www.google.com", style="link")
print(html)

html = create_html("div", "ini div", style="contoh")
print(html)
