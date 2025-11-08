import reflex as rx
from python_reflex import style
from python_reflex.state import State


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right"
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left"
        ),
        margin_y="1em"
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def chat_init() -> rx.Component:
    qa_pairs = [
        (
            "¿Qué es Reflex?",
            "Una forma de construir aplicaciones web en Python!",
        ),
        (
            "¿Qué puedo hacer con él?",
            "Cualquier cosa desde un simple sitio web a una compleja aplicación web!",
        ),
    ]
    return rx.box(
        *[
            qa(question, answer) for question, answer in qa_pairs
        ]
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(placeholder="Escribe tu pregunta", on_blur=State.set_question, style=style.input_style),
        rx.button("Preguntar", on_click=State.answer, style=style.button_style),
    )


def index() -> rx.Component:
    return rx.container(
        chat(),
        action_bar(),
        rx.box(element="iframe", src="https://www.youtube.com/embed/2u7JlBEavx0?si=o3G4Ljs_eOwkf4f1", width="100%", padding=30)
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
