import reflex as rx


class ButtonState(rx.State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1


def index():
    return rx.vstack(
        rx.hstack(
            rx.button(
                "Decrementar",
                bg="#fef2f2",
                color="#b91c1c",
                border_radius="lg",
                on_click=ButtonState.decrement
            ),
            rx.heading(
                ButtonState.count,
                font_size="2em",
                padding_x="0.5em"
            ),
            rx.button(
                "Incrementar",
                bg="#ecfdf5",
                color="#047857",
                border_radius="lg",
                on_click=ButtonState.increment
            )
        )
    )


app = rx.App()
app.add_page(index)
app.compile()
