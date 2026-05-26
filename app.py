import tkinter as tk
from tkinter import font


APP_TITLE = "Aventures of the Hazlenutts"


STORY = {
    "start": {
        "title": "Melody Wakes Up Brave",
        "image": "bedroom",
        "text": (
            "Melody the cat woke up in a sunbeam shaped exactly like a pancake. "
            "Her whiskers tingled. Today was clearly an adventure day.\n\n"
            "From the hallway, Callum the dog and Ledger the dinosaur were whispering very loudly. "
            "Callum had a backpack full of snacks. Ledger had a map that was mostly drawn in crayon."
        ),
        "choices": [
            ("Follow the snack crumbs", "crumb_trail"),
            ("Ask Ledger about the map", "map_plan"),
        ],
    },
    "crumb_trail": {
        "title": "The Trail of Crunchy Clues",
        "image": "kitchen",
        "text": (
            "Melody followed a line of tiny crunchy crumbs into the kitchen. Callum stood on a stool, "
            "wearing a superhero cape and holding a spoon like a royal scepter.\n\n"
            "\"I was not eating cereal,\" Callum announced, with cereal on his nose. "
            "\"I was researching breakfast science.\""
        ),
        "choices": [
            ("Help Callum with breakfast science", "breakfast_science"),
            ("Investigate the wobbly pantry door", "pantry"),
        ],
    },
    "map_plan": {
        "title": "Ledger's Wiggly Map",
        "image": "map",
        "text": (
            "Ledger spread the map across the floor. It showed three important places: "
            "The Sofa Mountain, The Pillow Cave, and The Mysterious X Behind the Laundry Basket.\n\n"
            "\"I am almost sure the X means treasure,\" Ledger said. \"Or socks. But maybe treasure socks.\""
        ),
        "choices": [
            ("Climb Sofa Mountain", "sofa_mountain"),
            ("Search behind the laundry basket", "laundry_x"),
        ],
    },
    "breakfast_science": {
        "title": "Breakfast Science",
        "image": "kitchen",
        "text": (
            "Melody, Callum, and Ledger tested whether toast tastes better when it is cut into stars. "
            "The answer was yes. They also tested whether jam makes a good mustache. "
            "The answer was very sticky.\n\n"
            "A soft meow came from the pantry. Melody's ears popped up like two tiny flags."
        ),
        "choices": [
            ("Open the pantry carefully", "pantry"),
            ("Pack star toast for the road", "sofa_mountain"),
        ],
    },
    "pantry": {
        "title": "The Pantry Parade",
        "image": "pantry",
        "text": (
            "Inside the pantry, Melody found a parade of cans, a bag of flour wearing a dust hat, "
            "and one very suspicious paper bag.\n\n"
            "The bag rustled. Ledger gave a tiny dino gasp. Callum whispered, \"If it is a dragon, I hope it likes crackers.\" "
            "Melody tapped the bag. Out rolled a toy mouse with a note tied around it."
        ),
        "choices": [
            ("Read the tiny note", "tiny_note"),
            ("Chase the toy mouse", "mouse_chase"),
        ],
    },
    "sofa_mountain": {
        "title": "Sofa Mountain",
        "image": "sofa",
        "text": (
            "Sofa Mountain was tall, squishy, and guarded by a blanket that kept trying to become a fort. "
            "Melody climbed first, because brave cats are excellent at cushions.\n\n"
            "At the summit, Callum found a button. Ledger found three coins. Melody found the best view "
            "of the entire living room kingdom."
        ),
        "choices": [
            ("Build a blanket fort", "blanket_fort"),
            ("Slide down to the laundry basket", "laundry_x"),
        ],
    },
    "laundry_x": {
        "title": "The Mysterious X",
        "image": "laundry",
        "text": (
            "Behind the laundry basket was an X made from two striped socks. Under the X sat a small box.\n\n"
            "Callum opened it with great ceremony. Inside were shiny stickers, a bell, and a note that said, "
            "\"For Melody, finder of cozy mysteries.\" Ledger bowed so deeply he bonked the basket."
        ),
        "choices": [
            ("Put the bell on Melody's adventure collar", "collar_bell"),
            ("Use the stickers to decorate the map", "decorate_map"),
        ],
    },
    "tiny_note": {
        "title": "A Note for a Noble Cat",
        "image": "note",
        "text": (
            "The tiny note said: \"Dear Melody, the Giggle Garden needs your help. "
            "The flowers forgot how to giggle. Bring snacks.\"\n\n"
            "Callum saluted with a cracker. Ledger added a giant arrow to the map, pointing outside."
        ),
        "choices": [
            ("Visit the Giggle Garden", "garden"),
            ("Gather supplies first", "supplies"),
        ],
    },
    "mouse_chase": {
        "title": "The Great Toy Mouse Chase",
        "image": "hallway",
        "text": (
            "The toy mouse zipped down the hallway. Melody dashed after it, skidding just a little, "
            "because floors are sneaky.\n\n"
            "It bumped into a flowerpot and stopped. From the pot came a tiny squeaky laugh. "
            "The Giggle Garden was calling."
        ),
        "choices": [
            ("Answer the tiny laugh", "garden"),
            ("Return to tell Callum and Ledger", "supplies"),
        ],
    },
    "blanket_fort": {
        "title": "The Blanket Fort Council",
        "image": "fort",
        "text": (
            "Inside the blanket fort, the three adventurers held a very serious council. "
            "The rules were: whisper, share snacks, and never sit on the flashlight.\n\n"
            "Ledger declared Melody captain. Callum declared himself snack manager. "
            "Melody declared the fort wonderfully nap-shaped."
        ),
        "choices": [
            ("Take a captain's nap", "cozy_ending"),
            ("March to the garden", "garden"),
        ],
    },
    "collar_bell": {
        "title": "The Bell of Bravery",
        "image": "bell",
        "text": (
            "Melody's new bell made a cheerful jingle-jingle. Every time it rang, Callum shouted, "
            "\"Adventure detected!\" Ledger wrote that down as scientific proof.\n\n"
            "The jingle seemed to make the house feel even more magical."
        ),
        "choices": [
            ("Follow the jingle to the garden", "garden"),
            ("Celebrate with a living room parade", "parade_ending"),
        ],
    },
    "decorate_map": {
        "title": "A Map Full of Sparkles",
        "image": "map",
        "text": (
            "The map looked much better with stickers. Stars for brave places. Hearts for snack places. "
            "One giant shiny sticker for Melody, because she was the hero.\n\n"
            "Ledger added a new place: The Giggle Garden."
        ),
        "choices": [
            ("Go to the Giggle Garden", "garden"),
            ("Save the map for tomorrow", "cozy_ending"),
        ],
    },
    "supplies": {
        "title": "Adventure Supplies",
        "image": "supplies",
        "text": (
            "The team packed star toast, three crackers, a magnifying glass, and one emergency spoon. "
            "Callum wanted to pack a chair, but Melody gently explained that chairs are not backpack food.\n\n"
            "Ledger checked the map twice. Melody checked the snacks three times."
        ),
        "choices": [
            ("Head to the garden", "garden"),
            ("Make a snack picnic first", "picnic_ending"),
        ],
    },
    "garden": {
        "title": "The Giggle Garden",
        "image": "garden",
        "text": (
            "In the garden, the flowers drooped sadly. Melody gave her bell a tiny jingle. "
            "Callum made his silliest cereal-nose face. Ledger read a joke from the map: "
            "\"Why did the cat sit on the computer? To keep an eye on the mouse!\"\n\n"
            "The flowers burst into giggles. Petals wiggled. Leaves clapped. Melody purred proudly."
        ),
        "choices": [
            ("Dance with the flowers", "dance_ending"),
            ("Name Melody Queen of Giggles", "queen_ending"),
        ],
    },
    "cozy_ending": {
        "title": "A Cozy Hero's Rest",
        "image": "nap",
        "text": (
            "Melody curled up with Callum and Ledger nearby, the map tucked safely under one paw. "
            "Some adventures end with treasure. This one ended with a nap, which Melody knew was even better."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Melody's story again", "start")],
    },
    "parade_ending": {
        "title": "The Living Room Parade",
        "image": "parade",
        "text": (
            "Melody led the grand parade past Sofa Mountain, around the coffee table, and through the blanket fort. "
            "Callum jingled a spoon. Ledger waved the map. Everyone agreed it was the finest parade of the afternoon."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Melody's story again", "start")],
    },
    "picnic_ending": {
        "title": "The Snack Picnic",
        "image": "picnic",
        "text": (
            "The adventurers held a picnic on a blanket. Melody got the sunniest spot. "
            "Callum counted crackers. Ledger gave a tiny speech about teamwork, bravery, and excellent toast shapes."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Melody's story again", "start")],
    },
    "dance_ending": {
        "title": "The Flower Dance",
        "image": "garden",
        "text": (
            "The flowers danced, Callum twirled, Ledger wiggled, and Melody performed one perfect cat leap. "
            "The Giggle Garden was saved, and the whole day smelled like sunshine."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Melody's story again", "start")],
    },
    "queen_ending": {
        "title": "Queen Melody of Giggles",
        "image": "queen",
        "text": (
            "The flowers crowned Melody with a daisy chain. Callum cheered. Ledger carefully wrote, "
            "\"Melody is brave, kind, and very good at mysteries.\"\n\n"
            "Queen Melody purred, because every kingdom needs kindness and snacks."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Melody's story again", "start")],
    },
}


CALLUM_STORY = {
    "start": {
        "title": "Callum and the Snack Patrol",
        "image": "kitchen",
        "text": (
            "Callum the dog woke up with one very important thought: someone had to protect the snacks. "
            "He put on his pretend patrol badge and sniffed the air.\n\n"
            "Melody the cat stretched in a sunbeam. Ledger the dinosaur held up a crayon map. "
            "\"The Missing Crunchies are this way,\" Ledger announced."
        ),
        "choices": [
            ("Sniff for clues under the table", "table_clues"),
            ("Ask Ledger to read the map", "map_mission"),
        ],
    },
    "table_clues": {
        "title": "The Under-Table Investigation",
        "image": "kitchen",
        "text": (
            "Callum sniffed under the table and found three crumbs, one button, and a spoon that looked surprised. "
            "Melody gently patted the spoon. Ledger wrote, \"Spoon is suspicious,\" on the map.\n\n"
            "Then Callum heard a tiny crunch from the pantry."
        ),
        "choices": [
            ("Check the pantry", "pantry_guard"),
            ("Follow the crumbs to Sofa Mountain", "sofa_search"),
        ],
    },
    "map_mission": {
        "title": "Ledger's Snack Map",
        "image": "map",
        "text": (
            "Ledger's map had arrows, stars, and one drawing of Callum with very heroic ears. "
            "It pointed to the blanket fort, where all serious snack meetings happen.\n\n"
            "Melody flicked her tail and said, \"Lead the way, Captain Callum.\""
        ),
        "choices": [
            ("March to the blanket fort", "fort_meeting"),
            ("Take a shortcut over Sofa Mountain", "sofa_search"),
        ],
    },
    "pantry_guard": {
        "title": "The Pantry Guard",
        "image": "pantry",
        "text": (
            "In the pantry, Callum found the Missing Crunchies sitting safely behind a flour bag. "
            "The flour bag had a white puff on top like a tiny snowy hat.\n\n"
            "Callum wagged so hard that Ledger had to hold onto the map. Melody declared the snacks rescued."
        ),
        "choices": [
            ("Share the rescued snacks", "snack_ending"),
            ("Carry them to the Giggle Garden", "garden_delivery"),
        ],
    },
    "sofa_search": {
        "title": "Sofa Mountain Search",
        "image": "sofa",
        "text": (
            "Callum climbed Sofa Mountain with careful paws. Melody leaped up beside him. "
            "Ledger tried to stomp bravely, but the cushions made every step go poof.\n\n"
            "At the top, Callum spotted a shiny trail leading toward the garden door."
        ),
        "choices": [
            ("Follow the shiny trail", "garden_delivery"),
            ("Call a blanket fort meeting", "fort_meeting"),
        ],
    },
    "fort_meeting": {
        "title": "The Snack Patrol Meeting",
        "image": "fort",
        "text": (
            "Inside the blanket fort, Callum made a gentle bark that meant, \"Team, we can solve this.\" "
            "Melody nodded wisely. Ledger raised one tiny dinosaur arm and voted for snacks.\n\n"
            "Everyone agreed: the mission needed kindness, courage, and crackers."
        ),
        "choices": [
            ("Start a living room parade", "parade_ending"),
            ("Deliver crackers to the flowers", "garden_delivery"),
        ],
    },
    "garden_delivery": {
        "title": "Callum's Garden Delivery",
        "image": "garden",
        "text": (
            "Callum carried the crackers to the Giggle Garden. The flowers were droopy until he set the snack plate down "
            "and gave his happiest tail wag.\n\n"
            "The flowers giggled. Melody purred. Ledger named the mission a crunchy success."
        ),
        "choices": [
            ("Celebrate with a snack picnic", "snack_ending"),
            ("Hold a victory parade", "parade_ending"),
        ],
    },
    "snack_ending": {
        "title": "Captain Callum's Snack Picnic",
        "image": "picnic",
        "text": (
            "Callum shared every rescued snack. Melody got the sunniest spot, Ledger got the biggest cracker, "
            "and Callum got a hero hug.\n\n"
            "The Snack Patrol was officially the coziest team in the house."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Callum's story again", "start")],
    },
    "parade_ending": {
        "title": "The Wagging Victory Parade",
        "image": "parade",
        "text": (
            "Callum led the parade with proud paws and a wagging tail. Melody jingled a bell. "
            "Ledger waved the map upside down, which somehow made it more exciting."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Callum's story again", "start")],
    },
}


LEDGER_STORY = {
    "start": {
        "title": "Ledger's Tiny Dino Expedition",
        "image": "map",
        "text": (
            "Ledger the dinosaur woke up ready for science. He sharpened his green crayon, unrolled his map, "
            "and made his bravest tiny roar.\n\n"
            "Melody the cat blinked from her sunbeam. Callum the dog sniffed the map and found a cracker crumb."
        ),
        "choices": [
            ("Study the cracker crumb", "crumb_science"),
            ("Explore Pillow Cave", "pillow_cave"),
        ],
    },
    "crumb_science": {
        "title": "Crumb Science",
        "image": "kitchen",
        "text": (
            "Ledger inspected the crumb with a magnifying glass. \"Important discovery,\" he said. "
            "\"This crumb is small, crunchy, and probably lonely.\"\n\n"
            "Callum volunteered to keep it company by eating it. Melody suggested finding where it came from."
        ),
        "choices": [
            ("Search the pantry volcano", "pantry_volcano"),
            ("Add the clue to the map", "map_sparkles"),
        ],
    },
    "pillow_cave": {
        "title": "Pillow Cave",
        "image": "fort",
        "text": (
            "Pillow Cave was soft, shadowy, and full of excellent echoes. Ledger gave one little roar. "
            "The cave answered with a very polite poof.\n\n"
            "Melody found a ribbon. Callum found a snack wrapper. Ledger found courage."
        ),
        "choices": [
            ("Make a dino flag from the ribbon", "dino_flag"),
            ("Follow the snack wrapper", "pantry_volcano"),
        ],
    },
    "pantry_volcano": {
        "title": "The Pantry Volcano",
        "image": "pantry",
        "text": (
            "The flour bag in the pantry looked exactly like a snowy volcano. Ledger announced that it must be studied "
            "from a safe distance, which was three dinosaur steps away.\n\n"
            "A note peeked out from behind it: \"The Giggle Garden needs a brave explorer.\""
        ),
        "choices": [
            ("Lead the expedition to the garden", "garden_explorer"),
            ("Bring supplies first", "dino_supplies"),
        ],
    },
    "map_sparkles": {
        "title": "The Sparkle Map",
        "image": "map",
        "text": (
            "Ledger added the crumb clue to the map and surrounded it with seven stars. "
            "Melody said maps are easier to follow when they sparkle. Callum agreed because sparkles might mean snacks."
        ),
        "choices": [
            ("Follow the sparkles", "garden_explorer"),
            ("Explore Pillow Cave", "pillow_cave"),
        ],
    },
    "dino_flag": {
        "title": "The Dino Flag",
        "image": "parade",
        "text": (
            "Ledger tied the ribbon to a spoon and made the first official Dino Expedition Flag. "
            "Callum saluted it. Melody gave it a royal paw tap.\n\n"
            "With the flag held high, the team was ready for anything gentle and silly."
        ),
        "choices": [
            ("March to the garden", "garden_explorer"),
            ("Pack expedition supplies", "dino_supplies"),
        ],
    },
    "dino_supplies": {
        "title": "Dino Supplies",
        "image": "supplies",
        "text": (
            "Ledger packed a crayon, a cracker, two stickers, and one emergency compliment. "
            "Melody packed patience. Callum packed enthusiasm and tried to pack a chair again."
        ),
        "choices": [
            ("Visit the Giggle Garden", "garden_explorer"),
            ("Have a practice parade", "dino_parade_ending"),
        ],
    },
    "garden_explorer": {
        "title": "Ledger Saves the Giggles",
        "image": "garden",
        "text": (
            "The Giggle Garden was quiet. Ledger stepped forward and told the flowers his best dinosaur joke: "
            "\"What do tiny dinosaurs put on toast? Jurassi-jam!\"\n\n"
            "The flowers giggled so much their petals wobbled. Melody clapped her paws. Callum wagged in circles."
        ),
        "choices": [
            ("Draw the garden on the map", "map_ending"),
            ("Lead a dino parade", "dino_parade_ending"),
        ],
    },
    "map_ending": {
        "title": "Ledger's Great Explorer Map",
        "image": "map",
        "text": (
            "Ledger drew the whole adventure on his map: the cave, the pantry volcano, the garden, "
            "and three heroic friends. He put a giant star beside his name, then added stars for everyone else too."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Ledger's story again", "start")],
    },
    "dino_parade_ending": {
        "title": "The Tiny Dino Parade",
        "image": "parade",
        "text": (
            "Ledger led the tiniest, proudest dinosaur parade the living room had ever seen. "
            "Melody stepped lightly, Callum wagged proudly, and the Dino Expedition Flag waved all the way home."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Ledger's story again", "start")],
    },
}


STORIES = {
    "melody": STORY,
    "callum": CALLUM_STORY,
    "ledger": LEDGER_STORY,
}


CHARACTERS = {
    "melody": {
        "name": "Melody",
        "description": "Melody the brave cat",
        "button": "Play as Melody the cat",
    },
    "callum": {
        "name": "Callum",
        "description": "Callum the snack-saving dog",
        "button": "Play as Callum the dog",
    },
    "ledger": {
        "name": "Ledger",
        "description": "Ledger the tiny T. rex explorer",
        "button": "Play as Ledger the dinosaur",
    },
}


PALETTES = {
    "bedroom": ("#ffe5a8", "#f7b267", "#f79d65"),
    "kitchen": ("#d6f5ff", "#7bdff2", "#f2b5d4"),
    "map": ("#f9e6b3", "#90be6d", "#f8961e"),
    "pantry": ("#f7ede2", "#84a59d", "#f28482"),
    "sofa": ("#cdb4db", "#ffc8dd", "#bde0fe"),
    "laundry": ("#e2ece9", "#b8c0ff", "#ffafcc"),
    "note": ("#fff3b0", "#e09f3e", "#9e2a2b"),
    "hallway": ("#caf0f8", "#00b4d8", "#ffb703"),
    "fort": ("#ffd6a5", "#a0c4ff", "#bdb2ff"),
    "bell": ("#fff1a8", "#f4a261", "#2a9d8f"),
    "supplies": ("#e9f5db", "#52b788", "#f4a261"),
    "garden": ("#d8f3dc", "#80ed99", "#ff70a6"),
    "nap": ("#f1e4f3", "#c9ada7", "#9a8c98"),
    "parade": ("#fff0f3", "#ff4d6d", "#48cae4"),
    "picnic": ("#fdffb6", "#caffbf", "#ffadad"),
    "queen": ("#fcefb4", "#f7aef8", "#72ddf7"),
}


class MelodyGame:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.minsize(760, 640)
        self.current_character = None
        self.current_scene = "start"
        self.history = []

        self.title_font = font.Font(family="Georgia", size=24, weight="bold")
        self.body_font = font.Font(family="Segoe UI", size=14)
        self.button_font = font.Font(family="Segoe UI", size=12, weight="bold")

        self.root.configure(bg="#fffaf0")
        self.main = tk.Frame(root, bg="#fffaf0", padx=24, pady=18)
        self.main.pack(fill="both", expand=True)

        self.header = tk.Label(
            self.main,
            text=APP_TITLE,
            font=self.title_font,
            bg="#fffaf0",
            fg="#4a3b2a",
        )
        self.header.pack(anchor="w")

        self.subtitle = tk.Label(
            self.main,
            text="A gentle read-along adventure starring Melody the cat, Callum the dog, and Ledger the dinosaur",
            font=("Segoe UI", 11),
            bg="#fffaf0",
            fg="#6b5a45",
        )
        self.subtitle.pack(anchor="w", pady=(0, 12))

        self.content = tk.Frame(self.main, bg="#fffaf0")
        self.content.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(
            self.content,
            width=360,
            height=300,
            bg="#ffffff",
            highlightthickness=0,
        )
        self.canvas.pack(side="left", fill="both", expand=False, padx=(0, 18))

        self.story_panel = tk.Frame(self.content, bg="#fffaf0")
        self.story_panel.pack(side="left", fill="both", expand=True)

        self.scene_title = tk.Label(
            self.story_panel,
            text="",
            font=("Georgia", 20, "bold"),
            bg="#fffaf0",
            fg="#3f3428",
            wraplength=430,
            justify="left",
        )
        self.scene_title.pack(anchor="w", pady=(4, 8))

        self.story_text = tk.Message(
            self.story_panel,
            text="",
            font=self.body_font,
            bg="#fffaf0",
            fg="#342f2b",
            width=430,
            padx=0,
            pady=0,
        )
        self.story_text.pack(anchor="w", fill="x")

        self.choices_frame = tk.Frame(self.story_panel, bg="#fffaf0")
        self.choices_frame.pack(anchor="w", fill="x", pady=(18, 0))

        self.footer = tk.Frame(self.main, bg="#fffaf0")
        self.footer.pack(fill="x", pady=(14, 0))

        self.back_button = tk.Button(
            self.footer,
            text="Back",
            font=self.button_font,
            command=self.go_back,
            bg="#f2d0a4",
            fg="#30271f",
            activebackground="#edbc7f",
            relief="flat",
            padx=18,
            pady=8,
        )
        self.back_button.pack(side="left")

        self.read_aloud_hint = tk.Label(
            self.footer,
            text="Tip: read together and let your child choose what happens next.",
            font=("Segoe UI", 10),
            bg="#fffaf0",
            fg="#766754",
        )
        self.read_aloud_hint.pack(side="right")

        self.show_character_select()

    def show_character_select(self):
        self.current_character = None
        self.current_scene = "character_select"
        self.history = []
        self.scene_title.config(text="Choose Your Hero")
        self.story_text.config(
            text=(
                "Pick who should lead this adventure. Each hero has their own story arc, "
                "with Melody, Callum, and Ledger still helping each other along the way."
            )
        )

        for child in self.choices_frame.winfo_children():
            child.destroy()

        for character_id, info in CHARACTERS.items():
            button = tk.Button(
                self.choices_frame,
                text=info["button"],
                font=self.button_font,
                command=lambda hero=character_id: self.start_story(hero),
                bg="#88d498",
                fg="#17351f",
                activebackground="#6cc57e",
                relief="flat",
                padx=14,
                pady=10,
                wraplength=360,
                justify="left",
            )
            button.pack(fill="x", pady=5)

        self.back_button.config(state="disabled")
        self.draw_character_select()

    def start_story(self, character_id):
        self.current_character = character_id
        self.history = []
        self.show_scene("start", remember=False)

    def show_scene(self, scene_id, remember=True):
        if scene_id == "character_select":
            self.show_character_select()
            return

        if remember:
            self.history.append(self.current_scene)

        self.current_scene = scene_id
        scene = STORIES[self.current_character][scene_id]
        self.scene_title.config(text=scene["title"])
        self.story_text.config(text=scene["text"])

        for child in self.choices_frame.winfo_children():
            child.destroy()

        for label, next_scene in scene["choices"]:
            button = tk.Button(
                self.choices_frame,
                text=label,
                font=self.button_font,
                command=lambda target=next_scene: self.show_scene(target),
                bg="#88d498",
                fg="#17351f",
                activebackground="#6cc57e",
                relief="flat",
                padx=14,
                pady=10,
                wraplength=360,
                justify="left",
            )
            button.pack(fill="x", pady=5)

        self.back_button.config(state="normal" if self.history else "disabled")
        self.draw_scene(scene["image"])

    def go_back(self):
        if not self.history:
            return
        previous = self.history.pop()
        self.show_scene(previous, remember=False)

    def draw_character_select(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 360, 300, fill="#fff1a8", outline="")
        self.canvas.create_oval(-70, -70, 150, 112, fill="#ffffff", outline="")
        self.canvas.create_oval(220, 185, 460, 370, fill="#ffffff", outline="")
        self.draw_stars("#f4a261", "#ff70a6")
        self.draw_cat(178, 132, scale=0.95, body="#f4a261", stripes="#bc6c25", name="Melody")
        self.draw_dog(76, 198, scale=0.68, name="Callum")
        self.draw_dino(286, 198, scale=0.68, name="Ledger")

    def draw_scene(self, image_key):
        self.canvas.delete("all")
        bg, accent, pop = PALETTES.get(image_key, PALETTES["bedroom"])
        width = int(self.canvas["width"])
        height = int(self.canvas["height"])

        self.canvas.create_rectangle(0, 0, width, height, fill=bg, outline="")
        self.canvas.create_oval(-80, -70, 160, 110, fill="#ffffff", outline="")
        self.canvas.create_oval(230, 180, 460, 370, fill="#ffffff", outline="")

        if image_key in {"garden", "queen"}:
            self.draw_flowers(accent, pop)
        elif image_key in {"map", "note"}:
            self.draw_map(accent, pop)
        elif image_key in {"sofa", "fort", "nap"}:
            self.draw_sofa(accent, pop)
        elif image_key in {"kitchen", "pantry", "supplies", "picnic"}:
            self.draw_snacks(accent, pop)
        elif image_key in {"laundry", "hallway"}:
            self.draw_laundry(accent, pop)
        elif image_key in {"bell", "parade"}:
            self.draw_bell(accent, pop)
        else:
            self.draw_stars(accent, pop)

        self.draw_adventurers()

        if image_key == "queen":
            self.canvas.create_arc(135, 63, 222, 122, start=0, extent=180, style="arc", width=4, outline="#f9c74f")
            for x, y in [(147, 81), (178, 66), (209, 81)]:
                self.canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill="#f9c74f", outline="#c08700")

    def draw_adventurers(self):
        positions = {
            "melody": (178, 146, 1.08),
            "callum": (82, 190, 0.78),
            "ledger": (274, 190, 0.78),
        }
        if self.current_character == "callum":
            positions = {
                "callum": (178, 150, 1.05),
                "melody": (82, 190, 0.76),
                "ledger": (274, 190, 0.76),
            }
        elif self.current_character == "ledger":
            positions = {
                "ledger": (178, 150, 1.02),
                "melody": (82, 190, 0.76),
                "callum": (274, 190, 0.76),
            }

        for character_id in ["melody", "callum", "ledger"]:
            x, y, scale = positions[character_id]
            self.draw_character(character_id, x, y, scale)

    def draw_character(self, character_id, x, y, scale):
        if character_id == "melody":
            self.draw_cat(x, y, scale=scale, body="#f4a261", stripes="#bc6c25", name="Melody")
        elif character_id == "callum":
            self.draw_dog(x, y, scale=scale, name="Callum")
        elif character_id == "ledger":
            self.draw_dino(x, y, scale=scale, name="Ledger")

    def draw_cat(self, x, y, scale, body, stripes, name):
        s = scale
        self.canvas.create_oval(x - 54 * s, y - 8 * s, x + 54 * s, y + 76 * s, fill=body, outline="#5c4033", width=2)
        self.canvas.create_oval(x - 42 * s, y - 70 * s, x + 42 * s, y + 12 * s, fill=body, outline="#5c4033", width=2)
        self.canvas.create_polygon(x - 38 * s, y - 44 * s, x - 23 * s, y - 92 * s, x - 8 * s, y - 45 * s, fill=body, outline="#5c4033")
        self.canvas.create_polygon(x + 38 * s, y - 44 * s, x + 23 * s, y - 92 * s, x + 8 * s, y - 45 * s, fill=body, outline="#5c4033")
        self.canvas.create_polygon(x - 29 * s, y - 48 * s, x - 23 * s, y - 73 * s, x - 15 * s, y - 48 * s, fill="#ffd6d6", outline="")
        self.canvas.create_polygon(x + 29 * s, y - 48 * s, x + 23 * s, y - 73 * s, x + 15 * s, y - 48 * s, fill="#ffd6d6", outline="")

        for offset in [-22, 0, 22]:
            self.canvas.create_line(x + offset * s, y - 66 * s, x + (offset - 6) * s, y - 47 * s, fill=stripes, width=max(1, int(3 * s)))

        self.canvas.create_oval(x - 21 * s, y - 35 * s, x - 9 * s, y - 23 * s, fill="#243b53", outline="")
        self.canvas.create_oval(x + 9 * s, y - 35 * s, x + 21 * s, y - 23 * s, fill="#243b53", outline="")
        self.canvas.create_oval(x - 4 * s, y - 18 * s, x + 4 * s, y - 10 * s, fill="#5c4033", outline="")
        self.canvas.create_arc(x - 12 * s, y - 16 * s, x, y - 2 * s, start=200, extent=120, style="arc", outline="#5c4033", width=2)
        self.canvas.create_arc(x, y - 16 * s, x + 12 * s, y - 2 * s, start=220, extent=120, style="arc", outline="#5c4033", width=2)

        for side in [-1, 1]:
            self.canvas.create_line(x + side * 4 * s, y - 13 * s, x + side * 39 * s, y - 21 * s, fill="#5c4033")
            self.canvas.create_line(x + side * 4 * s, y - 10 * s, x + side * 41 * s, y - 10 * s, fill="#5c4033")
            self.canvas.create_line(x + side * 4 * s, y - 7 * s, x + side * 39 * s, y + 1 * s, fill="#5c4033")

        self.canvas.create_arc(x + 37 * s, y + 10 * s, x + 92 * s, y + 78 * s, start=92, extent=210, style="arc", outline=body, width=max(6, int(11 * s)))
        self.canvas.create_text(x, y + 93 * s, text=name, fill="#3f3428", font=("Segoe UI", max(9, int(11 * s)), "bold"))

    def draw_dog(self, x, y, scale, name):
        s = scale
        tan = "#c98f5a"
        dark = "#3b2a24"
        cream = "#f5dfbf"
        self.canvas.create_oval(x - 52 * s, y - 4 * s, x + 52 * s, y + 70 * s, fill=tan, outline=dark, width=2)
        self.canvas.create_oval(x - 42 * s, y - 66 * s, x + 48 * s, y + 12 * s, fill=tan, outline=dark, width=2)
        self.canvas.create_polygon(x - 34 * s, y - 48 * s, x - 18 * s, y - 96 * s, x - 2 * s, y - 42 * s, fill=dark, outline=dark)
        self.canvas.create_polygon(x + 34 * s, y - 48 * s, x + 18 * s, y - 96 * s, x + 2 * s, y - 42 * s, fill=dark, outline=dark)
        self.canvas.create_oval(x - 22 * s, y - 30 * s, x + 30 * s, y + 12 * s, fill=dark, outline="")
        self.canvas.create_oval(x - 12 * s, y - 18 * s, x + 34 * s, y + 18 * s, fill=cream, outline="")
        self.canvas.create_oval(x - 22 * s, y - 34 * s, x - 10 * s, y - 22 * s, fill="#1f2933", outline="")
        self.canvas.create_oval(x + 14 * s, y - 34 * s, x + 26 * s, y - 22 * s, fill="#1f2933", outline="")
        self.canvas.create_oval(x + 5 * s, y - 12 * s, x + 17 * s, y - 2 * s, fill="#1f2933", outline="")
        self.canvas.create_arc(x - 4 * s, y - 8 * s, x + 10 * s, y + 8 * s, start=205, extent=120, style="arc", outline=dark, width=2)
        self.canvas.create_arc(x + 12 * s, y - 8 * s, x + 26 * s, y + 8 * s, start=215, extent=120, style="arc", outline=dark, width=2)
        self.canvas.create_oval(x - 38 * s, y + 20 * s, x - 12 * s, y + 54 * s, fill=cream, outline="")
        self.canvas.create_line(x + 42 * s, y + 10 * s, x + 78 * s, y - 18 * s, fill=dark, width=max(5, int(8 * s)))
        self.canvas.create_line(x + 75 * s, y - 18 * s, x + 88 * s, y - 8 * s, fill=dark, width=max(4, int(6 * s)))
        self.canvas.create_text(x, y + 89 * s, text=name, fill="#3f3428", font=("Segoe UI", max(9, int(11 * s)), "bold"))

    def draw_dino(self, x, y, scale, name):
        s = scale
        green = "#7cc576"
        dark_green = "#2d6a4f"
        belly = "#d8f3dc"
        self.canvas.create_oval(x - 48 * s, y - 4 * s, x + 50 * s, y + 72 * s, fill=green, outline=dark_green, width=2)
        self.canvas.create_oval(x - 18 * s, y - 78 * s, x + 64 * s, y - 10 * s, fill=green, outline=dark_green, width=2)
        self.canvas.create_polygon(x - 44 * s, y + 12 * s, x - 92 * s, y + 36 * s, x - 42 * s, y + 50 * s, fill=green, outline=dark_green)
        self.canvas.create_oval(x - 22 * s, y + 10 * s, x + 26 * s, y + 64 * s, fill=belly, outline="")
        for dx, dy in [(-20, -34), (-2, -58), (22, -68), (44, -52)]:
            self.canvas.create_polygon(
                x + dx * s,
                y + dy * s,
                x + (dx + 10) * s,
                y + (dy - 20) * s,
                x + (dx + 20) * s,
                y + dy * s,
                fill="#f9c74f",
                outline=dark_green,
            )
        self.canvas.create_oval(x + 18 * s, y - 55 * s, x + 31 * s, y - 42 * s, fill="#1f2933", outline="")
        self.canvas.create_arc(x + 30 * s, y - 40 * s, x + 56 * s, y - 22 * s, start=210, extent=110, style="arc", outline=dark_green, width=2)
        self.canvas.create_polygon(x + 51 * s, y - 39 * s, x + 69 * s, y - 33 * s, x + 51 * s, y - 27 * s, fill=belly, outline=dark_green)
        self.canvas.create_line(x - 10 * s, y + 14 * s, x - 38 * s, y + 34 * s, fill=dark_green, width=max(4, int(6 * s)))
        self.canvas.create_line(x + 18 * s, y + 14 * s, x + 42 * s, y + 34 * s, fill=dark_green, width=max(4, int(6 * s)))
        self.canvas.create_line(x - 18 * s, y + 62 * s, x - 30 * s, y + 86 * s, fill=dark_green, width=max(5, int(8 * s)))
        self.canvas.create_line(x + 18 * s, y + 62 * s, x + 30 * s, y + 86 * s, fill=dark_green, width=max(5, int(8 * s)))
        self.canvas.create_text(x, y + 96 * s, text=name, fill="#3f3428", font=("Segoe UI", max(9, int(11 * s)), "bold"))

    def draw_flowers(self, accent, pop):
        for x, y in [(48, 238), (314, 230), (62, 92), (296, 88)]:
            self.canvas.create_line(x, y, x, y + 42, fill="#2d6a4f", width=3)
            for dx, dy in [(0, -12), (10, -3), (-10, -3), (7, 9), (-7, 9)]:
                self.canvas.create_oval(x + dx - 9, y + dy - 9, x + dx + 9, y + dy + 9, fill=pop, outline="")
            self.canvas.create_oval(x - 7, y - 7, x + 7, y + 7, fill="#ffea00", outline="")
        self.draw_stars(accent, pop)

    def draw_map(self, accent, pop):
        self.canvas.create_rectangle(38, 52, 322, 242, fill="#fff8dc", outline="#9c6644", width=3)
        self.canvas.create_line(76, 88, 132, 142, 202, 108, 270, 196, fill=accent, width=4, smooth=True)
        self.canvas.create_text(96, 78, text="Sofa", fill="#6b4f3a", font=("Segoe UI", 12, "bold"))
        self.canvas.create_text(250, 204, text="X", fill=pop, font=("Segoe UI", 28, "bold"))

    def draw_sofa(self, accent, pop):
        self.canvas.create_rectangle(35, 170, 324, 250, fill=accent, outline="#6d597a", width=3)
        self.canvas.create_rectangle(62, 126, 160, 186, fill=pop, outline="#6d597a", width=3)
        self.canvas.create_rectangle(190, 126, 288, 186, fill=pop, outline="#6d597a", width=3)
        self.canvas.create_oval(54, 236, 86, 268, fill="#6d597a", outline="")
        self.canvas.create_oval(270, 236, 302, 268, fill="#6d597a", outline="")

    def draw_snacks(self, accent, pop):
        self.canvas.create_rectangle(32, 218, 326, 268, fill="#d4a373", outline="")
        self.canvas.create_oval(62, 186, 146, 224, fill="#ffffff", outline="#8d6e63", width=2)
        for x in [82, 104, 126]:
            self.canvas.create_oval(x - 11, 190, x + 11, 212, fill=pop, outline="")
        self.canvas.create_rectangle(236, 154, 294, 222, fill=accent, outline="#6b705c", width=2)
        self.canvas.create_text(265, 186, text="SNACKS", fill="#3f3428", font=("Segoe UI", 8, "bold"))

    def draw_laundry(self, accent, pop):
        self.canvas.create_oval(44, 156, 150, 260, fill="#ffffff", outline="#6c757d", width=3)
        self.canvas.create_arc(44, 116, 150, 196, start=0, extent=180, style="arc", outline="#6c757d", width=4)
        for x, y, color in [(238, 154, accent), (278, 188, pop), (228, 220, "#ffffff")]:
            self.canvas.create_oval(x - 32, y - 18, x + 32, y + 18, fill=color, outline="#6c757d")
        self.canvas.create_text(254, 94, text="X", fill=pop, font=("Segoe UI", 40, "bold"))

    def draw_bell(self, accent, pop):
        self.canvas.create_arc(128, 72, 232, 202, start=0, extent=180, fill=pop, outline="#7f5539", width=3)
        self.canvas.create_rectangle(128, 135, 232, 202, fill=pop, outline="#7f5539", width=3)
        self.canvas.create_oval(166, 194, 194, 222, fill=accent, outline="#7f5539", width=2)
        self.draw_stars(accent, pop)

    def draw_stars(self, accent, pop):
        for x, y, color in [(50, 55, accent), (306, 62, pop), (320, 252, accent), (42, 258, pop)]:
            self.canvas.create_text(x, y, text="*", fill=color, font=("Georgia", 34, "bold"))


def main():
    root = tk.Tk()
    MelodyGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
