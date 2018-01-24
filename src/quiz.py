import rosegraphics as rg


def main():
    mystery_draw(3, 5, rg.RoseWindow(400, 400))



def mystery_draw(m, n, window):
    x = 10
    y = 20
    for k in range(m):
        for i in range(n):
            upper_left = rg.Point(x, y)
            lower_right = rg.Point(x + 20, y + 20)
            rect = rg.Rectangle(upper_left, lower_right)
            rect.attach_to(window)
            window.render()
            x = x + 20
        x = 10
        y = 20
    window.close_on_mouse_click()
main()