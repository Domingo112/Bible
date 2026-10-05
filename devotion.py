import flet as ft
import json

def devotional_page(page: ft.Page):
    page.views.append(
        ft.View(
            route="/devotion"
        )
    )
    page.bgcolor = "#F7F5FA"
    page.window.width = 300
    purple = "#7652C8"
    dark = "#29243A"
    gray = "#898494"

    devotional_list = ft.Column(
        spacing=12,
        scroll=ft.ScrollMode.AUTO
    )

    # Load devotional JSON
    def devotional(e):
        with open("devotional.json", "r", encoding="utf-8") as file:
            devotionals = json.load(file)

        search_list = search.value.lower()
        devotional_list.controls.clear()

        for dev in devotionals["devotionals"]:
            book = dev["theme"]
            day = dev["day"]
            ref = dev["scripture"]["reference"]

            if search_list in book.lower():
                devotional_list.controls.append(
                    create_card(day, book, ref)
                )

        devotional_list.update()

    search = ft.TextField(
        hint_text="Search devotionals...",
        hint_style=ft.TextStyle(
            color="#A39DAF",
            size=13
        ),
        border="none",
        bgcolor="white",
        prefix_icon=ft.Icons.SEARCH,
        height=48,
        content_padding=ft.Padding.symmetric(
            horizontal=15,
            vertical=8
        ),
        border_radius=15,
        on_change=devotional,
    )

    category_row = ft.Row(
        scroll=ft.ScrollMode.AUTO,
        spacing=8
    )

    def create_card(day, theme, scripture1):

        def readmore(e,days=day):
            page.session.store.set("day", days)
            page.navigate("/seemore")

        # put bookmark fuction here for users to save book marked devotionals
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(
                                    day,
                                    color=purple,
                                    size=11,
                                    weight=ft.FontWeight.BOLD
                                ),
                                bgcolor="#F0E9FF",
                                padding=ft.Padding.symmetric(
                                    horizontal=12,
                                    vertical=7
                                ),
                                border_radius=20
                            ),

                            ft.Container(
                                content=ft.Icon(
                                    ft.Icons.BOOKMARK_BORDER,
                                    color=gray,
                                    size=21
                                ),
                                padding=5,
                                border_radius=20,
                                bgcolor="#F7F5FA"
                            )
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),

                    ft.Text(
                        theme,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=dark,
                        max_lines=2,
                        overflow=ft.TextOverflow.ELLIPSIS
                    ),

                    ft.Row(
                        [
                            ft.Icon(
                                ft.Icons.AUTO_STORIES_OUTLINED,
                                color=purple,
                                size=15
                            ),
                            ft.Text(
                                scripture1,
                                size=12,
                                color=purple,
                                weight=ft.FontWeight.W_500
                            )
                        ],
                        spacing=6
                    ),

                    ft.Container(
                        height=1,
                        bgcolor="#EEEAF4",
                        margin=ft.Margin.symmetric(vertical=2)
                    ),

                    ft.Row(
                        [
                            ft.Button(
                                on_click=readmore,
                                content=ft.Row(
                                    [   
                                        ft.Text(
                                            "Read More",
                                            size=12,
                                            weight=ft.FontWeight.BOLD
                                        ),
                                        ft.Icon(
                                            ft.Icons.ARROW_FORWARD,
                                            size=15
                                        )
                                    ],
                                    spacing=5,
                                    tight=True
                                ),
                                style=ft.ButtonStyle(
                                    bgcolor=purple,
                                    color="white",
                                    padding=ft.Padding.symmetric(
                                        horizontal=14,
                                        vertical=9
                                    ),
                                    shape=ft.RoundedRectangleBorder(
                                        radius=10
                                    )
                                )
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END
                    )
                ],
                spacing=12
            ),
            bgcolor="white",
            padding=18,
            border_radius=20,
            shadow=ft.BoxShadow(
                blur_radius=12,
                spread_radius=0,
                color="#15000000",
                offset=ft.Offset(0, 4)
            )
        )

    page.controls.clear()

    page.add(
        ft.Column(
            [
                # HEADER
                ft.Row(
                    [
                        ft.Container(
                            content=ft.IconButton(
                                ft.Icons.ARROW_BACK,
                                icon_color=purple,
                                icon_size=21,
                                on_click=lambda e: page.navigate("/home")
                            ),
                            bgcolor="white",
                            border_radius=13,
                            padding=2
                        ),

                        ft.Column(
                            [
                                ft.Text(
                                    "Devotional Library",
                                    size=21,
                                    color=dark,
                                    weight=ft.FontWeight.BOLD
                                ),
                                ft.Text(
                                    "Daily inspiration",
                                    size=11,
                                    color=gray
                                )
                            ],
                            spacing=2
                        )
                    ],
                    alignment=ft.MainAxisAlignment.START,
                    spacing=10
                ),

                # INTRODUCTION
                ft.Container(
                    content=ft.Row(
                        [
                            ft.Container(
                                content=ft.Icon(
                                    ft.Icons.AUTO_STORIES,
                                    color=purple,
                                    size=22
                                ),
                                width=42,
                                height=42,
                                bgcolor="#F0E9FF",
                                border_radius=12,
                                alignment=ft.Alignment(0, 0)
                            ),

                            ft.Column(
                                [
                                    ft.Text(
                                        "Grow spiritually",
                                        size=15,
                                        weight=ft.FontWeight.BOLD,
                                        color=dark
                                    ),
                                    ft.Text(
                                        "Grow spiritually every day",
                                        size=11,
                                        color=gray
                                    )
                                ],
                                spacing=3,
                                expand=True
                            )
                        ],
                        spacing=10
                    ),
                    bgcolor="#FFFFFF",
                    padding=12,
                    border_radius=16
                ),

                # SEARCH
                ft.Container(
                    content=search,
                    shadow=ft.BoxShadow(
                        blur_radius=8,
                        color="#12000000",
                        offset=ft.Offset(0, 2)
                    ),
                    border_radius=15
                ),

                # SECTION TITLE
                ft.Row(
                    [
                        ft.Text(
                            "Daily Devotion",
                            size=19,
                            color=dark,
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Container(
                            content=ft.Text(
                                "Today",
                                size=10,
                                color=purple,
                                weight=ft.FontWeight.BOLD
                            ),
                            bgcolor="#F0E9FF",
                            padding=ft.Padding.symmetric(
                                horizontal=10,
                                vertical=6
                            ),
                            border_radius=15
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                ),

                category_row,

                ft.Text(
                    size=14,
                    color=gray
                ),

                devotional_list
            ],
            spacing=15,
            expand=True,
            scroll=ft.ScrollMode.AUTO
        )
    )

    devotional(search)

