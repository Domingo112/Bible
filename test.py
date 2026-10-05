import flet as ft
import json
import random
import asyncio


def main(page: ft.Page):
    page.views.append(
            ft.View(
                route="/"
            )
        )
    async def auto_redirect():
        content.opacity=1
        content.update()
        await asyncio.sleep(5)
        content.opacity=0
        content.update()
        await asyncio.sleep(0.8)
        page.navigate("/home")
    page.title = "Bible App"

    # Remove fixed padding and spacing
    page.padding = 0
    page.spacing = 0
    page.window.width = 300

    page.theme_mode = ft.ThemeMode.DARK
    

    # =====================================================
    # GET STARTED BUTTON
    # =====================================================

    button = ft.Button(
         "GET STARTED",
         color="white",
         bgcolor="#1a2421",
         on_click=lambda e: page.navigate("/home"),
         width=180,
         height=50,
         style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=30),
             elevation=5,
         ),
     )

    # =====================================================
    # QUOTE
    # =====================================================

    quoteoutput = ft.Text(
        "GOD'S WORD LIVES IN US",
        color="white",
        weight=ft.FontWeight.W_500,
        text_align=ft.TextAlign.CENTER,
        size=14,
        max_lines=3,
        opacity=0.9,
    )

    # =====================================================
    # RANDOM QUOTE
    # =====================================================

    def quote():
        try:
            with open("quote.json", "r", encoding="utf-8") as f:
                quoteing = json.load(f)

            randtxt = random.choice(list(quoteing.values()))

            quoteoutput.value = randtxt

        except Exception:
            quoteoutput.value = "GOD'S WORD LIVES IN US"

    # =====================================================
    # FULL SCREEN BACKGROUND
    # =====================================================

    background = ft.Container(
        expand=True,

        image=ft.DecorationImage(
            src="main.png",
            fit=ft.BoxFit.COVER,
        ),
    )

    # =====================================================
    # DARK OVERLAY
    # =====================================================

    overlay = ft.Container(
        expand=True,

        gradient=ft.LinearGradient(
            begin=ft.Alignment.TOP_CENTER,
            end=ft.Alignment.BOTTOM_CENTER,

            colors=[
                ft.Colors.with_opacity(0.15, "black"),
                ft.Colors.with_opacity(0.80, "black"),
            ],
        ),
    )

    # =====================================================
    # CONTENT
    # =====================================================

    content = ft.Container(
        expand=True,

        padding=ft.Padding.symmetric(
            horizontal=20,
            vertical=25,
        ),

        content=ft.Column(
            expand=True,

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[

                # =================================================
                # TOP SECTION
                # =================================================

                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    spacing=5,

                    controls=[
                        #cross icon
                        ft.Icon(ft.icons.Icons.ADD, color="white", size=60),

                        # HOLY BIBLE
                        ft.Text(
                            "HOLY BIBLE",
                            color="white",
                            size=38,
                            weight=ft.FontWeight.BOLD,
                            text_align=ft.TextAlign.CENTER,
                        ),

                        # QUOTE
                        ft.Container(
                            content=quoteoutput,

                            width=280,

                            alignment=ft.Alignment.CENTER,

                            margin=ft.Margin.only(
                                top=8
                            ),
                        ),
                    ],
                ),

                # =================================================
                # FLEXIBLE EMPTY SPACE
                # =================================================

                ft.Container(
                    expand=True,
                ),

                # =================================================
                # GET STARTED
                # =================================================

                ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,

                    controls=[

                         button,

                        ft.Container(
                            height=15,
                        ),
                    ],
                ),
            ],
        ),
    )

    # =====================================================
    # STACK EVERYTHING
    # =====================================================

    page.add(
        ft.Stack(
            expand=True,

            controls=[

                # Background fills entire screen
                background,

                # Dark overlay fills entire screen
                overlay,

                # Text and button
                content,
            ],
        )
    )

    # Load quote
    quote()

    page.update()
    page.run_task(auto_redirect)


