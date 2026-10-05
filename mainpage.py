import flet as ft
from datetime import datetime
import json,random


def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/home"
        )
    )

    page.title = "Bible App"
    page.padding = 0
    page.spacing = 0
    page.bgcolor = "#F8F7F2"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.width = 300

    # =========================================================
    # COLORS
    # =========================================================

    GREEN = "#063F35"
    LIGHT_GREEN = "#EAF1ED"
    CREAM = "#F8F7F2"
    WHITE = "#FFFFFF"
    TEXT = "#111111"
    GREY = "#666666"

    # =========================================================
    # HEADER IMAGE
    # =========================================================
    #
    # Put your mountain image in the same folder as this file
    # and name it:
    #
    # mountain.jpg
    #
    # =========================================================
    salutation = ft.Text(
    "",
    size=25,
    weight=ft.FontWeight.BOLD,
    color=TEXT,)
    rantxt=ft.Text(
        "In His light, you are never alone.",
        size=14,
        color=TEXT,
    )
    versetxt=ft.Text(
        "Psalm 119:105",
        size=12,
        color=TEXT,
        weight=ft.FontWeight.BOLD,
        )
    header = ft.Container(
        height=230,
        border_radius=ft.BorderRadius.only(
            bottom_left=25,
            bottom_right=25,
        ),

        image=ft.DecorationImage(
            src="moutain.jpg",
            fit=ft.BoxFit.COVER,
        ),

        content=ft.Container(
            padding=ft.Padding.only(
                left=20,
                right=20,
                top=25,
                bottom=20,
            ),

            gradient=ft.LinearGradient(
                begin=ft.Alignment.TOP_CENTER,
                end=ft.Alignment.BOTTOM_CENTER,
                colors=[
                    ft.Colors.with_opacity(0.10, "white"),
                    ft.Colors.with_opacity(0.65, "white"),
                ],
            ),

            content=ft.Column(
                spacing=4,
                controls=[
                    salutation,
                    rantxt,

                    ft.Container(height=2),
                    versetxt,
                ],
            ),
        ),
    )

    # =========================================================
    # TODAY'S VERSE CARD
    # =========================================================


    # =========================================================
    # FEATURE CARD FUNCTION
    # =========================================================

    def feature_card(
        icon,
        title,
        icon_color=GREEN,
        icon_size=30,
    ):

        return ft.Container(
            expand=True,

            height=85,

            padding=ft.Padding.all(8),

            bgcolor=WHITE,

            border_radius=12,

            border=ft.Border.all(
                1,
                "#E7E7E2",
            ),

            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=6,

                controls=[

                    ft.Icon(
                        icon,
                        size=icon_size,
                        color=icon_color,
                    ),

                    ft.Text(
                        title,
                        size=11,
                        color=TEXT,
                        text_align=ft.TextAlign.CENTER,
                        max_lines=1,
                    ),
                ],
            ),
        )

    # =========================================================
    # FIRST ROW
    # =========================================================

    row_one = ft.Row(
        spacing=8,

        controls=[
            #for read bible
            ft.Container(
                expand=True,
                height=85,
                padding=ft.Padding.all(8),
                on_click=lambda e:page.navigate("/readbible"),
                bgcolor=WHITE,
                border_radius=12,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=6,
                
                    controls=[
                
                        ft.Icon(
                            ft.icons.Icons.MENU_BOOK,
                            size=30,
                            color=GREEN,
                            ),
                
                            ft.Text(
                            "Read Bible",
                            size=11,
                            color=TEXT,
                            text_align=ft.TextAlign.CENTER,
                            max_lines=1,
                                ),
                            ],
                            ),   
            ),
                #for Quiz
            ft.Container(
                            expand=True,
                            height=85,
                            padding=ft.Padding.all(8),
                            on_click=lambda e:page.navigate("/quiz"),
                            bgcolor=WHITE,
                            border_radius=12,
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=6,
                            
                                controls=[
                            
                                    ft.Icon(
                                        ft.icons.Icons.WB_SUNNY_OUTLINED,
                                        size=30,
                                        color="#daa520",
                                        ),
                            
                                        ft.Text(
                                        "Bible Quiz",
                                        size=11,
                                        color=TEXT,
                                        text_align=ft.TextAlign.CENTER,
                                        max_lines=1,
                                            ),
                                        ],
                                        ),   
                        ),
