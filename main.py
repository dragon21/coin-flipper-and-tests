def on_button_pressed_a():
    basic.show_icon(IconNames.COW)
    basic.show_icon(IconNames.GIRAFFE)
    basic.show_icon(IconNames.DIAMOND)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    if Math.random_boolean():
        basic.show_icon(IconNames.SKULL)
    else:
        basic.show_icon(IconNames.SQUARE)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(2 + 3)
input.on_button_pressed(Button.B, on_button_pressed_b)
