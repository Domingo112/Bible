
import flet as ft
import json


def main(page: ft.Page):
    page.bgcolor = "#F8F5F0"
    page.padding = 0
    page.window.width = 300
    page.window.height = 700

    # Stores the prayer selected from the list.
    # The selected prayer is then displayed by the /prayer route.
    selected_prayer = {}


    # =========================================================
    # FULL PRAYER PAGE
    # =========================================================

    def full_prayer_page(title, bible_references, prayer, category):

        # Back button
        # Always return through the Flet router.
        def go_back(e):
            page.go("/healing")

        # -----------------------------------------------------
        # HEADER
        # -----------------------------------------------------

        header = ft.Container(
            padding=ft.Padding(20, 45, 20, 20),

            content=ft.Row(
                controls=[

                    ft.Container(
                        width=42,
                        height=42,
                        bgcolor="white",
                        border_radius=21,
                        alignment=ft.Alignment(0, 0),

                        content=ft.IconButton(
                            icon=ft.Icons.ARROW_BACK,
                            icon_color="#2B2B2B",
                            icon_size=20,
                            on_click=go_back
                        )
                    ),

                    ft.Container(expand=True),

                    ft.Container(
                        width=42,
                        height=42,
                        bgcolor="white",
                        border_radius=21,
                        alignment=ft.Alignment(0, 0),

                        content=ft.Icon(
                            ft.Icons.FAVORITE,
                            color="#C4A46A",
                            size=20
                        )
                    )
                ]
            )
        )

        # -----------------------------------------------------
        # TITLE SECTION
        # -----------------------------------------------------

        title_section = ft.Container(
            padding=ft.Padding(25, 5, 25, 20),

            content=ft.Column(
                spacing=8,

                controls=[

                    ft.Text(
                        category.upper(),
                        size=11,
                        color="#C4A46A",
                        weight=ft.FontWeight.BOLD
                    ),

                    ft.Text(
                        title,
                        size=28,
                        color="#2B2B2B",
                        weight=ft.FontWeight.BOLD,
                        width=340
                    ),

                    ft.Row(
                        spacing=6,

                        controls=[

                            ft.Icon(
                                ft.Icons.MENU_BOOK,
                                size=15,
                                color="#C4A46A"
                            ),

                            ft.Text(
                                bible_references,
                                size=12,
                                color="#8D7E6B",
                                weight=ft.FontWeight.BOLD,
                                expand=True
                            )
                        ]
                    )
                ]
            )
        )

        # -----------------------------------------------------
        # BIBLE REFERENCE CARD
        # -----------------------------------------------------

        reference_card = ft.Container(
            margin=ft.Margin(20, 0, 20, 18),

            padding=ft.Padding(18, 16, 18, 16),

            bgcolor="#FFF8EC",

            border_radius=16,

            border=ft.BorderSide(
                1,
                "#E8DCC8"
            ),

            content=ft.Row(
                spacing=12,

                controls=[

                    ft.Container(
                        width=40,
                        height=40,
                        bgcolor="#E8DCC8",
                        border_radius=12,
                        alignment=ft.Alignment(0, 0),

                        content=ft.Icon(
                            ft.Icons.MENU_BOOK,
                            color="#8D6E3F",
                            size=20
                        )
                    ),

                    ft.Column(
                        spacing=2,
                        expand=True,

                        controls=[

                            ft.Text(
                                "SCRIPTURE",
                                size=10,
                                color="#A18D74",
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Text(
                                bible_references,
                                size=14,
                                color="#5E513F",
                                weight=ft.FontWeight.BOLD
                            )
                        ]
                    )
                ]
            )
        )

        # -----------------------------------------------------
        # PRAYER CONTENT
        # -----------------------------------------------------

        prayer_card = ft.Container(

            margin=ft.Margin(20, 0, 20, 25),

            padding=ft.Padding(22, 22, 22, 22),

            bgcolor="white",

            border_radius=20,

            shadow=ft.BoxShadow(
                blur_radius=15,
                color="#00000010",
                offset=ft.Offset(0, 6)
            ),

            content=ft.Column(
                spacing=15,

                controls=[

                    ft.Row(
                        spacing=8,

                        controls=[

                            ft.Container(
                                width=35,
                                height=35,
                                bgcolor="#E8F5E9",
                                border_radius=11,
                                alignment=ft.Alignment(0, 0),

                                content=ft.Icon(
                                    ft.Icons.FAVORITE,
                                    color="#4CAF50",
                                    size=19
                                )
                            ),

                            ft.Text(
                                "Prayer",
                                size=17,
                                color="#2B2B2B",
                                weight=ft.FontWeight.BOLD
                            )
                        ]
                    ),

                    # IMPORTANT:
                    # selectable=True lets the user select/copy
                    # the prayer text.

                    ft.Text(
                        prayer,
                        size=15,
                        color="#4A443D",
                        selectable=True,
                        width=320
                    ),

                    ft.Container(
                        margin=ft.Margin(0, 8, 0, 0),
                        height=1,
                        bgcolor="#EEE7DE"
                    ),

                    ft.Text(
                        "Amen.",
                        size=16,
                        color="#C4A46A",
                        italic=True,
                        weight=ft.FontWeight.BOLD
                    )
                ]
            )
        )

        # -----------------------------------------------------
        # SCROLLABLE BODY
        # -----------------------------------------------------

        body = ft.ListView(
            expand=True,
            spacing=0,

            controls=[
                title_section,
                reference_card,
                prayer_card,

                ft.Container(
                    height=30
                )
            ]
        )

        # -----------------------------------------------------
        # COMPLETE PAGE
        # -----------------------------------------------------

        return ft.Column(
            expand=True,
            spacing=0,

            controls=[
                header,
                body
            ]
        )


    # =========================================================
    # PRAYER CARD
    # =========================================================

    def PrayerCard(
        title,
        verse,
        preview,
        color,
        icon,
        full_prayer,
        category
    ):

        def open_prayer(e):
            # Save the clicked prayer, then navigate to its route.
            selected_prayer.clear()
            selected_prayer.update({
                "title": title,
                "verse": verse,
                "prayer": full_prayer,
                "category": category
            })

            page.go("/prayer")


        return ft.Container(

            bgcolor="white",

            border_radius=20,

            padding=ft.Padding(
                18,
                18,
                18,
                18
            ),

            margin=ft.Margin(
                0,
                0,
                0,
                14
            ),

            shadow=ft.BoxShadow(
                blur_radius=15,
                color="#00000010",
                offset=ft.Offset(0, 6)
            ),

            on_click=open_prayer,

            ink=True,

            content=ft.Row(

                spacing=14,

                controls=[

                    ft.Container(
                        width=56,
                        height=56,

                        bgcolor=color,

                        border_radius=16,

                        alignment=ft.Alignment(
                            0,
                            0
                        ),

                        content=ft.Icon(
                            icon,
                            color="#2B2B2B",
                            size=26
                        )
                    ),

                    ft.Column(

                        expand=True,

                        spacing=4,

                        controls=[

                            ft.Text(
                                title,
                                size=15,
                                weight=ft.FontWeight.BOLD,
                                color="#2B2B2B",
                                max_lines=2,
                                overflow=ft.TextOverflow.ELLIPSIS
                            ),

                            ft.Text(
                                preview,
                                size=13,
                                color="#8D7E6B",
                                max_lines=1,
                                overflow=ft.TextOverflow.ELLIPSIS
                            ),

                            ft.Row(

                                spacing=5,

                                controls=[

                                    ft.Icon(
                                        ft.Icons.MENU_BOOK,
                                        size=12,
                                        color="#C4A46A"
                                    ),

                                    ft.Text(
                                        verse,
                                        size=11,
                                        color="#C4A46A",
                                        weight=ft.FontWeight.BOLD,
                                        max_lines=1,
                                        overflow=ft.TextOverflow.ELLIPSIS,
                                        expand=True
                                    )
                                ]
                            )
                        ]
                    ),

                    ft.Icon(
                        ft.Icons.ARROW_FORWARD_IOS,
                        size=14,
                        color="#D6C8B6"
                    )
                ]
            )
        )


    # =========================================================
    # LOAD PRAYERS
    # =========================================================

    with open(
        "healings_1000_unique.json",
        "r",
        encoding="utf-8"
    ) as f:

        healingprayer = json.load(f)


    # =========================================================
    # PRAYER LIST
    # =========================================================

    prayers_list = ft.ListView(
        spacing=0,
        expand=True
    )


    # =========================================================
    # SEARCH
    # =========================================================

    def healing(e):

        search = searching.value.lower().strip()

        prayers_list.controls.clear()

        for heal in healingprayer["prayers"]:

            title = heal["title"]

            # Get all Bible references safely
            references = heal.get(
                "bible_references",
                []
            )

            if isinstance(
                references,
                list
            ):

                verse = ", ".join(
                    references
                )

            else:

                verse = str(
                    references
                )

            prayer = heal["prayer"]

            category = heal.get(
                "category",
                "Healing"
            )

            # First part of the prayer
            preview = prayer[:100]

            if search in title.lower():

                prayers_list.controls.append(

                    PrayerCard(

                        title=title,

                        verse=verse,

                        preview=preview,

                        color="#E8F5E9",

                        icon=ft.Icons.FAVORITE,

                        full_prayer=prayer,

                        category=category
                    )
                )

        page.update()


    # =========================================================
    # SEARCH FIELD
    # =========================================================

    searching = ft.TextField(

        hint_text="Search healing prayer...",

        color="#B8A898",

        border=ft.InputBorder.NONE,

        text_size=13,

        expand=True,

        on_change=healing
    )


    # =========================================================
    # HEADER
    # =========================================================

    header = ft.Container(

        padding=ft.Padding(
            25,
            50,
            25,
            25
        ),

        content=ft.Column(

            spacing=18,

            controls=[

                ft.Row(

                    controls=[
                            ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                icon_color="#2B2B2B",
                                icon_size=20,
                                on_click=lambda e: page.go("/home")
                                    ),
                            ft.Text(""),  
                        ft.Column(

                            spacing=0,

                            controls=[
                                 
                                ft.Text(
                                    "Healing Prayers",
                                    size=14,
                                    color="#8D7E6B"
                                ),

                                ft.Text(
                                    "Be Made Whole",
                                    size=26,
                                    weight=ft.FontWeight.BOLD,
                                    color="#2B2B2B"
                                )
                            ]
                        ),

                        ft.Container(
                            expand=True
                        ),

                        ft.Container(

                            width=44,
                            height=44,

                            bgcolor="white",

                            border_radius=22,

                            alignment=ft.Alignment(
                                0,
                                0
                            ),

                            content=ft.Icon(
                                ft.Icons.FAVORITE,
                                color="#C4A46A"
                            )
                        )
                    ]
                ),

                # SEARCH BOX

                ft.Container(

                    bgcolor="white",

                    border_radius=15,

                    height=50,

                    padding=ft.Padding(
                        16,
                        0,
                        16,
                        0
                    ),

                    content=ft.Row(

                        controls=[

                            ft.Icon(
                                ft.Icons.SEARCH,
                                color="#C4A46A",
                                size=20
                            ),

                            searching
                        ]
                    )
                ),

                # CATEGORY BUTTONS

                ft.Row(

                    spacing=10,

                    scroll=ft.ScrollMode.AUTO,

                    controls=[

                        ft.Container(
                            bgcolor="#2B2B2B",
                            border_radius=20,
                            padding=ft.Padding(
                                18,
                                8,
                                18,
                                8
                            ),

                            content=ft.Text(
                                "All",
                                color="white",
                                size=13,
                                weight=ft.FontWeight.BOLD
                            )
                        ),

                        ft.Container(
                            bgcolor="white",
                            border_radius=20,
                            padding=ft.Padding(
                                18,
                                8,
                                18,
                                8
                            ),

                            border=ft.BorderSide(
                                1,
                                "#E8E0D6"
                            ),

                            content=ft.Text(
                                "Healing",
                                color="#8D7E6B",
                                size=13
                            )
                        ),

                        ft.Container(
                            bgcolor="white",
                            border_radius=20,
                            padding=ft.Padding(
                                18,
                                8,
                                18,
                                8
                            ),

                            border=ft.BorderSide(
                                1,
                                "#E8E0D6"
                            ),

                            content=ft.Text(
                                "Peace",
                                color="#8D7E6B",
                                size=13
                            )
                        ),

                        ft.Container(
                            bgcolor="white",
                            border_radius=20,
                            padding=ft.Padding(
                                18,
                                8,
                                18,
                                8
                            ),

                            border=ft.BorderSide(
                                1,
                                "#E8E0D6"
                            ),

                            content=ft.Text(
                                "Strength",
                                color="#8D7E6B",
                                size=13
                            )
                        )
                    ]
                )
            ]
        )
    )


    # =========================================================
    # MAIN PAGE
    # =========================================================

    def main_page():

        return ft.Column(

            expand=True,

            spacing=0,

            controls=[

                header,

                ft.Container(

                    padding=ft.Padding(
                        20,
                        0,
                        20,
                        0
                    ),

                    expand=True,

                    content=prayers_list
                )
            ]
        )


    # =========================================================
    # ROUTING
    # =========================================================

    def home_page():
        # Replace this with your real app main/home page if this
        # Healing Prayers page is part of a larger application.
        return ft.Container(
            expand=True,
            bgcolor="#F8F5F0",
            alignment=ft.Alignment(0, 0),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15,
                controls=[
                    ft.Icon(
                        ft.Icons.HOME,
                        size=45,
                        color="#C4A46A"
                    ),
                    ft.Text(
                        "Main Page",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color="#2B2B2B"
                    ),
                    ft.Text(
                        "Replace home_page() with your actual main page.",
                        size=12,
                        color="#8D7E6B",
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.ElevatedButton(
                        "Open Healing Prayers",
                        on_click=lambda e: page.go("/healing")
                    )
                ]
            )
        )


    def route_change(e):
        # Remove the previous route view.
        page.views.clear()

        if page.route == "/home":

            page.views.append(
                ft.View(
                    "/home",
                    controls=[home_page()]
                )
            )

        elif page.route == "/healing":

            page.views.append(
                ft.View(
                    "/healing",
                    controls=[main_page()]
                )
            )

        elif page.route == "/prayer":

            # Make sure a prayer was selected before opening the detail page.
            if not selected_prayer:
                page.go("/healing")
                return

            page.views.append(
                ft.View(
                    "/prayer",
                    controls=[
                        full_prayer_page(
                            selected_prayer["title"],
                            selected_prayer["verse"],
                            selected_prayer["prayer"],
                            selected_prayer["category"]
                        )
                    ]
                )
            )

        else:
            page.go("/healing")
            return

        page.update()


    page.on_route_change = route_change

    # Start on the Healing Prayers page.
    page.go("/healing")

    # Load prayers immediately.
    healing(None)


if __name__ == "__main__":
    ft.run(main)


