"""
=====================================================================
  EVERYTHING you edit lives in THIS file.  Then run:   python3 build.py
  (or just edit this file on github.com - the Action rebuilds for you)

  Rules of thumb
   - ALL CAPS text only (pixel font: caps, digits and . , - : / + > < ! ? ( ) = * % # _ [ ] @)
   - Empty string ""  =  that row / button / line is hidden
   - Length limits are in the comments. Build prints a WARNING if something overflows.
=====================================================================
"""

# ---------------------------------------------------------------- 0. IDENTITY
HANDLE = "V1HAAN24"                       # title screen + used for GitHub fetches (lowercased)
NAME   = ("VIHAAN", "JAIN")               # big 2-line name on the title screen
CLASS  = "CURIOUS BY NATURE"               # tagline under the name

# ---------------------------------------------------------------- 1. PROFILE PICTURE (green dot-matrix avatar)
AVATAR_SOURCE   = "github"      # "github" = live github.com/<HANDLE>.png | "avatar.png" = local file | "" = no avatar (pixel sprite)
AVATAR_BIG_PX   = 32            # pixel grid on SELECT PLAYER screen (24 / 32 / 40)
AVATAR_SMALL_PX = 22            # pixel grid on the profile screen   (18 / 22 / 26)
AVATAR_CONTRAST = 1.35          # 1.0 = untouched, higher = punchier
AVATAR_BRIGHT   = 1.05          # 1.0 = untouched
AVATAR_DITHER   = "bayer"       # "bayer" (checker, most Game-Boy-like) | "none" (flat) | "floyd" (smooth)
AVATAR_INVERT   = False         # True = swap light/dark
AVATAR_ZOOM     = 1.0           # >1 crops in on the face (1.25 = tighter)
AVATAR_DOTS     = False         # True = each pixel is a small gapped dot (more LCD look, bigger svg)
SELECT_AVATAR_BOX = 64          # avatar box size (LCD px) on select screen
SELECT_TAG        = "VJ"        # initials shown on the avatar slot

# ---------------------------------------------------------------- 2. THEME / COLOURS (hex)
THEME   = ("#9bbc0f", "#8bac0f", "#306230", "#0f380f")   # LCD lightest -> darkest. mint: ("#c7f0d8","#8bc2a0","#35705a","#0b2e22")
SHELL_TOP, SHELL_BOT = "#dcd9cd", "#bdbaad"              # console body gradient
BEZEL   = "#55536a"                                      # dark screen frame
BTN_A, BTN_B = "#d4477d", "#8a1c4a"                      # A/B button gradient
SHELL_TEXT = "DOT MATRIX WITH STEREO SOUND"              # text on the bezel (<=34 chars)

# ---------------------------------------------------------------- 3. CONSOLE LCD TEXTS
TXT = dict(
    presents   = "PRESENTS",              # "<HANDLE> PRESENTS"
    press      = "PRESS START",
    copyright  = "(C) 2026",              # followed by HANDLE
    menu_title = "MAIN MENU",  menu_ver = "V1.0",
    menu_hint  = "D-PAD:MOVE   A:SELECT",
    select_title = "SELECT PLAYER", select_count = "1/1",
    select_hint  = "A:LOAD   B:BACK",
    select_menu  = "QUICK MENU",
    loading_top = "LOADING PROFILE", loading_name = "VIHAAN JAIN", loading_wait = "PLEASE WAIT...",
    detail_title = "ABOUT USER", detail_status = "ONLINE",
    detail_hint  = "B:BACK   SCROLL DOWN V",
)
MENU = ["NEW GAME", "CONTINUE", "PROFILES", "OPTIONS"]           # <=10 chars each, exactly 4

# ---- select-player: one player card + a QUICK MENU row of icon tiles underneath (the sections below the console)
SELECT_NAME = "VIHAAN JAIN"               # <=13 chars
SELECT_SUB  = ["VJTI / YEAR 2 / IT",     # up to 4 small lines (<=24 chars each)
               "CYBERSECURITY MINOR"]
# (label <=8 chars, icon: cart | chest | trophy | mail). Empty list [] = no tiles. 2-5 tiles fit nicely.
SELECT_TILES = [("PROJECTS", "cart"), ("LOADOUT", "chest"), ("HI-SCORE", "trophy"), ("CONTACT", "mail")]