#Devotional
            ft.Container(
                                        expand=True,
                                        height=85,
                                        padding=ft.Padding.all(8),
                                        on_click=lambda e:page.navigate("/devotion"),
                                        bgcolor=WHITE,
                                        border_radius=12,
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=6,
                                        
                                            controls=[
                                        
                                                ft.Icon(
                                                    ft.icons.Icons.LOCAL_FLORIST,
                                                    size=30,
                                                    color=GREEN,
                                                    ),
                                        
                                                    ft.Text(
                                                    "Devotional",
                                                    size=11,
                                                    color=TEXT,
                                                    text_align=ft.TextAlign.CENTER,
                                                    max_lines=1,
                                                        ),
                                                    ],
                                                    ),   
                                    ),
        ],
    )

    # =========================================================
    # SECOND ROW
    # =========================================================

    row_two = ft.Row(
        spacing=8,

        controls=[
            #For prayer
            ft.Container(
                                        expand=True,
                                        height=85,
                                        padding=ft.Padding.all(8),
                                        on_click=lambda e:page.navigate("/prayer"),
                                        bgcolor=WHITE,
                                        border_radius=12,
                                        content=ft.Column(
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            spacing=6,
                                        
                                            controls=[
                                        
                                                ft.Icon(
                                                    ft.icons.Icons.SELF_IMPROVEMENT,
                                                    size=30,
                                                    color=GREEN,
                                                    ),
                                        
                                                    ft.Text(
                                                    "Prayer",
                                                    size=11,
                                                    color=TEXT,
                                                    text_align=ft.TextAlign.CENTER,
                                                    max_lines=1,
                                                        ),
                                                    ],
                                                    ),   
                                    ),

            #For Healing
            ft.Container(
                expand=True,
                height=85,
                padding=ft.Padding.all(8),
                on_click=lambda e:page.navigate("/healing"),
                bgcolor=WHITE,
                border_radius=12,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=6,
                        controls=[
                                                    
                            ft.Icon(
                                ft.icons.Icons.SELF_IMPROVEMENT,
                                size=30,
                                color=GREEN,
                                ),
                                                    
                                 ft.Text(
                                "Healing",
                                size=11,
                                color=TEXT,
                                text_align=ft.TextAlign.CENTER,
                                max_lines=1,
                                                ),
                                            ],
                                        ),   
                                ),

            
        ],
    )

    # =========================================================
    # FEATURES SECTION
    # =========================================================

    features = ft.Container(
        padding=ft.Padding.only(
            left=20,
            right=20,
            top=12,
        ),

        content=ft.Column(
            spacing=8,

            controls=[
                row_one,
                row_two,
            ],
        ),
    )

    # =========================================================
    # BOTTOM NAVIGATION
    # =========================================================

    def nav_item(icon, label, selected=False):

        return ft.Container(
            expand=True,

            padding=ft.Padding.only(
                top=8,
                bottom=5,
            ),

            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=2,

                controls=[

                    ft.Icon(
                        icon,
                        size=21,
                        color=GREEN if selected else "#555555",
                    ),

                    ft.Text(
                        label,
                        size=9,
                        color=GREEN if selected else "#555555",
                        weight=(
                            ft.FontWeight.BOLD
                            if selected
                            else ft.FontWeight.NORMAL
                        ),
                    ),
                ],
            ),
        )

    

      

    # =========================================================
    # MAIN PAGE
    # =========================================================
    def time():
        time = datetime.now().hour

        if time <= 11:
            salutation.value = "Good Morning"
        elif time <= 16:
            salutation.value = "Good Afternoon"
        elif time <= 19:
            salutation.value = "Good Evening"
        elif time <= 23:
            salutation.value = "Good Night"
        else:
            salutation.value = "Good Night"
        page.update()
    time() 
      
    #function for random bible portions
    def bible_rand():
        #json extraction for the bible
        with open("biblejson.json","r",encoding="utf-8") as f:
            bible=json.load(f)
        listing=[] 
        for book in bible["books"]:
            for chapter in book["chapters"]:
                for verse in chapter["verses"]:
                    listing.append({
                        "englishName":book["englishName"],
                        "chapters":chapter["chapter"],
                        "verses":verse["number"],
                        "text":verse["text"]
                        })
        randtxt=random.choice(listing)
        rantxt.value=randtxt["text"]
        versetxt.value = f"{randtxt["englishName"]} {randtxt["chapters"]}:{randtxt["verses"]}"
    bible_rand()      
    page.add(

        ft.Column(
            expand=True,
            spacing=0,

            controls=[

                # Header + verse + features scroll together
                ft.Container(
                    expand=True,

                    content=ft.ListView(
                        expand=True,
                        spacing=0,

                        controls=[

                            header,

                            features,
                            # Extra space above navigation
                            ft.Container(
                                height=15,
                            ),
                        ],
                    ),
                ),

               
            ],
        )
    )


