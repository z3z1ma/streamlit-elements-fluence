from streamlit_elements.core.frame import new_element


class Extras:
    def InnerHTML(self, html, **props):
        new_element("extrasInnerHTML", "InnerHTML")(html=html, **props)