# ---- profile LCD (opens after LOAD). label <=7 chars, value <=18 chars
PLAYER = [
    ("NAME", "VIHAAN JAIN"),
    ("GUILD", "VJTI - 2ND YEAR"),
    ("LVL", "IT/CYBERSEC MINOR"),
]
BIO    = ["I BUILD THINGS THAT CATCH MY", "CURIOSITY AND SOLVE PROBLEMS."]   # lines <=32 chars
# label <=7 chars, value <=26 chars. Special labels: "@LOAD" = animated loading icon, "@BAL" = balance-scales icon
KV     = [("LEARNING",  "AI/ML, SYSTEMS"),
          ("EXPLORING", "CYBERSEC, NETWORKS, COMMS"),
          ("BUILDING",  "MEMORADB + DAWN"),
          ("VIBE",      "LEARN DEEP, STAY PLAYFUL"),
          ("SIDE QUEST","DSA/CP, EXPLORE THE WORLD")]
AVATAR_CAPTION = "VJ"                     # initials under avatar on profile screen

# ---------------------------------------------------------------- 4. README SECTIONS
# Each header is an SVG bar. The plain text for that section lives in a CLOSED drop-down whose <summary>
# IS the header image -> AI/text scanners can read it, humans just see the arcade UI.
# (key, tag(<=8 chars), title(<=14 chars), show?)
SECTIONS = [("profile",  "ABOUT ME", "VIHAAN JAIN", True),
            ("projects", "PROJECTS", "THE COLLECTION", True),
            ("stack",    "LOADOUT", "EQUIPPED GEAR", True),
            ("score",    "HI-SCORE", "ACTIVITY LOG", True),
            ("contact",  "CONTACT", "SAY HELLO",   True)]
HDR_HEIGHT = 36            # header bar height px (smaller = slimmer)
HDR_SCALE  = 2             # header text size (1-3)
HDR_ARROW  = "V"           # blinking hint on the right ("" = none)

# render width of each block in README (CSS %). Lower = smaller on screen. button = height in px
WIDTHS = dict(header="82%", console="78%", cart="88%", stack="70%", activity="78%", button=40)
CAP_LINE = False           # qualification is displayed prominently in the About Me section

# ---------------------------------------------------------------- 5. PROJECTS (cartridges)
# file, cart title(<=16), cart l1(<=16), cart l2(<=16), label colour, icon(db|chip|graph|net|maze|cal|dawn), repo ("" = locked),
# plate line1(<=21), plate line2(<=21), tech chips, plain-text description (README dropdown),
# cart blurb (CAPS pixel text, wraps to <=5 lines of ~40 chars - Build warns if longer; full text stays in the dropdown)
PROJECTS = [
 ("memoradb", "MEMORADB", "TEMPORAL DBMS", "C++ / SEMANTIC SEARCH", "#2f6bd0", "db", "MemoraDB",
  "A DATABASE WITH", "A MEMORY OF TIME", ["C++17", "CMAKE", "ONNX RUNTIME", "MINILM-L6"],
  "MemoraDB is a C++17 temporal and semantic DBMS built from scratch. It stores changes as immutable, append-only binary versions instead of overwriting records. It supports time-travel queries, snapshots, rollback, temporal indexing and diffs. Semantic columns can be embedded locally with ONNX Runtime and the all-MiniLM-L6-v2 model. A SQL-like query engine brings historical queries and semantic search together.",
  "C++17 TEMPORAL AND SEMANTIC DBMS BUILT FROM SCRATCH. IMMUTABLE, APPEND-ONLY VERSIONS. TIME-TRAVEL QUERIES, SNAPSHOTS, ROLLBACK, DIFFS. LOCAL ONNX EMBEDDINGS. SQL-LIKE QUERY ENGINE."),
 ("predictive-maintenance", "PREDICTIVE MAINT.", "ENGINE HEALTH", "LSTM / NASA CMAPSS", "#2f806d", "graph", "Predictive-Maintenance-System",
  "PREDICT REMAINING", "ENGINE LIFE", ["PYTHON", "TENSORFLOW", "KERAS", "NUMPY", "PANDAS", "SCIKIT-LEARN"],
  "A deep-learning predictive-maintenance pipeline built around the NASA CMAPSS FD001 engine dataset. It preprocesses multivariate sensor readings and converts them into fixed-length time-series sequences. An LSTM model estimates Remaining Useful Life (RUL), rather than simply classifying an engine as failed or healthy. The training pipeline uses early stopping and evaluates predictions with RMSE. It also saves the trained model, produces training-loss visualisations and generates rule-based maintenance recommendations.",
  "LSTM PIPELINE ON NASA CMAPSS FD001 DATA. TURNS SENSOR READINGS INTO TIME-SERIES SEQUENCES. ESTIMATES REMAINING USEFUL LIFE (RUL), EVALUATED WITH RMSE. RULE-BASED MAINTENANCE TIPS."),
 ("attendance-tracker", "ATTENDANCE", "STUDENT TOOL", "HTML / CSS / JS", "#8a7d32", "cal", "Attendance-Tracker",
  "TRACK CLASSES", "PLAN SAFE BUNKS", ["HTML5", "CSS3", "JAVASCRIPT", "LOCALSTORAGE"],
  "A lightweight attendance manager designed around the everyday student workflow. It lets students mark and edit daily attendance, organise a weekly timetable and inspect subject-wise and overall statistics. A bunk calculator helps estimate how many classes can be missed while staying above a target attendance percentage. Low-attendance alerts make it easier to spot subjects that need attention. The app runs entirely in the browser using LocalStorage, with no backend or database.",
  "BROWSER-BASED ATTENDANCE MANAGER. MARK AND EDIT DAILY ATTENDANCE, ORGANISE A WEEKLY TIMETABLE, VIEW SUBJECT STATS. BUNK CALCULATOR AND LOW-ATTENDANCE ALERTS. NO BACKEND, USES LOCALSTORAGE."),
 ("dawn", "DAWN", "NETWORKING PROJECT", "IN DEVELOPMENT", "#34344a", "dawn", "",
  "SIGNAL INCOMING", "DETAILS CLASSIFIED", ["NETWORKING", "IN PROGRESS"],
  "A networking project currently in development. Keeping the details under wraps until it is ready.",
  "A NETWORKING PROJECT CURRENTLY IN DEVELOPMENT. KEEPING THE DETAILS UNDER WRAPS UNTIL IT IS READY.")
]
EMPTY_SLOTS = 2      # empty "insert cartridge" placeholders after the projects (grid is 3 columns wide)
PROJECTS_NOTE = ""   # cartridge labels are self-explanatory; no extra footer

