
import flet as ft,json
def main(page: ft.Page):
    page.bgcolor = "#F8F5F0"
    page.padding = 0
    page.window.width = 390
    
    def PrayerCard(title, verse, preview, color, icon):
        return ft.Container(
            bgcolor="white",
            border_radius=20,
            padding=ft.Padding(18, 18, 18, 18),
            margin=ft.Margin(0, 0, 0, 14),
            shadow=ft.BoxShadow(blur_radius=15, color="#00000010", offset=ft.Offset(0, 6)),
            content=ft.Row(
                spacing=14,
                controls=[
                    ft.Container(
                        width=56,
                        height=56,
                        bgcolor=color,
                        border_radius=16,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Icon(icon, color="#2B2B2B", size=26)
                    ),
                    ft.Column(
                        expand=True,
                        spacing=4,
                        controls=[
                            ft.Text(title, size=15, weight=ft.FontWeight.BOLD, color="#2B2B2B"),
                            ft.Text(preview, size=13, color="#8D7E6B", max_lines=1),
                            ft.Row(
                                spacing=5,
                                controls=[
                                    ft.Icon(ft.Icons.MENU_BOOK, size=12, color="#C4A46A"),
                                    ft.Text(verse, size=11, color="#C4A46A", weight=ft.FontWeight.BOLD),
                                ]
                            )
                        ]
                    ),
                    ft.Icon(ft.Icons.ARROW_FORWARD_IOS, size=14, color="#D6C8B6")
                ]
            )
        )
    def healing(e):
        with open("healings_1000_unique.json","r",encoding="utf-8") as f:
            healingprayer=json.load(f)
        search=searching.value.lower() 
        prayers_list.controls.clear()
        for heal in healingprayer["prayers"]:
            prayer=heal['title']
            prayer1=heal['bible_references'][0]
            prayer2=heal['bible_references'][2]
            if search in prayer.lower():
                prayers_list.controls.append(PrayerCard(prayer,prayer1,prayer2,"green",ft.Icons.FAVORITE))
            
                
    searching=ft.TextField(hint_text="Search healing prayer...", width=320,border_radius=10, color="#B8A898",on_change=healing,expand=True)                  
    header = ft.Container(
        padding=ft.Padding(25, 50, 25, 25),
        content=ft.Column(
            spacing=18,
            controls=[
                ft.Row(
                    controls=[
                        ft.Column(
                            spacing=0,
                            controls=[
                                ft.Text("Healing Prayers", size=14, color="#8D7E6B"),
                                ft.Text("Be Made Whole", size=26, weight=ft.FontWeight.BOLD, color="#2B2B2B"),
                            ]
                        ),
                        ft.Container(expand=True),
                        ft.Container(
                            width=44, height=44,
                            bgcolor="white",
                            border_radius=22,
                            alignment=ft.Alignment(0, 0),
                            content=ft.Icon(ft.Icons.FAVORITE, color="#C4A46A")
                        )
                    ]
                ),
                ft.Container(
                    bgcolor="white",
                    border_radius=15,
                    height=50,
                    padding=ft.Padding(16, 0, 16, 0),
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.Icons.SEARCH, color="#C4A46A", size=20),
                            searching
                        ]
                    )
                ),
                ft.Row(
                    spacing=10,
                    controls=[
                        ft.Container(bgcolor="#2B2B2B", border_radius=20, padding=ft.Padding(18, 8, 18, 8), content=ft.Text("All", color="white", size=13, weight=ft.FontWeight.BOLD)),
                        ft.Container(bgcolor="white", border_radius=20, padding=ft.Padding(18, 8, 18, 8), border=ft.BorderSide(1, "#E8E0D6"), content=ft.Text("Healing", color="#8D7E6B", size=13)),
                        ft.Container(bgcolor="white", border_radius=20, padding=ft.Padding(18, 8, 18, 8), border=ft.BorderSide(1, "#E8E0D6"), content=ft.Text("Peace", color="#8D7E6B", size=13)),
                        ft.Container(bgcolor="white", border_radius=20, padding=ft.Padding(18, 8, 18, 8), border=ft.BorderSide(1, "#E8E0D6"), content=ft.Text("Strength", color="#8D7E6B", size=13)),
                    ]
                )
            ]
        )
    )

    prayers_list = ft.Column(
        spacing=0,
        scroll=ft.ScrollMode.AUTO,
        expand=True,
        controls=[
            ft.Container(
                padding=ft.Padding(20, 0, 20, 0),
                content=ft.Column(
                    spacing=0,
                    # controls=[
                    #     PrayerCard("Prayer for Physical Healing", "Jeremiah 30:17", "I will restore you to health and heal your wounds...", "#E8F5E9", ft.Icons.FAVORITE),
                    #     PrayerCard("Prayer for Anxiety & Sleep", "Psalm 4:8", "In peace I will lie down and sleep for you alone...", "#E3F2FD", ft.Icons.NIGHTLIGHT_ROUND),
                    #     PrayerCard("Prayer for Inner Strength", "Isaiah 41:10", "Do not fear, for I am with you. I will strengthen you...", "#FFF3E0", ft.Icons.SELF_IMPROVEMENT),
                    #     PrayerCard("Prayer for Family Healing", "Psalm 103:3", "He forgives all your sins and heals all your diseases...", "#F3E5F5", ft.Icons.FAMILY_RESTROOM),
                    #     PrayerCard("Prayer for Broken Heart", "Psalm 147:3", "He heals the brokenhearted and binds up their wounds...", "#FFEBEE", ft.Icons.HEALING),
                    # ]
                )
            )
        ]
    )
    page.add(
        ft.Column(
            expand=True,
            spacing=0,
            controls=[header, prayers_list]
        )
    )
    healing(searching) 
ft.run(main)