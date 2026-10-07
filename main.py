import flet as ft
import test
import mainpage
import mainbible,readbible,seemore,devotion,prayer,showprayer,fullhealing,quiz

def main(page:ft.Page):
    def route_change():
        page.views.clear()
        if page.route=="/":
            test.main(page)
        elif page.route=="/home":
            mainpage.main(page)
        elif page.route =="/bible":
            mainbible.main(page)
        elif page.route == "/readbible":
            readbible.main(page)
        elif page.route == "/seemore":
            seemore.devotional_page(page) 
        elif page.route == "/devotion":
            devotion.devotional_page(page)
        elif page.route == "/prayer":
            prayer.devotional_page(page)
        elif page.route == "/showprayer":
            showprayer.devotional_page(page)
        elif page.route == "/healing":
            fullhealing.main(page)
        elif page.route == "/quiz":
            quiz.main(page)                            
        page.update()
        
    page.on_route_change=route_change
    route_change()
ft.run(main,host="192.168.101.79")          