# ---------------------------------------------------------------- 6. TECH STACK (category, items)
# Items are ALL CAPS. Keep to what you actually use. Loadout LCD fits 5 categories / ~25 items.
STACK = [("LANGUAGES",          ["C", "C++", "PYTHON", "JAVA", "JAVASCRIPT", "TYPESCRIPT"]),
         ("FRONTEND",           ["HTML", "CSS", "REACT", "NEXT.JS", "TAILWIND CSS"]),
         ("BACKEND & DATABASES",["MONGODB", "SQLITE"]),
         ("TOOLS & PLATFORMS",  ["GIT", "GITHUB", "DOCKER", "LINUX", "VERCEL"]),
         ("AI/ML & DATA",       ["NUMPY", "PANDAS", "SCIKIT-LEARN", "TENSORFLOW", "KERAS", "PYTORCH", "KAGGLE"])]
# short label shown on the LCD (<=9 chars; the pixel font has no & so the full name is used in the README text)
STACK_SHORT = {"LANGUAGES": "LANGUAGES", "FRONTEND": "FRONTEND", "BACKEND & DATABASES": "BACKEND/DB",
               "TOOLS & PLATFORMS": "TOOLS", "AI/ML & DATA": "ML+DATA"}
# LCD chip badge: item -> (monogram <=2 chars, brand colour, monogram colour). Brand colours only - not official logos.
STACK_BRAND = {"C": ("C", "#A8B9CC", "#0f380f"), "C++": ("++", "#00599C", "#ffffff"), "PYTHON": ("PY", "#3776AB", "#FFD43B"),
    "JAVA": ("JV", "#ED8B00", "#ffffff"), "JAVASCRIPT": ("JS", "#F7DF1E", "#0f380f"), "TYPESCRIPT": ("TS", "#3178C6", "#ffffff"),
    "HTML": ("H5", "#E34F26", "#ffffff"), "CSS": ("C3", "#1572B6", "#ffffff"), "REACT": ("RE", "#61DAFB", "#0f380f"),
    "NEXT.JS": ("N", "#111111", "#ffffff"), "TAILWIND CSS": ("TW", "#06B6D4", "#ffffff"),
    "MONGODB": ("MG", "#47A248", "#ffffff"), "SQLITE": ("SQ", "#0F80CC", "#ffffff"),
    "GIT": ("GI", "#F05032", "#ffffff"), "GITHUB": ("GH", "#24292F", "#ffffff"), "DOCKER": ("DK", "#2496ED", "#ffffff"),
    "LINUX": ("LX", "#FCC624", "#0f380f"), "VERCEL": ("V", "#111111", "#ffffff"),
    "NUMPY": ("NP", "#4DABCF", "#0f380f"), "PANDAS": ("PD", "#150458", "#E70488"), "SCIKIT-LEARN": ("SK", "#F7931E", "#0f380f"),
    "TENSORFLOW": ("TF", "#FF6F00", "#ffffff"), "KERAS": ("K", "#D00000", "#ffffff"), "PYTORCH": ("PT", "#EE4C2C", "#ffffff"),
    "KAGGLE": ("K", "#20BEFF", "#0f380f")}

