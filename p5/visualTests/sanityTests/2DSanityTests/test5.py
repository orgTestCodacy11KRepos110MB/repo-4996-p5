from p5 import *
import os

font = None

dirname = os.path.dirname(os.path.realpath(__file__))


def preload():
    global font
    # TODO: Use bunch of different fonts formats like otf,rtf etc
    font_path = f"{dirname}/TestAssets/TestFont.ttf"
    font = load_font(font_path)


def setup():
    size(640, 360)


def draw():
    global font
    text_font(font)
    background(255)
    test_text = """
    processing
    
is
fun     
"""
    text(test_text, mouse_x, mouse_y)
    text_align(CENTER, TOP)
    stroke(0)
    text_size(20)
    fill(220, 180, 200)
    stroke_weight(1)
    text("Processing is Fun", mouse_x + 50, mouse_y + 50)
    no_fill()
    text_align(TOP, BOTTOM)
    text("Processing is Fun", mouse_x + 100, mouse_y + 100)
    no_stroke()
    fill(47, 213, 28)
    text_align(LEFT, CENTER)
    text("Processing is Fun", mouse_x + 150, mouse_y + 150)
    stroke(47, 213, 28)
    text("Processing is Fun", mouse_x + 200, mouse_y + 200)
    text_size(40)
    stroke_weight(5)
    text("Processing is Fun", mouse_x + 300, mouse_y + 300)

    print(text_width("Processing is Fun"))
