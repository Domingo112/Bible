
import flet as ft
import json


def devotional_page(page: ft.Page):
    page.views.append(
        ft.View(
            route="/showprayer"
        )
    )
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

    
    
                   
    def create_card(
        day,
        theme,
        scripture_reference,
        scripture_text,
        
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
                        day,
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
                                theme,
                                size=15,
                                color="black",
                                expand=True
                            ),

                            
                        ],

                        spacing=8,

                        vertical_alignment=ft.CrossAxisAlignment.START
                    ),

                    ft.Divider(),

                    # ==================================
                    # PRAYER
                    # ==================================

                    ft.Column(
                        [
                            ft.Text("Prayer :",text_align=ft.TextAlign.CENTER),
                         ft.Text(
                            scripture_text,
                            italic=True,
                            size=15,
                            color="black",
                            weight=ft.FontWeight.BOLD),
                            
                           
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
    def seemore():
            day=page.session.store.get("day")
            with open("prayer.json","r", encoding="utf-8") as file:
                devotionals = json.load(file)   
            listing=[]    
            for dev in devotionals["prayers"]:
                if  dev["id"] == day:
                    
                    listing.append({
                        "title":dev["title"],
                        "category":dev["category"],
                        "scripture_reference":dev["scripture_reference"],
                        "text":dev["text"],

                    
                    })
            loop=listing
            for l in loop:
                devotional_list.controls.append(
                     create_card(l["title"],l["scripture_reference"],l["category"],l["text"],
                                )) 
  

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
                            on_click=lambda e: page.navigate("/prayer")
                        ),

                        ft.Text(
                            "Meditation",
                            size=21,
                            color=dark,
                            weight=ft.FontWeight.BOLD,
                            expand=True
                        )
                    ]
                ),

                category_row,

                devotional_list

            ],

            spacing=15,

            expand=True,

            scroll=ft.ScrollMode.AUTO
        )
    )
    seemore()