# Simple Icons slugs used to embed genuine brand marks in the generated LCD SVG.
STACK_LOGOS = {"C": "c", "C++": "cplusplus", "PYTHON": "python", "JAVA": "openjdk",
    "JAVASCRIPT": "javascript", "TYPESCRIPT": "typescript", "HTML": "html5", "CSS": "css3",
    "REACT": "react", "NEXT.JS": "nextdotjs", "TAILWIND CSS": "tailwindcss",
    "MONGODB": "mongodb", "SQLITE": "sqlite", "GIT": "git", "GITHUB": "github",
    "DOCKER": "docker", "LINUX": "linux", "VERCEL": "vercel", "NUMPY": "numpy",
    "PANDAS": "pandas", "SCIKIT-LEARN": "scikitlearn", "TENSORFLOW": "tensorflow",
    "KERAS": "keras", "PYTORCH": "pytorch", "KAGGLE": "kaggle"}

# ---------------------------------------------------------------- 7. HI-SCORE labels
SCORE_LABELS = dict(score="SCORE", best="BEST DAY", streak="STREAK", maxstreak="MAX STREAK", monthly="MONTHLY XP")

# ---------------------------------------------------------------- 8. CONTACT buttons: label, url, icon text (<=3 chars). empty url = hidden
LINKS = [("GITHUB",    "https://github.com/v1haan24",                         ""),
         ("EMAIL",     "mailto:vihaanjain2411@gmail.com",                     ""),
         ("LINKEDIN",  "https://www.linkedin.com/in/vihaanjain24/", ""),
         ("DISCORD",   "https://discord.com/users/899297371484217365",         ""),
         ("PORTFOLIO", "https://google.com",                                   "")]

# ---------------------------------------------------------------- 9. extra hidden text (only inside the closed drop-downs)
PROFILE_TEXT_EXTRA = ""     # any extra plain-text sentence about you

# ================================================================= 10. DROP-DOWN (hidden AI/plain text) DESIGN
# Normal mixed-case text here (NOT the pixel font). Shown only when someone clicks a header open.
PROMPTS = dict(profile="", projects="THE PROJECT FILES", stack="EQUIPMENT CHECK", score="ACTIVITY ARCHIVE", contact="CHOOSE YOUR CHANNEL")   # shell-style label at top of each drop-down ("" = none)

# left column of the profile drop-down: (emoji, bold lead, rest of the line)
PROFILE_ROWS = [("🎓", "VJTI · Year 2", "Information Technology; Cybersecurity minor"),
                ("🧠", "Curious by nature", "When a problem catches my interest, I like to go deep."),
                ("🛠️", "Build to understand", "I enjoy making useful things that solve real problems."),
                ("🔭", "Exploring", "AI/ML, systems, cybersecurity, networks and communication."),
                ("🎮", "Learn deep, stay playful", "I take the tech seriously without taking myself too seriously."),
                ("🧭", "Side quests", "DSA, competitive programming and exploring the world.")]
# right column: Currently (bold name, description) and Ask me about
CURRENTLY = [("MemoraDB", "A temporal + semantic DBMS from scratch in C++, with time-travel queries and semantic search."),
             ("DAWN", "A networking project in progress. More details when it is ready.")]
ASK_ABOUT = ["Systems", "Low-level", "AI / ML", "Networking", "DSA / CP", "Travel"]

PROJECT_EMOJI = dict(db="🗄️", chip="🧠", dawn="🌅", graph="📈", net="🌐", maze="🧭", cal="📅")
CONTACT_EMOJI = {"GITHUB": "🐙", "EMAIL": "✉️", "LINKEDIN": "💼", "DISCORD": "🎮", "PORTFOLIO": "🌐"}
