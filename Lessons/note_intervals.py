def note_intervals():
   import tkinter as tk
from tkinter import ttk

# ============================================================
# NOTE INTERVALS — INTERACTIVE AI TUTOR
# 30 QUESTIONS / 6 LEVELS
# ============================================================

QUESTIONS = [

    # =========================
    # LEVEL 1
    # =========================

    {
        "level": 1,
        "title": "Basic Recognition",
        "notes": "C → D",
        "question": "What is the interval?",
        "options": [
            "Major 2nd",
            "Minor 2nd",
            "Major 3rd",
            "Perfect 4th"
        ],
        "answer": 0,
        "feedback": [
            "Correct. C–D contains two letter names, so the interval is a 2nd. C to D is 2 semitones, making it a Major 2nd.",
            "Incorrect. A Minor 2nd contains 1 semitone, such as C → Db. C → D contains 2 semitones, so it is a Major 2nd.",
            "Incorrect. A 3rd spans three letter names. C → E is a 3rd; C → D spans only two.",
            "Incorrect. A 4th spans four letter names, such as C → F. C → D is a 2nd."
        ]
    },

    {
        "level": 1,
        "title": "Basic Recognition",
        "notes": "C → E",
        "question": "What is the interval?",
        "options": [
            "Minor 3rd",
            "Major 3rd",
            "Perfect 4th",
            "Major 2nd"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. C → Eb is a Minor 3rd. C → E is 4 semitones, making it a Major 3rd.",
            "Correct. C–D–E contains three letter names, so it is a 3rd. C → E is 4 semitones, which makes it a Major 3rd.",
            "Incorrect. A Perfect 4th spans four letter names. C → F is a Perfect 4th.",
            "Incorrect. A Major 2nd spans two letter names and 2 semitones, such as C → D."
        ]
    },

    {
        "level": 1,
        "title": "Basic Recognition",
        "notes": "C → F",
        "question": "What is the interval?",
        "options": [
            "Major 3rd",
            "Perfect 4th",
            "Perfect 5th",
            "Minor 3rd"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. C → E is a Major 3rd. C → F spans four letter names.",
            "Correct. C–D–E–F contains four letter names and C → F is 5 semitones, so it is a Perfect 4th.",
            "Incorrect. A Perfect 5th spans five letter names. C → G is a Perfect 5th.",
            "Incorrect. A Minor 3rd contains three letter names and 3 semitones, such as C → Eb."
        ]
    },

    {
        "level": 1,
        "title": "Basic Recognition",
        "notes": "C → G",
        "question": "What is the interval?",
        "options": [
            "Perfect 4th",
            "Major 6th",
            "Perfect 5th",
            "Major 3rd"
        ],
        "answer": 2,
        "feedback": [
            "Incorrect. C → F is a Perfect 4th. C → G spans five letter names.",
            "Incorrect. C → A is a Major 6th. A 6th spans six letter names.",
            "Correct. C–D–E–F–G contains five letter names, and C → G is 7 semitones. That is a Perfect 5th.",
            "Incorrect. C → E is a Major 3rd. C → G spans five letter names."
        ]
    },

    {
        "level": 1,
        "title": "Basic Recognition",
        "notes": "C → C (one octave higher)",
        "question": "What is the interval?",
        "options": [
            "Perfect 5th",
            "Major 7th",
            "Octave",
            "Unison"
        ],
        "answer": 2,
        "feedback": [
            "Incorrect. A Perfect 5th is 7 semitones, such as C → G.",
            "Incorrect. C → B is a Major 7th, which is 11 semitones.",
            "Correct. The same note repeated 12 semitones higher is an octave.",
            "Incorrect. Unison means the notes have the same pitch. Here the second C is one octave higher."
        ]
    },

    # =========================
    # LEVEL 2
    # =========================

    {
        "level": 2,
        "title": "Counting Intervals",
        "notes": "D → F",
        "question": "What is the interval?",
        "options": [
            "Major 3rd",
            "Minor 3rd",
            "Perfect 4th",
            "Major 2nd"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. D → F# is a Major 3rd. D → F is 3 semitones.",
            "Correct. D–E–F gives three letter names, and D → F is 3 semitones. Therefore it is a Minor 3rd.",
            "Incorrect. D → G is a Perfect 4th. A 4th requires four letter names.",
            "Incorrect. D → E is a Major 2nd. D → F spans three letters."
        ]
    },

    {
        "level": 2,
        "title": "Counting Intervals",
        "notes": "E → B",
        "question": "What is the interval?",
        "options": [
            "Perfect 4th",
            "Perfect 5th",
            "Major 6th",
            "Diminished 5th"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. E → A is a Perfect 4th. E → B spans five letter names.",
            "Correct. E–F–G–A–B gives five letter names, and E → B is 7 semitones. That makes it a Perfect 5th.",
            "Incorrect. E → C# is a Major 6th. A 6th requires six letter names.",
            "Incorrect. E → Bb would create a Diminished 5th. E → B is a Perfect 5th."
        ]
    },

    {
        "level": 2,
        "title": "Counting Intervals",
        "notes": "G → C",
        "question": "What is the interval?",
        "options": [
            "Perfect 4th",
            "Perfect 5th",
            "Major 3rd",
            "Minor 6th"
        ],
        "answer": 0,
        "feedback": [
            "Correct. G–A–B–C contains four letter names, and G → C is 5 semitones. That makes it a Perfect 4th.",
            "Incorrect. G → D is a Perfect 5th. G → C contains four letter names.",
            "Incorrect. G → B is a Major 3rd. G → C is a 4th.",
            "Incorrect. A 6th requires six letter names. G → E is a 6th."
        ]
    },

    {
        "level": 2,
        "title": "Counting Intervals",
        "notes": "B → D",
        "question": "What is the interval?",
        "options": [
            "Major 3rd",
            "Minor 3rd",
            "Perfect 4th",
            "Minor 2nd"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. B → D# would be a Major 3rd. B → D is 3 semitones.",
            "Correct. B–C–D gives three letter names, and B → D is 3 semitones. Therefore it is a Minor 3rd.",
            "Incorrect. B → E is a Perfect 4th. B → D spans three letters.",
            "Incorrect. B → C is a Minor 2nd. B → D spans three letter names."
        ]
    },

    {
        "level": 2,
        "title": "Counting Intervals",
        "notes": "F → E (ascending)",
        "question": "What is the interval?",
        "options": [
            "Minor 7th",
            "Major 7th",
            "Minor 2nd",
            "Major 2nd"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. F → Eb is a Minor 7th. When ascending from F to E, you reach the E in the next octave.",
            "Correct. F–G–A–B–C–D–E contains seven letter names, and the ascending distance is 11 semitones. That is a Major 7th.",
            "Incorrect. A Minor 2nd is 1 semitone. The ascending F → E is much larger.",
            "Incorrect. F → G is a Major 2nd. F → E ascending is an octave minus one semitone."
        ]
    },

    # =========================
    # LEVEL 3
    # =========================

    {
        "level": 3,
        "title": "Major, Minor & Perfect",
        "notes": "C → Eb",
        "question": "What is the interval?",
        "options": [
            "Major 3rd",
            "Minor 3rd",
            "Perfect 3rd",
            "Augmented 3rd"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. C → E is a Major 3rd with 4 semitones. Eb is one semitone lower.",
            "Correct. C–D–E gives three letter names, and C → Eb is 3 semitones. Therefore it is a Minor 3rd.",
            "Incorrect. 3rds are part of the major/minor interval family, not the perfect family.",
            "Incorrect. An Augmented 3rd is larger than a Major 3rd. C → Eb is smaller than a Major 3rd."
        ]
    },

    {
        "level": 3,
        "title": "Major, Minor & Perfect",
        "notes": "C → F#",
        "question": "What is the interval?",
        "options": [
            "Perfect 4th",
            "Augmented 4th",
            "Diminished 5th",
            "Major 5th"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. C → F is a Perfect 4th. Raising F to F# adds one semitone.",
            "Correct. C–D–E–F establishes a 4th, and C → F# is 6 semitones. A 4th that is one semitone larger than Perfect is Augmented.",
            "Incorrect for the given spelling. C → Gb would be a Diminished 5th. C → F# is spelled as an Augmented 4th.",
            "Incorrect. A 5th must span five letter names. C → G is a Perfect 5th."
        ]
    },

    {
        "level": 3,
        "title": "Major, Minor & Perfect",
        "notes": "C → Bb",
        "question": "What is the interval?",
        "options": [
            "Major 7th",
            "Minor 7th",
            "Major 6th",
            "Minor 6th"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. C → B is a Major 7th. Lowering B to Bb makes the interval one semitone smaller.",
            "Correct. C–D–E–F–G–A–B gives seven letter names, and C → Bb is 10 semitones. That is a Minor 7th.",
            "Incorrect. C → A is a Major 6th. A 6th spans six letter names.",
            "Incorrect. C → Ab is a Minor 6th. C → Bb spans seven letter names."
        ]
    },

    {
        "level": 3,
        "title": "Major, Minor & Perfect",
        "notes": "E → G#",
        "question": "What is the interval?",
        "options": [
            "Minor 3rd",
            "Major 3rd",
            "Perfect 4th",
            "Major 2nd"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. E → G is a Minor 3rd and contains 3 semitones. Raising G to G# gives 4 semitones.",
            "Correct. E–F–G contains three letter names, and E → G# is 4 semitones. Therefore it is a Major 3rd.",
            "Incorrect. E → A is a Perfect 4th. E → G# spans only three letter names.",
            "Incorrect. E → F# is a Major 2nd. E → G# is a 3rd."
        ]
    },

    {
        "level": 3,
        "title": "Major, Minor & Perfect",
        "notes": "A → Eb",
        "question": "What is the interval?",
        "options": [
            "Perfect 5th",
            "Diminished 5th",
            "Augmented 4th",
            "Major 5th"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. A → E is a Perfect 5th. Lowering E to Eb reduces the interval by one semitone.",
            "Correct. A–B–C–D–E gives five letter names, and A → Eb is 6 semitones. A Perfect 5th is 7 semitones, so this is a Diminished 5th.",
            "Incorrect by spelling. A → Eb is written as a 5th. An Augmented 4th would have four letter names.",
            "Incorrect. 5ths belong to the Perfect family and are not called Major 5ths."
        ]
    },

    # =========================
    # LEVEL 4
    # =========================

    {
        "level": 4,
        "title": "Accidentals & Direction",
        "notes": "F# → A",
        "question": "What is the interval?",
        "options": [
            "Major 3rd",
            "Minor 3rd",
            "Perfect 4th",
            "Major 2nd"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. F# → A# is a Major 3rd. F# → A is 3 semitones.",
            "Correct. F#–G–A contains three letter names, and F# → A is 3 semitones. That makes it a Minor 3rd.",
            "Incorrect. A 4th needs four letter names. F# → B is a Perfect 4th.",
            "Incorrect. F# → G# is a Major 2nd. F# → A is a 3rd."
        ]
    },

    {
        "level": 4,
        "title": "Accidentals & Direction",
        "notes": "Bb → E",
        "question": "What is the interval?",
        "options": [
            "Perfect 4th",
            "Augmented 4th",
            "Diminished 5th",
            "Perfect 5th"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. Bb → Eb is a Perfect 4th. Raising Eb to E adds one semitone.",
            "Correct. Bb–C–D–E gives four letter names, and Bb → E is 6 semitones. A Perfect 4th is 5 semitones, so this is an Augmented 4th.",
            "Incorrect by spelling. Bb → E is a 4th, not a 5th.",
            "Incorrect. A 5th requires five letter names. Bb → F is a 5th."
        ]
    },

    {
        "level": 4,
        "title": "Accidentals & Direction",
        "notes": "C# → A (ascending)",
        "question": "What is the interval?",
        "options": [
            "Minor 6th",
            "Major 6th",
            "Minor 3rd",
            "Major 3rd"
        ],
        "answer": 0,
        "feedback": [
            "Correct. C#–D–E–F–G–A contains six letter names. C# → A is 8 semitones, which is a Minor 6th.",
            "Incorrect. A Major 6th contains 9 semitones. C# → A is 8 semitones, one semitone smaller.",
            "Incorrect. A Minor 3rd spans three letter names. C# → A spans six.",
            "Incorrect. C# → E# is a Major 3rd. C# → A is a 6th."
        ]
    },

    {
        "level": 4,
        "title": "Accidentals & Direction",
        "notes": "G → Db",
        "question": "What is the interval?",
        "options": [
            "Perfect 5th",
            "Diminished 5th",
            "Augmented 4th",
            "Major 5th"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. G → D is a Perfect 5th. Lowering D to Db makes the interval one semitone smaller.",
            "Correct. G–A–B–C–D gives five letter names, while G → Db is 6 semitones. A Perfect 5th is 7 semitones, so this is a Diminished 5th.",
            "Incorrect by spelling. G → Db is written as a 5th. G → C# would be an Augmented 4th.",
            "Incorrect. 5ths belong to the Perfect family, so they are not called Major 5ths."
        ]
    },

    {
        "level": 4,
        "title": "Accidentals & Direction",
        "notes": "Ab → F (ascending)",
        "question": "What is the interval?",
        "options": [
            "Major 6th",
            "Minor 6th",
            "Major 3rd",
            "Minor 3rd"
        ],
        "answer": 0,
        "feedback": [
            "Correct. Ab–Bb–C–D–Eb–F gives six letter names. Ab → F is 9 semitones, which makes it a Major 6th.",
            "Incorrect. A Minor 6th contains 8 semitones. Ab → F is 9 semitones.",
            "Incorrect. Ab → C is a Major 3rd. Ab → F spans six letter names.",
            "Incorrect. A Minor 3rd spans three letter names and 3 semitones. Ab → F is much larger."
        ]
    },

    # =========================
    # LEVEL 5
    # =========================

    {
        "level": 5,
        "title": "Advanced Analysis",
        "notes": "D# → C (ascending)",
        "question": "What is the interval?",
        "options": [
            "Minor 7th",
            "Major 7th",
            "Diminished 7th",
            "Augmented 6th"
        ],
        "answer": 2,
        "feedback": [
            "Incorrect. D# → C# is a Minor 7th. D# → C is one semitone smaller.",
            "Incorrect. A Major 7th contains 11 semitones. D# → C is 10 semitones.",
            "Correct. This is an advanced spelling problem. D#–E–F–G–A–B–C gives seven letter names, and the unusual spelling changes the theoretical quality.",
            "Incorrect. An Augmented 6th is spelled as a 6th. Here the written interval is a 7th."
        ]
    },

    {
        "level": 5,
        "title": "Advanced Analysis",
        "notes": "Eb → B",
        "question": "What is the interval?",
        "options": [
            "Perfect 5th",
            "Augmented 5th",
            "Diminished 5th",
            "Major 5th"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. Eb → Bb is a Perfect 5th. Raising Bb to B adds one semitone.",
            "Correct. Eb–F–G–A–B contains five letter names. Eb → B is 8 semitones, one more than a Perfect 5th, so it is an Augmented 5th.",
            "Incorrect. A Diminished 5th is one semitone smaller than a Perfect 5th. Eb → B is one semitone larger.",
            "Incorrect. 5ths are part of the Perfect family, so the standard quality names are Perfect, Diminished, and Augmented."
        ]
    },

    {
        "level": 5,
        "title": "Advanced Analysis",
        "notes": "F# → C",
        "question": "What is the interval?",
        "options": [
            "Perfect 5th",
            "Diminished 5th",
            "Augmented 4th",
            "Major 5th"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. F# → C# is a Perfect 5th. Lowering C# to C reduces the distance by one semitone.",
            "Correct. F#–G–A–B–C contains five letter names. F# → C is 6 semitones, one less than the 7-semitone Perfect 5th, so it is a Diminished 5th.",
            "Incorrect by spelling. F# → C contains five letter names, so the interval number is 5.",
            "Incorrect. 5ths are not described as Major or Minor. This one is Diminished."
        ]
    },

    {
        "level": 5,
        "title": "Advanced Analysis",
        "notes": "Bb → C#",
        "question": "What is the interval?",
        "options": [
            "Major 2nd",
            "Minor 2nd",
            "Augmented 2nd",
            "Diminished 3rd"
        ],
        "answer": 2,
        "feedback": [
            "Incorrect. Bb → C is a Major 2nd and contains 2 semitones. Bb → C# contains 3 semitones.",
            "Incorrect. A Minor 2nd contains 1 semitone. Bb → C# is larger.",
            "Correct. Bb–C contains two letter names, so the interval number is 2. Bb → C# is 3 semitones. Since a Major 2nd is 2 semitones, this is an Augmented 2nd.",
            "Incorrect. Bb → C# is spelled using two letter names, Bb–C, so it is a 2nd rather than a 3rd."
        ]
    },

    {
        "level": 5,
        "title": "Advanced Analysis",
        "notes": "C → B#",
        "question": "What is the interval?",
        "options": [
            "Major 7th",
            "Augmented 7th",
            "Perfect octave",
            "Minor 7th"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. C → B is a Major 7th. Raising B to B# makes the interval one semitone larger.",
            "Correct. C–D–E–F–G–A–B gives seven letter names, so the interval is a 7th. B# is one semitone above B, making C → B# an Augmented 7th.",
            "Incorrect by spelling. C → C is an octave. Even though B# sounds like C, the written interval is a 7th.",
            "Incorrect. C → Bb is a Minor 7th. C → B# is larger than a Major 7th."
        ]
    },

    # =========================
    # LEVEL 6
    # =========================

    {
        "level": 6,
        "title": "Expert Challenge",
        "notes": "Ab → C#",
        "question": "What is the interval?",
        "options": [
            "Major 3rd",
            "Augmented 3rd",
            "Minor 4th",
            "Perfect 4th"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. Ab → C is a Major 3rd. Raising C to C# makes the interval one semitone larger.",
            "Correct. Ab–Bb–C contains three letter names, establishing a 3rd. Ab → C is a Major 3rd; C# is one semitone higher, so Ab → C# is an Augmented 3rd.",
            "Incorrect. The letter names Ab–Bb–C establish a 3rd, not a 4th.",
            "Incorrect. A Perfect 4th would contain four letter names, such as Ab → Db."
        ]
    },

    {
        "level": 6,
        "title": "Expert Challenge",
        "notes": "Fb → Bb",
        "question": "What is the interval?",
        "options": [
            "Perfect 4th",
            "Augmented 4th",
            "Diminished 5th",
            "Perfect 5th"
        ],
        "answer": 0,
        "feedback": [
            "Correct. Fb–Gb–Ab–Bb contains four letter names. Fb → Bb is 5 semitones, so it is a Perfect 4th.",
            "Incorrect. An Augmented 4th contains 6 semitones. Fb → Bb contains 5.",
            "Incorrect by spelling. Fb → Bb spans four letter names, so it is a 4th rather than a 5th.",
            "Incorrect. A Perfect 5th requires five letter names. Fb → Cb would be a Perfect 5th."
        ]
    },

    {
        "level": 6,
        "title": "Expert Challenge",
        "notes": "C# → Gb",
        "question": "What is the interval?",
        "options": [
            "Perfect 5th",
            "Diminished 5th",
            "Augmented 4th",
            "Major 5th"
        ],
        "answer": 1,
        "feedback": [
            "Incorrect. C# → G# is a Perfect 5th. C# → Gb is smaller by one semitone.",
            "Correct. C#–D–E–F–G gives five letter names, establishing a 5th. C# → Gb is 6 semitones, so it is a Diminished 5th.",
            "Incorrect for the written spelling. Although an enharmonic equivalent can sound like an Augmented 4th, C# → Gb is spelled as a 5th.",
            "Incorrect. 5ths belong to the Perfect family, so they are not called Major 5ths."
        ]
    },

    {
        "level": 6,
        "title": "Expert Challenge",
        "notes": "B# → Ab",
        "question": "What is the interval when ascending?",
        "options": [
            "Minor 7th",
            "Major 7th",
            "Diminished 7th",
            "Augmented 6th"
        ],
        "answer": 2,
        "feedback": [
            "Incorrect. A Minor 7th contains 10 semitones, but interval spelling must also be considered.",
            "Incorrect. A Major 7th contains 11 semitones. This question is testing the effect of unusual note spelling.",
            "Correct for the intended theoretical spelling. The notes are written as a 7th relationship, and the unusual accidentals make this an advanced enharmonic-spelling problem.",
            "Incorrect. An Augmented 6th is spelled as a 6th. Here the intended theoretical classification is a 7th."
        ]
    },

    {
        "level": 6,
        "title": "Expert Challenge",
        "notes": "Gb → E#",
        "question": "What is the interval when ascending?",
        "options": [
            "Major 6th",
            "Minor 6th",
            "Augmented 6th",
            "Diminished 7th"
        ],
        "answer": 2,
        "feedback": [
            "Incorrect. Gb → Eb is a Major 6th. The E# spelling changes the theoretical interval.",
            "Incorrect. A Minor 6th contains 8 semitones and is spelled as a 6th with the appropriate accidental.",
            "Correct. The unusual enharmonic notation means the interval must be analyzed from the written note names rather than simply treating E# as F.",
            "Incorrect for the intended spelling. This question is designed to challenge the distinction between enharmonic equivalents and interval spelling."
        ]
    }
]


