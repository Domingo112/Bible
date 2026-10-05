import flet as ft
import json


def main(page: ft.Page):
    page.views.append(
        ft.View(route="/readbible")
    )
    # =========================================================
    # PAGE SETTINGS
    # =========================================================

    page.title = "Select Book"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 0
    page.window.width = 300
    page.window.height = 650


    # =========================================================
    # BIBLE FILES
    # =========================================================

    kjv = "biblejson.json"
    cath = "catholic_bible.json"


    # =========================================================
    # CURRENT BIBLE
    # =========================================================

    current_file = kjv

    with open(
        current_file,
        "r",
        encoding="utf-8"
    ) as f:

        bible = json.load(f)


    # =========================================================
    # SEARCH BOX
    # =========================================================

    search = ft.TextField(

        hint_text="Search books...",

        hint_style=ft.TextStyle(
            size=11,
            color=ft.Colors.GREY_700,
        ),

        text_style=ft.TextStyle(
            size=12,
        ),

        prefix_icon=ft.Icons.SEARCH,

        height=38,

        content_padding=ft.Padding.symmetric(
            horizontal=10,
            vertical=0,
        ),

        bgcolor=ft.Colors.GREY_100,

        border=ft.InputBorder.NONE,

        border_radius=20,
    )


    # =========================================================
    # BOOK LIST
    # =========================================================

    book_list = ft.ListView(

        spacing=2,

        expand=True,
    )


    # =========================================================
    # SELECTED VERSION TEXT
    # =========================================================

    version_text = ft.Text(
        "KJV",
        size=11,
        color=ft.Colors.GREY_600,
    )


    # =========================================================
    # ROUTING TO BIBLE READER
    # =========================================================

    def select_book(book):

        def mainbible(e):

            # Save selected book
            page.session.store.set(
                "books",
                book
            )

            # Save selected Bible version
            page.session.store.set(
                "version",
                current_file
            )

            # Go to Bible reader
            page.navigate("/bible")

        return ft.Container(

            height=43,

            padding=ft.Padding.symmetric(
                horizontal=7,
            ),

            border=ft.Border(

                bottom=ft.BorderSide(
                    1,
                    ft.Colors.GREY_200,
                )
            ),

            content=ft.Row(

                alignment=
                ft.MainAxisAlignment.SPACE_BETWEEN,

                vertical_alignment=
                ft.CrossAxisAlignment.CENTER,

                controls=[

                    ft.Text(
                        book,
                        size=13,
                        color=ft.Colors.BLACK_87,
                    ),

                    ft.IconButton(

                        ft.Icons.CHEVRON_RIGHT,

                        icon_size=17,

                        on_click=mainbible,

                        icon_color=
                        ft.Colors.GREY_600,
                    ),
                ],
            ),
        )


    # =========================================================
    # SHOW BOOKS
    # =========================================================

    def show_books():

        book_list.controls.clear()

        search_text = search.value.lower().strip()

        for book in bible["books"]:

            book_name = book["englishName"]

            if search_text in book_name.lower():

                book_list.controls.append(
                    select_book(book_name)
                )

        page.update()


    # =========================================================
    # SEARCH FUNCTION
    # =========================================================

    def search_bible(e):

        show_books()


    search.on_change = search_bible


    # =========================================================
    # CHANGE TO KJV
    # =========================================================

    def change_to_kjv(e):

        nonlocal bible
        nonlocal current_file

        current_file = kjv

        with open(
            current_file,
            "r",
            encoding="utf-8"
        ) as f:

            bible = json.load(f)

        # Change version name
        version_text.value = "KJV"

        # Clear search
        search.value = ""

        # Show KJV books
        show_books()


    # =========================================================
    # CHANGE TO CATHOLIC
    # =========================================================

    def change_to_catholic(e):

        nonlocal bible
        nonlocal current_file

        current_file = cath

        with open(
            current_file,
            "r",
            encoding="utf-8"
        ) as f:

            bible = json.load(f)

        # Change version name
        version_text.value = "CATH"

        # Clear search
        search.value = ""

        # Show Catholic books
        show_books()


    # =========================================================
    # VERSION BUTTONS
    # =========================================================

    version_buttons = ft.Row(

        spacing=5,

        controls=[

            ft.Button(
                "KJV",
                width=60,
                height=35,
                color=ft.Colors.BLACK,
                bgcolor="#F3F0EA",
                on_click=change_to_kjv,
            ),

            ft.Button(
                "CATH",
                width=70,
                height=35,
                color=ft.Colors.BLACK,
                bgcolor="#F3F0EA",
                on_click=change_to_catholic,
            ),
        ],
    )


    # =========================================================
    # HEADER
    # =========================================================

    header = ft.Row(

        controls=[

            ft.IconButton(

                icon=
                ft.Icons.ARROW_BACK_IOS_NEW,

                icon_size=17,

                icon_color=
                ft.Colors.BLACK_87,

                on_click=lambda e:
                page.navigate("/home")
            ),

            ft.Container(

                expand=True,

                alignment=ft.Alignment.CENTER,

                content=ft.Column(

                    spacing=0,

                    horizontal_alignment=
                    ft.CrossAxisAlignment.CENTER,

                    controls=[

                        ft.Text(
                            "Select Book",
                            size=16,
                            weight=
                            ft.FontWeight.BOLD,
                            color=
                            ft.Colors.BLACK,
                        ),

                        version_text,
                    ],
                ),
            ),

            version_buttons,
        ],
    )


    # =========================================================
    # MAIN UI
    # =========================================================

    main_content = ft.Container(

        expand=True,

        padding=ft.Padding.only(

            left=15,

            right=15,

            top=5,

            bottom=5,
        ),

        content=ft.Column(

            expand=True,

            spacing=8,

            controls=[

                header,

                search,

                ft.Container(

                    expand=True,

                    content=book_list,
                ),
            ],
        ),
    )


    # =========================================================
    # ADD TO PAGE
    # =========================================================

    page.add(main_content)


    # =========================================================
    # SHOW BOOKS WHEN PAGE OPENS
    # =========================================================

    show_books()


