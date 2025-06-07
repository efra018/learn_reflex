import reflex as rx


class State(rx.State):

    # variable contador
    count: int = 0

    # funcion incrementar
    def increment(self):
        self.count += 1

    # funcion decrement
    def decrement(self):
        self.count -= 1


# page index
def index() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.button(
                "Decrement",
                color_scheme="ruby",
                on_click=State.decrement,
            ),
        ),
        rx.heading(State.count, font_size="2em"),
        rx.button(
            "Increment",
            color_scheme="grass",
            on_click=State.increment,
        ),
        my_button(),
        my_page(),
        my_div(),
        half_filled_progress(),
        rx.box(
            rx.vstack(
                round_button(),
            )
        ),
        spacing="4",
    )


### BASICS ###


def my_button():
    return rx.button("Click me")


# Anidar componentes rx.box
def my_page():
    return rx.box(rx.text("This is a page"), my_button())


# Usando base HTML
def my_div():
    return rx.el.div(rx.el.p("Use base HTML"))


# Personalizacion y diseño de componentes
def half_filled_progress():
    return rx.progress(value=50)


# Button CSS
def round_button():
    return rx.button(
        "Click me",
        border_radius="15px",
        font_size="18px",
    )


app = rx.App()
app.add_page(index)
