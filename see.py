
import flet as ft
import json


def devotional_page(page: ft.Page):

    page.bgcolor = "#F7F5FA"
    page.window.width = 300
    page.window.height = 650

    purple = "#7652C8"
    dark = "#29243A"
    gray = "#898494"

    devotional_list = ft.Column(
        spacing=12,
        scroll=ft.ScrollMode.AUTO,
        expand=True
    )

    # ==================================================
    # DEVOTIONAL DETAILS PAGE
    # ==================================================

    def devotional_details(
        day,
        theme,
        scripture_reference,
        scripture_text,
        reading_time,
        category,
        introduction,
        reflection,
        prayer,
        key_lesson,
        author
    ):

        page.controls.clear()

        page.add(
            ft.Column(
                [
                    # ==================================
                    # HEADER
                    # ==================================

                    ft.Container(
                        content=ft.Row(
                            [
                                ft.IconButton(
                                    icon=ft.Icons.ARROW_BACK,
                                    icon_color=purple,
                                    on_click=lambda e: page.go(
                                        "/devotional"
                                    )
                                ),

                                ft.Text(
                                    "Devotional",
                                    size=21,
                                    color=dark,
                                    weight=ft.FontWeight.BOLD,
                                    expand=True
                                )
                            ],
                            spacing=5
                        ),

                        padding=ft.Padding(
                            left=10,
                            right=10,
                            top=10,
                            bottom=5
                        )
                    ),

                    # ==================================
                    # CONTENT
                    # ==================================

                    ft.Container(
                        content=ft.Column(
                            [
                                # DAY
                                ft.Container(
                                    content=ft.Text(
                                        day,
                                        size=11,
                                        color=purple,
                                        weight=ft.FontWeight.BOLD
                                    ),

                                    bgcolor="#F0E9FF",

                                    padding=ft.Padding(
                                        left=12,
                                        right=12,
                                        top=7,
                                        bottom=7
                                    ),

                                    border_radius=20
                                ),

                                # ==================================
                                # THEME
                                # ==================================

                                ft.Text(
                                    theme,
                                    size=24,
                                    color=dark,
                                    weight=ft.FontWeight.BOLD,
                                    width=270
                                ),

                                # ==================================
                                # CATEGORY
                                # ==================================

                                ft.Text(
                                    category,
                                    size=12,
                                    color=purple,
                                    weight=ft.FontWeight.BOLD,
                                    width=270
                                ),

                                # ==================================
                                # INFORMATION
                                # ==================================

                                ft.Row(
                                    [
                                        ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.Text(
                                                        "Reading Time",
                                                        size=9,
                                                        color=gray
                                                    ),

                                                    ft.Text(
                                                        str(reading_time),
                                                        size=11,
                                                        color=dark,
                                                        weight=ft.FontWeight.BOLD,
                                                        max_lines=2,
                                                        overflow=ft.TextOverflow.ELLIPSIS
                                                    )
                                                ],

                                                spacing=3,

                                                tight=True
                                            ),

                                            bgcolor="white",

                                            padding=ft.Padding(
                                                left=12,
                                                right=12,
                                                top=10,
                                                bottom=10
                                            ),

                                            border_radius=12,

                                            expand=True
                                        ),

                                        ft.Container(
                                            content=ft.Column(
                                                [
                                                    ft.Text(
                                                        "Author",
                                                        size=9,
                                                        color=gray
                                                    ),

                                                    ft.Text(
                                                        str(author),
                                                        size=11,
                                                        color=dark,
                                                        weight=ft.FontWeight.BOLD,
                                                        max_lines=2,
                                                        overflow=ft.TextOverflow.ELLIPSIS
                                                    )
                                                ],

                                                spacing=3,

                                                tight=True
                                            ),

                                            bgcolor="white",

                                            padding=ft.Padding(
                                                left=12,
                                                right=12,
                                                top=10,
                                                bottom=10
                                            ),

                                            border_radius=12,

                                            expand=True
                                        )
                                    ],

                                    spacing=8,

                                    vertical_alignment=ft.CrossAxisAlignment.START
                                ),

                                # ==================================
                                # SCRIPTURE
                                # ==================================

                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                scripture_reference,
                                                size=14,
                                                color=purple,
                                                weight=ft.FontWeight.BOLD,
                                                width=240
                                            ),

                                            ft.Text(
                                                scripture_text,
                                                size=13,
                                                color=dark,
                                                italic=True,
                                                width=240
                                            )
                                        ],

                                        spacing=10
                                    ),

                                    bgcolor="#F0E9FF",

                                    padding=ft.Padding(
                                        left=15,
                                        right=15,
                                        top=15,
                                        bottom=15
                                    ),

                                    border_radius=18
                                ),

                                # ==================================
                                # INTRODUCTION
                                # ==================================

                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                "Introduction",
                                                size=17,
                                                color=dark,
                                                weight=ft.FontWeight.BOLD
                                            ),

                                            ft.Text(
                                                introduction,
                                                size=12,
                                                color=gray,
                                                width=240
                                            )
                                        ],

                                        spacing=8
                                    ),

                                    bgcolor="white",

                                    padding=ft.Padding(
                                        left=15,
                                        right=15,
                                        top=15,
                                        bottom=15
                                    ),

                                    border_radius=18
                                ),

                                # ==================================
                                # REFLECTION
                                # ==================================

                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                "Reflection",
                                                size=17,
                                                color=dark,
                                                weight=ft.FontWeight.BOLD
                                            ),

                                            ft.Text(
                                                reflection,
                                                size=12,
                                                color=gray,
                                                width=240
                                            )
                                        ],

                                        spacing=8
                                    ),

                                    bgcolor="white",

                                    padding=ft.Padding(
                                        left=15,
                                        right=15,
                                        top=15,
                                        bottom=15
                                    ),

                                    border_radius=18
                                ),

                                # ==================================
                                # KEY LESSON
                                # ==================================

                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                "Key Lesson",
                                                size=17,
                                                color=dark,
                                                weight=ft.FontWeight.BOLD
                                            ),

                                            ft.Text(
                                                key_lesson,
                                                size=12,
                                                color=gray,
                                                width=240
                                            )
                                        ],

                                        spacing=8
                                    ),

                                    bgcolor="white",

                                    padding=ft.Padding(
                                        left=15,
                                        right=15,
                                        top=15,
                                        bottom=15
                                    ),

                                    border_radius=18
                                ),

                                # ==================================
                                # PRAYER
                                # ==================================

                                ft.Container(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                "Today's Prayer",
                                                size=17,
                                                color=dark,
                                                weight=ft.FontWeight.BOLD
                                            ),

                                            ft.Text(
                                                prayer,
                                                size=12,
                                                color=gray,
                                                italic=True,
                                                width=240
                                            )
                                        ],

                                        spacing=8
                                    ),

                                    bgcolor="white",

                                    padding=ft.Padding(
                                        left=15,
                                        right=15,
                                        top=15,
                                        bottom=15
                                    ),

                                    border_radius=18
                                ),

                                ft.Container(
                                    height=20
                                )
                            ],

                            spacing=14
                        ),

                        padding=ft.Padding(
                            left=15,
                            right=15,
                            top=5,
                            bottom=20
                        )
                    )
                ],

                spacing=0,

                scroll=ft.ScrollMode.AUTO,

                expand=True
            )
        )

        page.update()

    # ==================================================
    # CREATE CARD
    # ==================================================

    def create_card(
        day,
        theme,
        scripture_reference,
        scripture_text,
        reading_time,
        category,
        introduction,
        reflection,
        prayer,
        key_lesson,
        author
    ):

        return ft.Container(

            content=ft.Column(
                [
                    # ==================================
                    # DAY + BOOKMARK
                    # ==================================

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

                                padding=ft.Padding(
                                    left=12,
                                    right=12,
                                    top=7,
                                    bottom=7
                                ),

                                border_radius=20
                            ),

                            ft.Icon(
                                ft.Icons.BOOKMARK_BORDER,
                                color=gray
                            )
                        ],

                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    ),

                    # ==================================
                    # THEME
                    # ==================================

                    ft.Text(
                        theme,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=dark,
                        width=264
                    ),

                    # ==================================
                    # SCRIPTURE
                    # ==================================

                    ft.Text(
                        scripture_reference,
                        size=12,
                        color=purple,
                        width=264
                    ),

                    # ==================================
                    # CATEGORY + READING TIME
                    # ==================================

                    ft.Row(
                        [
                            ft.Text(
                                category,
                                size=11,
                                color=gray,
                                expand=True
                            ),

                            ft.Text(
                                str(reading_time),
                                size=11,
                                color=gray,
                                text_align=ft.TextAlign.RIGHT
                            )
                        ],

                        spacing=8,

                        vertical_alignment=ft.CrossAxisAlignment.START
                    ),

                    ft.Divider(),

                    # ==================================
                    # SEE MORE
                    # ==================================

                    ft.Row(
                        [
                            ft.Button(
                                content="See More",

                                on_click=lambda e:
                                devotional_details(
                                    day,
                                    theme,
                                    scripture_reference,
                                    scripture_text,
                                    reading_time,
                                    category,
                                    introduction,
                                    reflection,
                                    prayer,
                                    key_lesson,
                                    author
                                ),

                                style=ft.ButtonStyle(
                                    bgcolor=purple,
                                    color="white",

                                    padding=ft.Padding(
                                        left=15,
                                        right=15,
                                        top=9,
                                        bottom=9
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

                spacing=11
            ),

            bgcolor="white",

            padding=ft.Padding(
                left=18,
                right=18,
                top=18,
                bottom=18
            ),

            border_radius=20,

            shadow=ft.BoxShadow(
                blur_radius=10,
                spread_radius=0,
                color="#15000000",
                offset=ft.Offset(0, 3)
            )
        )

    # ==================================================
    # LOAD JSON AND LOOP
    # ==================================================

    def devotional(e):

        with open(
            "devotional.json",
            "r",
            encoding="utf-8"
        ) as file:

            devotionals = json.load(file)

        search_list = search.value.lower()

        devotional_list.controls.clear()

        for dev in devotionals["devotionals"]:

            day = dev["day"]

            theme = dev["theme"]

            scripture_reference = dev["scripture"]["reference"]

            scripture_text = dev["scripture"]["text"]

            reading_time = dev["reading_time_minutes"]

            category = dev["devotional"]

            introduction = dev["title"]

            reflection = dev["title"]

            prayer = dev["title"]

            key_lesson = dev["title"]

            author = dev["title"]

            if search_list in theme.lower():

                devotional_list.controls.append(

                    create_card(

                        day,
                        theme,
                        scripture_reference,
                        scripture_text,
                        reading_time,
                        category,
                        introduction,
                        reflection,
                        prayer,
                        key_lesson,
                        author

                    )
                )

        devotional_list.update()

    # ==================================================
    # SEARCH
    # ==================================================

    search = ft.TextField(
        hint_text="Search devotionals...",

        border="none",

        bgcolor="white",

        prefix_icon=ft.Icons.SEARCH,


        height=48,

        content_padding=ft.Padding(
            left=15,
            right=15,
            top=8,
            bottom=8
        ),

        border_radius=15,

        on_change=devotional
    )

    # ==================================================
    # CATEGORY
    # ==================================================

    category_row = ft.Row(
        scroll=ft.ScrollMode.AUTO,
        spacing=8
    )

    # ==================================================
    # MAIN PAGE
    # ==================================================

    page.controls.clear()

    page.add(

        ft.Column(
            [

                ft.Row(
                    [
                        ft.IconButton(
                            ft.Icons.ARROW_BACK,
                            icon_color=purple,
                            on_click=lambda e: page.go("/")
                        ),

                        ft.Text(
                            "Devotional Library",
                            size=21,
                            color=dark,
                            weight=ft.FontWeight.BOLD,
                            expand=True
                        )
                    ]
                ),

                ft.Text(
                    "Grow spiritually every day",
                    size=12,
                    color=gray
                ),

                search,

                ft.Text(
                    "Daily Devotion",
                    size=19,
                    color=dark,
                    weight=ft.FontWeight.BOLD
                ),

                category_row,

                devotional_list

            ],

            spacing=15,

            expand=True,

            scroll=ft.ScrollMode.AUTO
        )
    )

    devotional(search)


ft.run(devotional_page)
