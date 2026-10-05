import flet as ft
import random


def main(page: ft.Page):
    page.views.append(
        ft.View(
            route="/quiz"
        )
    )

    # =========================================================
    # PAGE SETTINGS
    # =========================================================

    page.title = "Bible Quiz"
    page.bgcolor = "#F8F5F0"
    page.padding = 0

    page.window.width = 350
    page.window.height = 700

    # =========================================================
    # QUIZ QUESTIONS
    # =========================================================

    questions = [
        {
            "question": "Who built the ark?",
            "options": [
                "Moses",
                "Noah",
                "Abraham",
                "David"
            ],
            "answer": "Noah"
        },

        {
            "question": "Who was the first man created by God?",
            "options": [
                "Adam",
                "Abel",
                "Noah",
                "Jacob"
            ],
            "answer": "Adam"
        },

        {
            "question": "Who led the Israelites out of Egypt?",
            "options": [
                "Joshua",
                "Aaron",
                "Moses",
                "David"
            ],
            "answer": "Moses"
        },

        {
            "question": "How many disciples did Jesus choose?",
            "options": [
                "7",
                "10",
                "12",
                "15"
            ],
            "answer": "12"
        },

        {
            "question": "Who defeated Goliath?",
            "options": [
                "Saul",
                "David",
                "Solomon",
                "Samuel"
            ],
            "answer": "David"
        },

        {
            "question": "What is the first book of the Bible?",
            "options": [
                "Exodus",
                "Matthew",
                "Genesis",
                "Psalms"
            ],
            "answer": "Genesis"
        },

        {
            "question": "Who was thrown into the lions' den?",
            "options": [
                "Daniel",
                "Joseph",
                "Elijah",
                "Jeremiah"
            ],
            "answer": "Daniel"
        },

        {
            "question": "Who betrayed Jesus?",
            "options": [
                "Peter",
                "John",
                "Judas Iscariot",
                "Thomas"
            ],
            "answer": "Judas Iscariot"
        },

        {
            "question": "What did Jesus turn water into?",
            "options": [
                "Oil",
                "Wine",
                "Juice",
                "Milk"
            ],
            "answer": "Wine"
        },

        {
            "question": "Who was known as the wisest king of Israel?",
            "options": [
                "David",
                "Saul",
                "Solomon",
                "Hezekiah"
            ],
            "answer": "Solomon"
        }
    ]

    # =========================================================
    # QUIZ VARIABLES
    # =========================================================

    random.shuffle(questions)

    current_question = 0
    score = 0
    answered = False

    # =========================================================
    # UI CONTROLS
    # =========================================================

    question_number = ft.Text(
        "",
        size=13,
        color="#8D7E6B",
        weight=ft.FontWeight.BOLD
    )

    score_text = ft.Text(
        "Score: 0",
        size=13,
        color="#C4A46A",
        weight=ft.FontWeight.BOLD
    )

    question_text = ft.Text(
        "",
        size=22,
        color="#2B2B2B",
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    options_column = ft.Column(
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )

    feedback_text = ft.Text(
        "",
        size=14,
        text_align=ft.TextAlign.CENTER
    )

    # =========================================================
    # NEXT BUTTON
    # =========================================================

    next_button = ft.Button(
        "NEXT QUESTION",
        width=200,
        height=50,
        color="white",
        bgcolor="#2B2B2B",
        visible=False,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(
                radius=25
            )
        )
    )

    # =========================================================
    # PROGRESS BAR
    # =========================================================

    progress_bar = ft.ProgressBar(
        value=0,
        height=6,
        color="#C4A46A",
        bgcolor="#E8E0D6"
    )

    # =========================================================
    # OPTION BUTTON
    # =========================================================

    def create_option(text):

        button = ft.Container(
            width=310,
            padding=ft.Padding(
                18,
                15,
                18,
                15
            ),
            bgcolor="white",
            border_radius=15,
            border=ft.Border.all(
                1,
                "#E8E0D6"
            ),
            ink=True
        )

        # Store the answer on the container
        button.data = text

        def select_answer(e):

            nonlocal score, answered

            # Prevent selecting another answer
            # after an answer has already been selected
            if answered:
                return

            answered = True

            correct_answer = (
                questions[current_question]["answer"]
            )

            # =================================================
            # CORRECT ANSWER
            # =================================================

            if text == correct_answer:

                score += 1

                button.bgcolor = "#E8F5E9"

                button.border = ft.Border.all(
                    2,
                    "#4CAF50"
                )

                feedback_text.value = (
                    "Correct! Well done."
                )

                feedback_text.color = "#4CAF50"

            # =================================================
            # WRONG ANSWER
            # =================================================

            else:

                button.bgcolor = "#FFEBEE"

                button.border = ft.Border.all(
                    2,
                    "#E53935"
                )

                feedback_text.value = (
                    f"Not quite. "
                    f"The correct answer is "
                    f"{correct_answer}."
                )

                feedback_text.color = "#E53935"

                # ---------------------------------------------
                # HIGHLIGHT CORRECT ANSWER
                # ---------------------------------------------

                for control in options_column.controls:

                    if hasattr(control, "data"):

                        if control.data == correct_answer:

                            control.bgcolor = "#E8F5E9"

                            control.border = ft.Border.all(
                                2,
                                "#4CAF50"
                            )

            # =================================================
            # UPDATE SCORE
            # =================================================

            score_text.value = f"Score: {score}"

            # =================================================
            # SHOW NEXT QUESTION BUTTON
            # =================================================

            next_button.visible = True

            page.update()

        # =====================================================
        # OPTION TEXT
        # =====================================================

        button.content = ft.Text(
            text,
            size=14,
            color="#4A443D",
            weight=ft.FontWeight.W_500,
            text_align=ft.TextAlign.CENTER
        )

        button.on_click = select_answer

        return button

    # =========================================================
    # LOAD QUESTION
    # =========================================================

    def load_question():

        nonlocal answered

        answered = False

        question = questions[current_question]

        # -----------------------------------------------------
        # QUESTION NUMBER
        # -----------------------------------------------------

        question_number.value = (
            f"QUESTION "
            f"{current_question + 1} "
            f"OF "
            f"{len(questions)}"
        )

        # -----------------------------------------------------
        # QUESTION TEXT
        # -----------------------------------------------------

        question_text.value = question["question"]

        # -----------------------------------------------------
        # CLEAR OLD FEEDBACK
        # -----------------------------------------------------

        feedback_text.value = ""

        # -----------------------------------------------------
        # UPDATE SCORE
        # -----------------------------------------------------

        score_text.value = f"Score: {score}"

        # -----------------------------------------------------
        # UPDATE PROGRESS
        # -----------------------------------------------------

        progress_bar.value = (
            (current_question + 1)
            / len(questions)
        )

        # -----------------------------------------------------
        # REMOVE OLD OPTIONS
        # -----------------------------------------------------

        options_column.controls.clear()

        # -----------------------------------------------------
        # COPY OPTIONS
        # -----------------------------------------------------

        options = question["options"].copy()

        # -----------------------------------------------------
        # RANDOMIZE OPTIONS
        # -----------------------------------------------------

        random.shuffle(options)

        # -----------------------------------------------------
        # CREATE NEW OPTIONS
        # -----------------------------------------------------

        for option in options:

            options_column.controls.append(
                create_option(option)
            )

        # -----------------------------------------------------
        # HIDE NEXT BUTTON FOR NEW QUESTION
        # -----------------------------------------------------

        next_button.visible = False

        page.update()

    # =========================================================
    # NEXT QUESTION
    # =========================================================

    def next_question(e):

        nonlocal current_question

        # Do nothing if the user has not answered
        if not answered:
            return

        # -----------------------------------------------------
        # THERE ARE MORE QUESTIONS
        # -----------------------------------------------------

        if current_question < len(questions) - 1:

            current_question += 1

            load_question()

        # -----------------------------------------------------
        # QUIZ FINISHED
        # -----------------------------------------------------

        else:

            show_result()

    next_button.on_click = next_question

    # =========================================================
    # RESULT PAGE
    # =========================================================

    def show_result():

        percentage = int(
            (score / len(questions)) * 100
        )

        # -----------------------------------------------------
        # RESULT MESSAGE
        # -----------------------------------------------------

        if percentage >= 80:

            message = (
                "Excellent! "
                "You know your Bible well."
            )

        elif percentage >= 50:

            message = (
                "Good job! "
                "Keep studying God's Word."
            )

        else:

            message = (
                "Keep learning! "
                "God's Word is worth studying."
            )

        # -----------------------------------------------------
        # CLEAR QUIZ
        # -----------------------------------------------------

        page.controls.clear()

        # -----------------------------------------------------
        # RESULT SCREEN
        # -----------------------------------------------------

        page.add(

            ft.Container(

                expand=True,

                alignment=ft.Alignment(
                    0,
                    0
                ),

                content=ft.Column(

                    horizontal_alignment=(
                        ft.CrossAxisAlignment.CENTER
                    ),

                    spacing=20,

                    controls=[

                        ft.Container(

                            width=90,
                            height=90,

                            bgcolor="#FFF8EC",

                            border_radius=45,

                            alignment=ft.Alignment(
                                0,
                                0
                            ),

                            content=ft.Icon(
                                ft.Icons.MENU_BOOK,
                                color="#C4A46A",
                                size=45
                            )
                        ),

                        ft.Text(
                            "QUIZ COMPLETE",
                            size=13,
                            color="#C4A46A",
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            f"{score} / {len(questions)}",
                            size=48,
                            color="#2B2B2B",
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            f"{percentage}%",
                            size=20,
                            color="#8D7E6B",
                            weight=ft.FontWeight.BOLD
                        ),

                        ft.Text(
                            message,
                            size=15,
                            color="#6F655B",
                            text_align=ft.TextAlign.CENTER,
                            width=280
                        ),

                        ft.Container(
                            height=10
                        ),

                        ft.Button(
                            "PLAY AGAIN",
                            width=190,
                            height=50,
                            color="white",
                            bgcolor="#2B2B2B",

                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(
                                    radius=25
                                )
                            ),

                            on_click=restart_quiz
                        )
                    ]
                )
            )
        )

        page.update()

    # =========================================================
    # RESTART QUIZ
    # =========================================================

    def restart_quiz(e):

        nonlocal current_question
        nonlocal score

        current_question = 0
        score = 0

        random.shuffle(questions)

        page.controls.clear()

        page.add(
            quiz_page()
        )

        load_question()

    # =========================================================
    # QUIZ PAGE
    # =========================================================

    def quiz_page():

        return ft.Column(

            expand=True,

            spacing=0,

            controls=[

                # =================================================
                # HEADER
                # =================================================

                ft.Container(

                    padding=ft.Padding(
                        20,
                        45,
                        20,
                        20
                    ),

                    content=ft.Row(

                        controls=[

                            ft.IconButton(
                                icon=ft.Icons.ARROW_BACK,
                                icon_color="#2B2B2B",
                                icon_size=20,
                                on_click=lambda e: page.navigate("/home")
                            ),

                            ft.Container(
                                expand=True
                            ),

                            ft.Text(
                                "BIBLE QUIZ",
                                size=16,
                                color="#2B2B2B",
                                weight=ft.FontWeight.BOLD
                            ),

                            ft.Container(
                                expand=True
                            ),

                            score_text
                        ]
                    )
                ),

                # =================================================
                # PROGRESS
                # =================================================

                ft.Container(

                    padding=ft.Padding(
                        25,
                        0,
                        25,
                        20
                    ),

                    content=ft.Column(

                        spacing=8,

                        controls=[

                            ft.Row(

                                controls=[

                                    question_number,

                                    ft.Container(
                                        expand=True
                                    )
                                ]
                            ),

                            progress_bar
                        ]
                    )
                ),

                # =================================================
                # QUESTION
                # =================================================

                ft.Container(

                    padding=ft.Padding(
                        25,
                        20,
                        25,
                        20
                    ),

                    content=ft.Column(

                        horizontal_alignment=(
                            ft.CrossAxisAlignment.CENTER
                        ),

                        spacing=15,

                        controls=[

                            ft.Container(

                                width=60,
                                height=60,

                                bgcolor="#FFF8EC",

                                border_radius=30,

                                alignment=ft.Alignment(
                                    0,
                                    0
                                ),

                                content=ft.Icon(
                                    ft.Icons.MENU_BOOK,
                                    color="#C4A46A",
                                    size=28
                                )
                            ),

                            question_text
                        ]
                    )
                ),

                # =================================================
                # ANSWERS
                # =================================================

                ft.Container(

                    padding=ft.Padding(
                        20,
                        10,
                        20,
                        10
                    ),

                    expand=True,

                    content=ft.ListView(

                        spacing=12,

                        controls=[
                            options_column
                        ]
                    )
                ),

                # =================================================
                # FEEDBACK
                # =================================================

                ft.Container(

                    padding=ft.Padding(
                        20,
                        5,
                        20,
                        5
                    ),

                    content=feedback_text
                ),

                # =================================================
                # NEXT BUTTON
                # =================================================

                ft.Container(

                    padding=ft.Padding(
                        20,
                        10,
                        20,
                        25
                    ),

                    alignment=ft.Alignment(
                        0,
                        0
                    ),

                    content=next_button
                )
            ]
        )

    # =========================================================
    # START QUIZ
    # =========================================================

    page.add(
        quiz_page()
    )

    load_question()


# =============================================================
# RUN APP
# =============================================================

