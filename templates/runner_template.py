from manim import *
class MyGeneratedScene(Scene):
    def construct(self):
        # 👇 USER_CODE goes here
        text1 = Text("Welcome to Manim!", font_size=72)
        text2 = Text("Let's animate this text", font_size=48).next_to(text1, DOWN)

        self.play(Write(text1))
        self.wait(1)

        self.play(FadeIn(text2))
        self.wait(1)

        self.play(FadeOut(text1), FadeOut(text2))