# ============================================================
# APPLICATION
# ============================================================

class IntervalTutor:

    def __init__(self, root):

        self.root = root

        self.root.title("Note Intervals — Interactive AI Tutor")
        self.root.geometry("1000x720")
        self.root.minsize(850, 620)

        # COLORS
        self.bg = "#0f172a"
        self.card = "#1e293b"
        self.card2 = "#334155"
        self.text = "#f8fafc"
        self.muted = "#94a3b8"
        self.accent = "#60a5fa"
        self.correct = "#22c55e"
        self.incorrect = "#ef4444"

        self.root.configure(bg=self.bg)

        # STATE
        self.question_index = 0
        self.score = 0
        self.answered = False

        self.level_scores = {
            1: [0, 0],
            2: [0, 0],
            3: [0, 0],
            4: [0, 0],
            5: [0, 0],
            6: [0, 0]
        }

        self.build_styles()
        self.show_welcome()

    # --------------------------------------------------------
    # STYLES
    # --------------------------------------------------------

    def build_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Progress.Horizontal.TProgressbar",
            troughcolor=self.card,
            background=self.accent,
            bordercolor=self.card,
            lightcolor=self.accent,
            darkcolor=self.accent
        )

    # --------------------------------------------------------
    # CLEAR SCREEN
    # --------------------------------------------------------

    def clear(self):

        for widget in self.root.winfo_children():
            widget.destroy()

    # --------------------------------------------------------
    # LABEL HELPER
    # --------------------------------------------------------

    def make_label(
        self,
        parent,
        text,
        size=14,
        weight="normal",
        color=None
    ):

        return tk.Label(
            parent,
            text=text,
            font=("Segoe UI", size, weight),
            fg=color or self.text,
            bg=parent.cget("bg")
        )

    # --------------------------------------------------------
    # WELCOME SCREEN
    # --------------------------------------------------------

    def show_welcome(self):

        self.clear()

        container = tk.Frame(
            self.root,
            bg=self.bg
        )

        container.pack(
            fill="both",
            expand=True,
            padx=80,
            pady=50
        )

        self.make_label(
            container,
            "NOTE INTERVALS",
            15,
            "bold",
            self.accent
        ).pack(pady=(10, 8))

        self.make_label(
            container,
            "Interactive AI Tutor",
            34,
            "bold"
        ).pack()

        self.make_label(
            container,
            "Learn to identify the distance and quality between notes.",
            16,
            color=self.muted
        ).pack(pady=(10, 35))

        card = tk.Frame(
            container,
            bg=self.card,
            padx=35,
            pady=30
        )

        card.pack(
            fill="x",
            padx=40
        )

        self.make_label(
            card,
            "The Core Strategy",
            21,
            "bold"
        ).pack(anchor="w")

        strategy = (
            "1. Count the letter names → determine the interval number.\n\n"
            "2. Count the semitones → determine the interval quality.\n\n"
            "3. Combine both → name the complete interval."
        )

        tk.Label(
            card,
            text=strategy,
            font=("Segoe UI", 14),
            fg=self.muted,
            bg=self.card,
            justify="left"
        ).pack(
            anchor="w",
            pady=(15, 25)
        )

        self.make_label(
            card,
            "Example:  C → E",
            18,
            "bold"
        ).pack(anchor="w")

        example = (
            "C–D–E = 3rd\n"
            "C → E = 4 semitones\n"
            "Therefore: Major 3rd"
        )

        tk.Label(
            card,
            text=example,
            font=("Segoe UI", 14),
            fg=self.muted,
            bg=self.card,
            justify="left"
        ).pack(
            anchor="w",
            pady=(10, 0)
        )

        self.make_label(
            container,
            "6 levels • 30 questions • Detailed explanations",
            13,
            color=self.muted
        ).pack(pady=25)

        start_button = tk.Button(
            container,
            text="Start Course",
            command=self.start_course,
            font=("Segoe UI", 15, "bold"),
            fg=self.bg,
            bg=self.accent,
            activebackground=self.accent,
            activeforeground=self.bg,
            relief="flat",
            padx=35,
            pady=13,
            cursor="hand2"
        )

        start_button.pack()

    # --------------------------------------------------------
    # START
    # --------------------------------------------------------

    def start_course(self):

        self.question_index = 0
        self.score = 0
        self.answered = False

        self.level_scores = {
            1: [0, 0],
            2: [0, 0],
            3: [0, 0],
            4: [0, 0],
            5: [0, 0],
            6: [0, 0]
        }

        self.show_question()

    # --------------------------------------------------------
    # QUESTION SCREEN
    # --------------------------------------------------------

    def show_question(self):

        self.clear()

        self.answered = False

        q = QUESTIONS[self.question_index]

        level = q["level"]

        number = self.question_index + 1

        outer = tk.Frame(
            self.root,
            bg=self.bg
        )

        outer.pack(
            fill="both",
            expand=True,
            padx=55,
            pady=30
        )

        # HEADER

        header = tk.Frame(
            outer,
            bg=self.bg
        )

        header.pack(fill="x")

        self.make_label(
            header,
            f"LEVEL {level} • {q['title']}",
            12,
            "bold",
            self.accent
        ).pack(side="left")

        self.make_label(
            header,
            f"{number} / {len(QUESTIONS)}",
            12,
            color=self.muted
        ).pack(side="right")

        # PROGRESS BAR

        progress = ttk.Progressbar(
            outer,
            style="Progress.Horizontal.TProgressbar",
            maximum=len(QUESTIONS),
            value=number
        )

        progress.pack(
            fill="x",
            pady=(12, 25)
        )

        # QUESTION CARD

        card = tk.Frame(
            outer,
            bg=self.card,
            padx=35,
            pady=30
        )

        card.pack(
            fill="both",
            expand=True
        )

        self.make_label(
            card,
            "IDENTIFY THE INTERVAL",
            13,
            "bold",
            self.muted
        ).pack()

        self.make_label(
            card,
            q["notes"],
            34,
            "bold"
        ).pack(
            pady=(8, 8)
        )

        self.make_label(
            card,
            q["question"],
            17
        ).pack(
            pady=(0, 22)
        )

        # OPTIONS

        self.option_frame = tk.Frame(
            card,
            bg=self.card
        )

        self.option_frame.pack(fill="x")

        self.option_buttons = []

        for i, option in enumerate(q["options"]):

            button = tk.Button(
                self.option_frame,
                text=f"{chr(65+i)}) {option}",
                command=lambda index=i: self.select_answer(index),
                font=("Segoe UI", 13),
                fg=self.text,
                bg=self.card2,
                activebackground=self.card2,
                activeforeground=self.text,
                relief="flat",
                anchor="w",
                padx=18,
                pady=13,
                cursor="hand2"
            )

            button.pack(
                fill="x",
                pady=5
            )

            self.option_buttons.append(button)

        # FEEDBACK

        self.feedback_label = tk.Label(
            card,
            text="",
            font=("Segoe UI", 12),
            fg=self.text,
            bg=self.card,
            justify="left",
            wraplength=820
        )

        self.feedback_label.pack(
            fill="x",
            pady=(20, 10)
        )

        # BOTTOM BAR

        bottom = tk.Frame(
            outer,
            bg=self.bg
        )

        bottom.pack(
            fill="x",
            pady=(18, 0)
        )

        self.score_label = self.make_label(
            bottom,
            f"Score: {self.score}/{number-1}",
            12,
            color=self.muted
        )

        self.score_label.pack(side="left")

        self.next_button = tk.Button(
            bottom,
            text="Next Question",
            command=self.next_question,
            font=("Segoe UI", 12, "bold"),
            fg=self.bg,
            bg=self.accent,
            activebackground=self.accent,
            activeforeground=self.bg,
            relief="flat",
            padx=25,
            pady=10,
            cursor="hand2",
            state="disabled"
        )

        self.next_button.pack(side="right")

    # --------------------------------------------------------
    # SELECT ANSWER
    # --------------------------------------------------------

    def select_answer(self, index):

        if self.answered:
            return

        self.answered = True

        q = QUESTIONS[self.question_index]

        correct = index == q["answer"]

        # Update attempts

        self.level_scores[q["level"]][1] += 1

        if correct:

            self.score += 1

            self.level_scores[q["level"]][0] += 1

        # Disable buttons

        for i, button in enumerate(self.option_buttons):

            button.configure(
                state="disabled"
            )

            # Correct answer
            if i == q["answer"]:

                button.configure(
                    bg=self.correct,
                    fg="#052e16",
                    activebackground=self.correct
                )

            # User's incorrect choice
            elif i == index:

                button.configure(
                    bg=self.incorrect,
                    fg="#450a0a",
                    activebackground=self.incorrect
                )

        # Explanation

        if correct:

            prefix = "Correct."

            color = self.correct

        else:

            prefix = "Incorrect."

            color = self.incorrect

        explanation = q["feedback"][index]

        self.feedback_label.configure(
            text=prefix + " " + explanation,
            fg=color
        )

        # Enable next

        self.next_button.configure(
            state="normal"
        )

        self.score_label.configure(
            text=f"Score: {self.score}/{self.question_index + 1}"
        )

    # --------------------------------------------------------
    # NEXT QUESTION
    # --------------------------------------------------------

    def next_question(self):

        if self.question_index >= len(QUESTIONS) - 1:

            self.show_results()

        else:

            self.question_index += 1

            self.show_question()

    # --------------------------------------------------------
    # RESULTS
    # --------------------------------------------------------

    def show_results(self):

        self.clear()

        outer = tk.Frame(
            self.root,
            bg=self.bg
        )

        outer.pack(
            fill="both",
            expand=True,
            padx=70,
            pady=45
        )

        self.make_label(
            outer,
            "COURSE COMPLETE",
            14,
            "bold",
            self.accent
        ).pack()

        self.make_label(
            outer,
            f"{self.score} / {len(QUESTIONS)}",
            46,
            "bold"
        ).pack(
            pady=(8, 0)
        )

        percentage = (
            self.score /
            len(QUESTIONS)
        ) * 100

        if percentage >= 90:

            message = (
                "Excellent work. You have demonstrated "
                "strong command of interval identification."
            )

        elif percentage >= 75:

            message = (
                "Strong performance. Review the explanations "
                "for the questions you missed."
            )

        elif percentage >= 60:

            message = (
                "Good foundation. More practice with interval "
                "quality will strengthen your accuracy."
            )

        else:

            message = (
                "You have started building the foundation. "
                "Review the core strategy and try again."
            )

        tk.Label(
            outer,
            text=message,
            font=("Segoe UI", 15),
            fg=self.muted,
            bg=self.bg,
            wraplength=750,
            justify="center"
        ).pack(
            pady=(10, 30)
        )

        # PERFORMANCE CARD

        card = tk.Frame(
            outer,
            bg=self.card,
            padx=30,
            pady=25
        )

        card.pack(fill="x")

        self.make_label(
            card,
            "Performance by Level",
            18,
            "bold"
        ).pack(
            anchor="w",
            pady=(0, 15)
        )

        level_names = {
            1: "Basic Recognition",
            2: "Counting Intervals",
            3: "Major, Minor & Perfect",
            4: "Accidentals & Direction",
            5: "Advanced Analysis",
            6: "Expert Challenge"
        }

        for level in range(1, 7):

            correct, attempted = self.level_scores[level]

            percentage = (
                correct / attempted * 100
                if attempted
                else 0
            )

            row = tk.Frame(
                card,
                bg=self.card
            )

            row.pack(
                fill="x",
                pady=6
            )

            self.make_label(
                row,
                f"Level {level}: {level_names[level]}",
                12
            ).pack(side="left")

            self.make_label(
                row,
                f"{correct}/5 ({percentage:.0f}%)",
                12,
                color=self.muted
            ).pack(side="right")

        # BUTTONS

        buttons = tk.Frame(
            outer,
            bg=self.bg
        )

        buttons.pack(
            pady=25
        )

        tk.Button(
            buttons,
            text="Try Again",
            command=self.start_course,
            font=("Segoe UI", 12, "bold"),
            fg=self.bg,
            bg=self.accent,
            activebackground=self.accent,
            relief="flat",
            padx=25,
            pady=10,
            cursor="hand2"
        ).pack(
            side="left",
            padx=7
        )

        tk.Button(
            buttons,
            text="Exit",
            command=self.root.destroy,
            font=("Segoe UI", 12),
            fg=self.text,
            bg=self.card2,
            activebackground=self.card2,
            relief="flat",
            padx=25,
            pady=10,
            cursor="hand2"
        ).pack(
            side="left",
            padx=7
        )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = IntervalTutor(root)

    root.mainloop()