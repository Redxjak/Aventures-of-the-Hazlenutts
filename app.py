import re
import tkinter as tk
from tkinter import font
from pathlib import Path


APP_TITLE = "Fun Family Adventures"
APP_VERSION = "v1.1.3"
RELEASE_NOTES = [
    "Added support for the updated FFA character branching story brief.",
    "Added story selection after choosing a hero.",
    "Added a Family Map Quest that can star any hero.",
    "Added end-of-story choices to pick another story or another hero.",
]


def release_notes_text():
    updates = "\n".join(f"- {note}" for note in RELEASE_NOTES)
    return f"Current version: {APP_VERSION}.\n\nUpdates\n{updates}"


STORY = {
    "start": {
        "title": "Melody Wakes Up Brave",
        "image": "bedroom",
        "text": (
            "Melody the cat woke up in a sunbeam shaped exactly like a pancake. "
            "Her whiskers tingled. Today was clearly an adventure day.\n\n"
            "From the hallway, Callum the dog and Ledger the dinosaur were whispering very loudly. "
            "Callum had a backpack full of snacks. Ledger had a map that was mostly drawn in crayon.\n\n"
            "Mama Bear, their mom, peeked in and said, \"Adventurers need kind hearts.\" "
            "Daddy Monkey, their dad, swung a banana-shaped flashlight onto the hook and said, "
            "\"And a very silly plan.\""
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
            "Mama Bear called from the doorway, \"Breakfast science is best with napkins.\" "
            "Daddy Monkey handed over three napkins and somehow wore one on his head.\n\n"
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
            "The flowers forgot how to giggle. Bring snacks. Love, Mama Bear and Daddy Monkey.\"\n\n"
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
            "In the garden behind Gigi and Papa Gecko's house, the flowers drooped sadly. "
            "Gigi carried extra napkins, and Papa Gecko guarded the snack basket like it was royal treasure.\n\n"
            "Melody gave her bell a tiny jingle. "
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
            "Mama Bear tucked a blanket around all three heroes while Daddy Monkey tiptoed in with warm cocoa.\n\n"
            "Some adventures end with treasure. This one ended with a nap, which Melody knew was even better."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Melody's story again", "start")],
    },
    "parade_ending": {
        "title": "The Living Room Parade",
        "image": "parade",
        "text": (
            "Melody led the grand parade past Sofa Mountain, around the coffee table, and through the blanket fort. "
            "Mama Bear clapped along while Daddy Monkey announced each hero in his fanciest parade voice. "
            "Callum jingled a spoon. Ledger waved the map. Everyone agreed it was the finest parade of the afternoon."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Melody's story again", "start")],
    },
    "picnic_ending": {
        "title": "The Snack Picnic",
        "image": "picnic",
        "text": (
            "The adventurers held a picnic on Gigi and Papa Gecko's blanket. Gigi poured tiny cups "
            "of juice, and Papa Gecko balanced crackers like a tower. Melody got the sunniest spot.\n\n"
            "Callum counted crackers. Ledger gave a tiny speech about teamwork, bravery, and excellent toast shapes."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Melody's story again", "start")],
    },
    "dance_ending": {
        "title": "The Flower Dance",
        "image": "garden",
        "text": (
            "The flowers danced, Callum twirled, Ledger wiggled, and Melody performed one perfect cat leap. "
            "Mama Bear hummed the tune while Daddy Monkey played a spoon like a tiny cymbal. "
            "The Giggle Garden was saved, and the whole day smelled like sunshine."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Melody's story again", "start")],
    },
    "queen_ending": {
        "title": "Queen Melody of Giggles",
        "image": "queen",
        "text": (
            "The flowers crowned Melody with a daisy chain. Mama Bear gave a proud, gentle cheer. "
            "Daddy Monkey bowed so low his tail made a loop. Callum cheered. Ledger carefully wrote, "
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
            "Mama Bear, his mom, pinned on his pretend patrol badge and reminded him that sharing counts as protecting. "
            "Daddy Monkey, his dad, made a trumpet sound into a paper towel tube.\n\n"
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
            "A note from Mama Bear said, \"Saved for brave helpers.\" Daddy Monkey had drawn a smiling banana beside it.\n\n"
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
            "Callum carried the crackers to the Giggle Garden. Mama Bear walked beside him with the picnic blanket, "
            "and Daddy Monkey swung the lanterns just high enough to make the flowers look up.\n\n"
            "The flowers were droopy until he set the snack plate down "
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
            "Gigi got the first thank-you, and Papa Gecko got crumbs in his eyebrows. "
            "Callum got a hero hug.\n\n"
            "The Snack Patrol was officially the coziest team in the house."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Callum's story again", "start")],
    },
    "parade_ending": {
        "title": "The Wagging Victory Parade",
        "image": "parade",
        "text": (
            "Callum led the parade with proud paws and a wagging tail. Melody jingled a bell. "
            "Gigi waved a dish towel like a royal flag, and Papa Gecko marched backward just to be funny. "
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
            "Ledger the dinosaur woke up ready for science. Mama Bear, his mom, packed his green crayon and whispered, "
            "\"Careful explorers notice small wonders.\" Daddy Monkey, his dad, tucked a banana sticker onto the map "
            "and whispered, \"Silly explorers notice big laughs.\"\n\n"
            "Ledger unrolled his map and made his bravest tiny roar.\n\n"
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
            "The flour bag in the pantry looked exactly like a snowy volcano. Mama Bear appeared with a broom and said, "
            "\"Gentle science first.\" Daddy Monkey put on a colander helmet and saluted the volcano.\n\n"
            "Ledger announced that it must be studied "
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
            "The Giggle Garden at Gigi and Papa Gecko's house was quiet. Gigi hummed softly "
            "beside the droopy flowers, and Papa Gecko held Ledger's map open so the breeze could not fold "
            "the important parts.\n\n"
            "Ledger stepped forward and told the flowers his best dinosaur joke: "
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
            "Gigi's humming flowers, Papa Gecko's snack watch, and three heroic friends. "
            "He put a giant star beside his name, then added stars for everyone else too."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Ledger's story again", "start")],
    },
    "dino_parade_ending": {
        "title": "The Tiny Dino Parade",
        "image": "parade",
        "text": (
            "Ledger led the tiniest, proudest dinosaur parade the living room had ever seen. "
            "Mama Bear kept the beat with soft claps, and Daddy Monkey carried the snack banner. "
            "Melody stepped lightly, Callum wagged proudly, and the Dino Expedition Flag waved all the way home."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Ledger's story again", "start")],
    },
}


MILLIE_STORY = {
    "start": {
        "title": "Millie and the Teacup Trail",
        "image": "kitchen",
        "text": (
            "Millie the Bunny arrived for cousin day with a thimble-sized backpack, a blue ribbon, "
            "and a very important hop. She was Melody, Callum, and Ledger's cousin, and she knew "
            "small heroes could find clues that big paws missed.\n\n"
            "Mama Bear set a tiny teacup on the table and said, \"Welcome, Millie.\" Daddy Monkey "
            "balanced a crumb on his nose and whispered, \"The house has been waiting for a bunny-sized mystery.\"\n\n"
            "Auntie Croc, Millie's mom and Daddy Monkey's sister, gave her a careful crocodile smile. "
            "Uncle Zebra, Millie's dad, straightened her ribbon stripes and said, "
            "\"Cousin adventures are best when you hop bravely.\""
        ),
        "choices": [
            ("Inspect the teacup", "teacup_clue"),
            ("Follow the ribbon under the sofa", "sofa_tunnel"),
        ],
    },
    "teacup_clue": {
        "title": "The Teacup Clue",
        "image": "note",
        "text": (
            "Inside the teacup, Millie found a folded note no bigger than a cracker crumb. It said, "
            "\"The Whispering Crumbs need a brave cousin. Bring kindness and a good listening ear.\"\n\n"
            "Melody leaned close, Callum held very still, and Ledger wrote, \"Bunny clues are highly official.\""
        ),
        "choices": [
            ("Listen for whispering crumbs", "crumb_whispers"),
            ("Ask Mama Bear about the note", "mama_advice"),
        ],
    },
    "sofa_tunnel": {
        "title": "The Sofa Tunnel",
        "image": "sofa",
        "text": (
            "Millie followed the ribbon under Sofa Mountain, where the dust looked like fluffy clouds "
            "and a lost button shone like a moon.\n\n"
            "Callum tried to peek underneath and bumped his nose. Millie patted it and said, "
            "\"This is cousin-sized exploring.\""
        ),
        "choices": [
            ("Rescue the moon button", "button_rescue"),
            ("Crawl toward the pantry light", "pantry_path"),
        ],
    },
    "mama_advice": {
        "title": "Mama Bear's Tiny Advice",
        "image": "kitchen",
        "text": (
            "Mama Bear crouched beside Millie and said, \"Tiny paws are perfect for gentle jobs.\" "
            "She tied Millie's blue ribbon into a neat adventure bow.\n\n"
            "Daddy Monkey handed Millie a raisin and called it emergency treasure. Millie accepted, "
            "because every explorer needs supplies.\n\n"
            "\"If the note is tiny,\" Mama Bear said, \"Grandma Mimi and Papa Dave might know what it means. "
            "They keep a whole shelf of tiny things.\""
        ),
        "choices": [
            ("Follow the note to the pantry", "pantry_path"),
            ("Share the raisin with the team", "picnic_ending"),
        ],
    },
    "crumb_whispers": {
        "title": "The Whispering Crumbs",
        "image": "pantry",
        "text": (
            "Millie pressed one ear to the floor. The crumbs whispered, \"This way, this way,\" "
            "in tiny crunchy voices. They led her to a pantry shelf where a jam jar had lost its giggle.\n\n"
            "Ledger gasped. Melody blinked wisely. Callum promised not to eat any clue that was currently talking."
        ),
        "choices": [
            ("Help the jam jar giggle", "jam_giggle"),
            ("Build a crumb bridge", "crumb_bridge"),
        ],
    },
    "button_rescue": {
        "title": "The Moon Button Rescue",
        "image": "laundry",
        "text": (
            "Millie nudged the lost button out from under the sofa. It rolled across the floor and stopped "
            "beside Daddy Monkey's foot.\n\n"
            "\"A moon for the map!\" Grandma Mimi cheered when Millie rolled it onto her tiny-things shelf. "
            "Papa Dave found a bit of string and helped tie the button safely to Millie's map."
        ),
        "choices": [
            ("Add the moon button to the map", "map_ending"),
            ("Follow the button's roll to the pantry", "pantry_path"),
        ],
    },
    "pantry_path": {
        "title": "The Pantry Path",
        "image": "pantry",
        "text": (
            "The pantry smelled like crackers, cinnamon, and adventure. Millie climbed a spoon like a ladder "
            "and found the jam jar hiding behind a flour bag.\n\n"
            "The jar whispered, \"I forgot my giggle, and now the Giggle Garden will be quiet.\""
        ),
        "choices": [
            ("Carry the giggle to the garden", "garden_giggle"),
            ("Ask the crumbs to help", "crumb_bridge"),
        ],
    },
    "crumb_bridge": {
        "title": "The Crumb Bridge",
        "image": "map",
        "text": (
            "Millie lined the crumbs into a tiny bridge across the map. Each crumb pointed toward the garden, "
            "and the moon button made the path shine.\n\n"
            "Melody called it beautiful. Callum called it snack architecture. Ledger called it science with crumbs."
        ),
        "choices": [
            ("March across the crumb bridge", "garden_giggle"),
            ("Save the bridge on the map", "map_ending"),
        ],
    },
    "jam_giggle": {
        "title": "The Jam Jar Giggle",
        "image": "bell",
        "text": (
            "Millie tapped the jar with her tail. Tink, tink, hop! A tiny giggle bubbled up through the jam.\n\n"
            "Daddy Monkey made his silliest face in the shiny lid. Mama Bear hummed a soft song. "
            "The giggle grew warm and bright enough to carry."
        ),
        "choices": [
            ("Bring the giggle to the garden", "garden_giggle"),
            ("Celebrate with a tiny picnic", "picnic_ending"),
        ],
    },
    "garden_giggle": {
        "title": "Millie Saves a Little Giggle",
        "image": "garden",
        "text": (
            "In Grandma Mimi and Papa Dave's window garden, Millie opened the jam jar and released one tiny giggle. "
            "It bounced from flowerpot to flowerpot until the whole windowsill shimmered.\n\n"
            "Melody purred, and Papa Dave added Millie's cousin-sized victory to the map. Grandma Mimi "
            "declared the giggle officially saved."
        ),
        "choices": [
            ("Lead a bunny parade", "parade_ending"),
            ("Draw Millie's path on the map", "map_ending"),
        ],
    },
    "picnic_ending": {
        "title": "Millie's Tiny Picnic",
        "image": "picnic",
        "text": (
            "Millie shared the raisin treasure, the jam jar giggle, and three heroic crumbs. "
            "Grandma Mimi poured juice into the tiniest cup, and Papa Dave made a napkin tent just for her.\n\n"
            "Auntie Croc and Uncle Zebra found cozy spots nearby. "
            "Millie decided cousin day was best when everyone had room at the blanket."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Millie's story again", "start")],
    },
    "map_ending": {
        "title": "Millie's Bunny-Sized Map",
        "image": "map",
        "text": (
            "Millie drew her path with a crumb, a button moon, a teacup, and one bright giggle. "
            "Ledger added labels, Melody added a heart, and Callum added a snack corner.\n\n"
            "Grandma Mimi called it brave. Papa Dave called it tiny-but-mighty. Auntie Croc and Uncle Zebra "
            "asked for a copy to hang on Millie's cousin wall."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Millie's story again", "start")],
    },
    "parade_ending": {
        "title": "The Bunny Hop Parade",
        "image": "parade",
        "text": (
            "Millie led a parade around the table leg, across the blanket, and past the pantry door. "
            "Her tail held the blue ribbon like a flag.\n\n"
            "Grandma Mimi and Papa Dave cheered from the tiny-things shelf, and Auntie Croc and Uncle Zebra "
            "cheered from the front row. "
            "The family cheered for their cousin, and Millie took the smallest, proudest bow."
        ),
        "choices": [("Choose another hero", "character_select"), ("Play Millie's story again", "start")],
    },
}


COUSIN_HEROES = {
    "lily": {
        "name": "Lily",
        "full_name": "Lily the Beaver",
        "animal": "beaver",
        "gift": "building stick bridges",
        "tool": "a bundle of smooth sticks",
        "sound": "tap-tap-build",
        "color": "#8b5e34",
    },
    "mason": {
        "name": "Mason",
        "full_name": "Mason the Dragon",
        "animal": "dragon",
        "gift": "warming lanterns with gentle dragon breath",
        "tool": "a tiny lantern",
        "sound": "whoosh-glow",
        "color": "#b84a62",
    },
    "oliver": {
        "name": "Oliver",
        "full_name": "Oliver the Husky",
        "animal": "husky",
        "gift": "pulling sleds and sniffing snowy clues",
        "tool": "a blue scarf",
        "sound": "ruff-rush",
        "color": "#8da9c4",
    },
    "gemma": {
        "name": "Gemma",
        "full_name": "Gemma the Hedgehog",
        "animal": "hedgehog",
        "gift": "finding tiny clues in cozy corners",
        "tool": "a leaf notebook",
        "sound": "sniff-snuffle",
        "color": "#9b7e5c",
    },
    "nora": {
        "name": "Nora",
        "full_name": "Nora the Kangaroo",
        "animal": "kangaroo",
        "gift": "carrying helpful supplies in her pocket",
        "tool": "a pocket full of buttons",
        "sound": "hop-hop-hooray",
        "color": "#c9865b",
    },
}


def make_cousin_story(hero):
    name = hero["name"]
    full_name = hero["full_name"]
    return {
        "start": {
            "title": f"{name}'s Cousin Club Day",
            "image": "garden",
            "text": (
                f"{full_name} arrived for Cousin Club Day carrying {hero['tool']}. "
                "Aunt Chicken packed a snack pouch, Uncle Panther gave a quiet proud nod, "
                "and the cousins gathered near the family tree.\n\n"
                f"{name} was especially good at {hero['gift']}. Today, that might be exactly what the family needed."
            ),
            "choices": [
                ("Check the family tree map", "family_tree_map"),
                ("Follow the giggle trail", "giggle_trail"),
            ],
        },
        "family_tree_map": {
            "title": "The Wiggly Family Map",
            "image": "map",
            "text": (
                "Gigi and Papa Gecko had drawn a big family map, but one ribbon path had wiggled loose. "
                "Melody held one corner, Ledger read the labels, and Callum guarded the snack bowl.\n\n"
                f"{name} studied the map and spotted where the cousin branch should go."
            ),
            "choices": [
                ("Fix the cousin branch", "cousin_branch"),
                ("Ask Millie to check the tiny labels", "tiny_labels"),
            ],
        },
        "giggle_trail": {
            "title": "The Giggle Trail",
            "image": "hallway",
            "text": (
                "A tiny giggle bounced down the hallway, around a chair leg, and under the picnic blanket. "
                f"{name} followed it carefully, using {hero['tool']} to mark the way.\n\n"
                "Millie hopped beside the trail and whispered, \"Cousin clue detected.\""
            ),
            "choices": [
                ("Track the giggle to the garden", "garden_helper"),
                ("Build a tiny clue station", "cousin_branch"),
            ],
        },
        "cousin_branch": {
            "title": "The Cousin Branch",
            "image": "supplies",
            "text": (
                f"{name} used {hero['gift']} to help put every cousin in the right place. "
                "Lily, Mason, Oliver, Gemma, Nora, Melody, Callum, Ledger, and Millie all got their own spot.\n\n"
                f"Then {name} made the official family-helper sound: \"{hero['sound']}!\""
            ),
            "choices": [
                ("Bring the fixed branch to the garden", "garden_helper"),
                ("Celebrate with a cousin parade", "parade_ending"),
            ],
        },
        "tiny_labels": {
            "title": "Millie's Tiny Labels",
            "image": "note",
            "text": (
                "Millie found the tiniest labels tucked inside a teacup. One said Cousins. One said Aunt Chicken. "
                "One said Uncle Panther.\n\n"
                f"{name} placed them carefully while Gemma checked the corners and Mason warmed the glue just enough."
            ),
            "choices": [
                ("Finish the family map", "map_ending"),
                ("Take the labels to the garden", "garden_helper"),
            ],
        },
        "garden_helper": {
            "title": f"{name} Helps the Garden",
            "image": "garden",
            "text": (
                "The garden flowers had been waiting for the family names to settle. "
                f"When {name} brought the fixed cousin branch, every flower leaned closer to listen.\n\n"
                f"{name} shared {hero['tool']}, and the garden answered with a warm little giggle."
            ),
            "choices": [
                ("Save the family giggle", "map_ending"),
                ("Lead a cousin parade", "parade_ending"),
            ],
        },
        "map_ending": {
            "title": f"{name}'s Family Map",
            "image": "map",
            "text": (
                f"{name} helped finish the family map. It showed grandparents, parents, aunts, uncles, "
                "siblings, and cousins all connected with bright careful lines.\n\n"
                "Mama Bear called it beautiful. Daddy Monkey called it official. The cousins called it theirs."
            ),
            "choices": [("Choose another hero", "character_select"), (f"Play {name}'s story again", "start")],
        },
        "parade_ending": {
            "title": f"{name}'s Cousin Parade",
            "image": "parade",
            "text": (
                f"{name} led a cousin parade past the family tree, around the snack blanket, and through the garden path. "
                "Everyone had a part: builders, hoppers, sniffers, map-makers, and giggle-carriers.\n\n"
                "The whole family cheered, because every good adventure has room for one more cousin story."
            ),
            "choices": [("Choose another hero", "character_select"), (f"Play {name}'s story again", "start")],
        },
    }


STORIES = {
    "melody": STORY,
    "callum": CALLUM_STORY,
    "ledger": LEDGER_STORY,
    "millie": MILLIE_STORY,
}
STORIES.update({key: make_cousin_story(hero) for key, hero in COUSIN_HEROES.items()})


HERO_STORY_DETAILS = {
    "melody": {
        "full_name": "Melody the Cat",
        "gift": "finding cozy clues with brave little paws",
        "tool": "a jingly adventure bell",
        "sound": "jingle-jingle-brave",
    },
    "callum": {
        "full_name": "Callum the Dog",
        "gift": "sniffing out snack emergencies",
        "tool": "a backpack full of crackers",
        "sound": "ruff-rescue",
    },
    "ledger": {
        "full_name": "Ledger the Dinosaur",
        "gift": "reading maps and naming important discoveries",
        "tool": "a crayon map",
        "sound": "rawr-research",
    },
    "millie": {
        "full_name": "Millie the Bunny",
        "gift": "finding tiny clues in tiny places",
        "tool": "a blue ribbon",
        "sound": "hop-hop-found-it",
    },
}
HERO_STORY_DETAILS.update(
    {
        key: {
            "full_name": hero["full_name"],
            "gift": hero["gift"],
            "tool": hero["tool"],
            "sound": hero["sound"],
        }
        for key, hero in COUSIN_HEROES.items()
    }
)


def make_family_map_story(hero):
    name = hero["full_name"].split()[0]
    return {
        "start": {
            "title": f"{name}'s Family Map Quest",
            "image": "map",
            "text": (
                f"{hero['full_name']} found a big family map spread across the living room rug. "
                "Some of the bright ribbon paths had slipped loose, and nobody could tell which way "
                "led to the snack table, the garden, or the cozy story blanket.\n\n"
                f"{name} knew this was a job for {hero['gift']}."
            ),
            "choices": [
                ("Follow the loose ribbon path", "ribbon_path"),
                ("Ask the family for clues", "family_clues"),
            ],
        },
        "ribbon_path": {
            "title": "The Loose Ribbon Path",
            "image": "hallway",
            "text": (
                f"{name} followed the ribbon past the sofa, around the toy basket, and under one very "
                "wiggly blanket corner. Melody held one end, Callum guarded the snacks, and Ledger "
                "announced that the path was officially mysterious.\n\n"
                f"At the end of the ribbon sat {hero['tool']} with a note tucked beside it."
            ),
            "choices": [
                ("Read the tucked-away note", "note_clue"),
                ("Carry the tool to the garden", "garden_fix"),
            ],
        },
        "family_clues": {
            "title": "Everybody Helps",
            "image": "supplies",
            "text": (
                "Mama Bear remembered the garden path. Daddy Monkey remembered the silly shortcut. "
                "Gigi and Papa Gecko remembered where the picnic blanket belonged.\n\n"
                f"{name} listened carefully, then made the official helper sound: \"{hero['sound']}!\""
            ),
            "choices": [
                ("Add the clues to the map", "map_fix"),
                ("Bring everyone to the garden", "garden_fix"),
            ],
        },
        "note_clue": {
            "title": "A Note From the Map",
            "image": "note",
            "text": (
                "The note said, \"A family map works best when everybody gets a place and every place "
                "gets a giggle.\"\n\n"
                f"{name} smiled, because that sounded like exactly the kind of puzzle a family could solve together."
            ),
            "choices": [
                ("Fix the family map", "map_fix"),
                ("Test the path in the garden", "garden_fix"),
            ],
        },
        "map_fix": {
            "title": "The Map Comes Together",
            "image": "map",
            "text": (
                f"{name} placed every ribbon carefully. Melody got the sunbeam path, Callum got the "
                "snack path, Ledger got the discovery path, and Millie got the tiny clue path.\n\n"
                "The map shimmered with happy colors. It was ready for a parade."
            ),
            "choices": [
                ("Lead a map parade", "parade_ending"),
                ("Save the map for story time", "story_blanket_ending"),
            ],
        },
        "garden_fix": {
            "title": "The Garden Path",
            "image": "garden",
            "text": (
                f"{name} carried the map outside, where the flowers leaned close to see. "
                "When the last ribbon path touched the garden gate, every flower gave a tiny giggle.\n\n"
                "The family clapped, because the map had found its way home."
            ),
            "choices": [
                ("Celebrate with flower giggles", "garden_ending"),
                ("Take the map back inside", "story_blanket_ending"),
            ],
        },
        "parade_ending": {
            "title": f"{name}'s Map Parade",
            "image": "parade",
            "text": (
                f"{name} led the family around the whole map route: past Sofa Mountain, through the "
                "blanket tunnel, around the snack table, and all the way to the garden door.\n\n"
                "Every ribbon stayed in place, and every helper got a cheer."
            ),
            "choices": [("Choose another story", "story_select"), ("Choose another hero", "character_select"), ("Play this story again", "start")],
        },
        "garden_ending": {
            "title": "The Giggle Path",
            "image": "garden",
            "text": (
                "The flowers giggled so brightly that the whole garden seemed to sparkle. "
                f"{name} gave a proud little nod, and the family map became the official guide "
                "for all future cozy adventures."
            ),
            "choices": [("Choose another story", "story_select"), ("Choose another hero", "character_select"), ("Play this story again", "start")],
        },
        "story_blanket_ending": {
            "title": "The Story Blanket",
            "image": "nap",
            "text": (
                "Back inside, Mama Bear spread the cozy story blanket over everyone. Daddy Monkey "
                "used the map to tell a very silly tale with three snack breaks.\n\n"
                f"{name} rested beside the finished map, ready for the next adventure."
            ),
            "choices": [("Choose another story", "story_select"), ("Choose another hero", "character_select"), ("Play this story again", "start")],
        },
    }


BRIEF_CHARACTER_IDS = {
    "Melody": "melody",
    "Callum": "callum",
    "Ledger": "ledger",
    "Millie": "millie",
}


def clean_brief_text(text):
    replacements = {
        "â€œ": "\"",
        "â€": "\"",
        "â€™": "'",
        "â€˜": "'",
        "â€\"": "-",
        "â€“": "-",
        "â€”": "-",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text.strip()


def find_story_brief():
    candidates = [
        Path.cwd() / "FFA_character_branching_stories_for_codex(1).md",
        Path.cwd() / "FFA_character_branching_stories_for_codex.md",
    ]
    downloads = Path.home() / "Downloads"
    if downloads.exists():
        candidates.extend(
            sorted(
                downloads.glob("FFA_character_branching_stories_for_codex*.md"),
                key=lambda path: path.stat().st_mtime,
                reverse=True,
            )
        )

    for path in candidates:
        if not path.exists():
            continue
        for encoding in ("utf-8", "cp1252"):
            try:
                return path, clean_brief_text(path.read_text(encoding=encoding))
            except UnicodeDecodeError:
                continue
    return None, ""


def markdown_section(body, heading):
    pattern = rf"^### {re.escape(heading)}\s*$"
    match = re.search(pattern, body, re.MULTILINE)
    if not match:
        return ""
    next_heading = re.search(r"^### ", body[match.end():], re.MULTILINE)
    end = match.end() + next_heading.start() if next_heading else len(body)
    return body[match.end():end].strip()


def outcome_text(choice_body):
    lines = []
    for line in choice_body.strip().splitlines():
        stripped = line.strip()
        if not stripped:
            lines.append("")
            continue
        if re.match(r"^(Outcome|[A-Za-z -]+ ending):$", stripped):
            continue
        lines.append(stripped)
    text = "\n".join(lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def brief_image_for(title, text):
    lower_text = f"{title} {text}".lower()
    image_keywords = [
        ("pie", "kitchen"),
        ("violin", "note"),
        ("lantern", "hallway"),
        ("attic", "bedroom"),
        ("kitten", "garden"),
        ("bull", "garden"),
        ("race", "hallway"),
        ("cave", "fort"),
        ("garden", "garden"),
        ("medicine", "supplies"),
        ("tea", "picnic"),
        ("roar", "fort"),
        ("bridge", "map"),
        ("rock", "treasure"),
        ("picnic", "picnic"),
        ("cheese", "kitchen"),
        ("library", "note"),
        ("storm drain", "garden"),
        ("clocktower", "map"),
        ("map", "map"),
    ]
    for keyword, image in image_keywords:
        if keyword in lower_text:
            return image
    return "garden"


def make_brief_story(story_title, lesson, premise, starting_scene, choices):
    scenes = {
        "start": {
            "title": story_title,
            "image": brief_image_for(story_title, starting_scene),
            "text": starting_scene,
            "choices": [
                (choice["label"], f"choice_{index}")
                for index, choice in enumerate(choices, start=1)
            ],
        }
    }

    for index, choice in enumerate(choices, start=1):
        choice_text = outcome_text(choice["body"])
        scenes[f"choice_{index}"] = {
            "title": choice["label"],
            "image": brief_image_for(choice["label"], choice_text),
            "text": choice_text,
            "choices": [
                ("Choose another story", "story_select"),
                ("Choose another hero", "character_select"),
                ("Play this story again", "start"),
            ],
        }

    description = lesson or premise or "A gentle branching adventure from the updated story brief."
    return {
        "title": story_title,
        "description": description,
        "scenes": scenes,
    }


def parse_brief_stories():
    _, text = find_story_brief()
    if not text:
        return {}

    stories_by_character = {character_id: [] for character_id in BRIEF_CHARACTER_IDS.values()}
    story_pattern = re.compile(
        r"^## (?P<character>Melody|Callum|Ledger|Millie) Story (?P<number>\d+): (?P<title>.+?)\s*$",
        re.MULTILINE,
    )
    matches = list(story_pattern.finditer(text))

    for index, match in enumerate(matches):
        body_start = match.end()
        body_end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        body = text[body_start:body_end]
        lesson = markdown_section(body, "Lesson")
        premise = markdown_section(body, "Premise")
        starting_scene = markdown_section(body, "Starting Scene")
        choices_section = markdown_section(body, "Branching Choices")
        choice_matches = list(
            re.finditer(r"^#### Choice [A-Z]: (?P<label>.+?)\s*$", choices_section, re.MULTILINE)
        )
        choices = []
        for choice_index, choice_match in enumerate(choice_matches):
            choice_start = choice_match.end()
            choice_end = (
                choice_matches[choice_index + 1].start()
                if choice_index + 1 < len(choice_matches)
                else len(choices_section)
            )
            choices.append(
                {
                    "label": choice_match.group("label").strip(),
                    "body": choices_section[choice_start:choice_end].strip(),
                }
            )

        if starting_scene and choices:
            character_id = BRIEF_CHARACTER_IDS[match.group("character")]
            story = make_brief_story(
                match.group("title").strip(),
                lesson,
                premise,
                starting_scene,
                choices,
            )
            story["id"] = f"brief_{match.group('character').lower()}_{match.group('number')}"
            stories_by_character[character_id].append(story)

    return stories_by_character


STORY_OPTIONS = {
    character_id: [
        {
            "id": "signature",
            "title": STORIES[character_id]["start"]["title"],
            "description": f"A special adventure starring {HERO_STORY_DETAILS[character_id]['full_name']}.",
            "button": "Play the special adventure",
            "scenes": STORIES[character_id],
        },
        {
            "id": "family_map",
            "title": f"{HERO_STORY_DETAILS[character_id]['full_name'].split()[0]}'s Family Map Quest",
            "description": "A family helper adventure about fixing the map and finding the giggle path.",
            "button": "Play the family map quest",
            "scenes": make_family_map_story(HERO_STORY_DETAILS[character_id]),
        },
    ]
    for character_id in STORIES
}

for character_id, brief_stories in parse_brief_stories().items():
    STORY_OPTIONS[character_id].extend(
        {
            "id": story["id"],
            "title": story["title"],
            "description": story["description"],
            "button": f"Play {story['title']}",
            "scenes": story["scenes"],
        }
        for story in brief_stories
    )


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
    "millie": {
        "name": "Millie",
        "description": "Millie the curious bunny cousin",
        "button": "Play as Millie the bunny",
    },
}
CHARACTERS.update(
    {
        key: {
            "name": hero["name"],
            "description": hero["full_name"],
            "button": f"Play as {hero['full_name']}",
        }
        for key, hero in COUSIN_HEROES.items()
    }
)


PLAYABLE_CHARACTER_ORDER = [
    "melody",
    "callum",
    "ledger",
    "millie",
    "lily",
    "mason",
    "oliver",
    "gemma",
    "nora",
]


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
        self.current_story_id = None
        self.current_story_scenes = None
        self.current_scene = "start"
        self.history = []
        self.character_select_art = None
        self.sprite_images = {}

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
            text=f"A gentle read-along adventure with the whole family. Current version: {APP_VERSION}.",
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

        self.release_notes = tk.Message(
            self.story_panel,
            text=release_notes_text(),
            font=("Segoe UI", 10),
            bg="#fff4dc",
            fg="#5f4a34",
            width=520,
            padx=12,
            pady=10,
            relief="flat",
        )

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

        art_path = Path(__file__).with_name("assets") / "character-cards.png"
        if art_path.exists():
            self.character_select_art = tk.PhotoImage(file=str(art_path))
        sprite_root = Path(__file__).with_name("assets") / "sprites"
        for character_id in PLAYABLE_CHARACTER_ORDER:
            variants = {}
            for size in ["small", "medium", "large"]:
                sprite_path = sprite_root / f"{character_id}-{size}.png"
                if sprite_path.exists():
                    variants[size] = tk.PhotoImage(file=str(sprite_path))
            if variants:
                self.sprite_images[character_id] = variants

        self.show_character_select()

    def show_character_select(self):
        self.current_character = None
        self.current_story_id = None
        self.current_story_scenes = None
        self.current_scene = "character_select"
        self.history = []
        self.canvas.pack_forget()
        self.story_panel.pack_configure(expand=True)
        self.scene_title.config(text="Choose Your Hero")
        self.scene_title.config(justify="center")
        self.scene_title.pack_configure(anchor="center")
        self.story_text.config(justify="center", width=520)
        self.story_text.pack_configure(anchor="center")
        self.story_text.config(
            text=(
                "Pick who should lead this adventure. Each hero has their own story arc, "
                "with the family still helping each other along the way."
            )
        )
        self.show_release_notes(anchor="center")

        for child in self.choices_frame.winfo_children():
            child.destroy()

        for character_id, info in CHARACTERS.items():
            sprite = self.sprite_images.get(character_id, {}).get("medium")
            button = tk.Button(
                self.choices_frame,
                text=info["button"],
                image=sprite,
                compound="right",
                font=self.button_font,
                command=lambda hero=character_id: self.show_story_select(hero, reset_history=True),
                bg="#88d498",
                fg="#17351f",
                activebackground="#6cc57e",
                relief="flat",
                padx=14,
                pady=8,
                wraplength=360,
                justify="left",
                height=78,
            )
            button.pack(fill="x", pady=5)

        self.back_button.config(state="disabled")
        self.draw_character_select()

    def show_story_select(self, character_id=None, reset_history=False):
        character_changed = character_id is not None and character_id != self.current_character
        if character_id is not None:
            self.current_character = character_id
        if not self.current_character:
            self.show_character_select()
            return

        if reset_history or character_changed:
            self.current_story_id = None
            self.current_story_scenes = None
        self.current_scene = "story_select"
        if reset_history:
            self.history = ["character_select"]

        self.canvas.pack_forget()
        self.story_panel.pack_configure(expand=True)
        hero_name = CHARACTERS[self.current_character]["name"]
        self.scene_title.config(text=f"Choose {hero_name}'s Story")
        self.scene_title.config(justify="center")
        self.scene_title.pack_configure(anchor="center")
        self.story_text.config(justify="center", width=520)
        self.story_text.pack_configure(anchor="center")
        self.story_text.config(text="Pick which adventure to read and play together.")
        self.show_release_notes(anchor="center")

        for child in self.choices_frame.winfo_children():
            child.destroy()

        for story in STORY_OPTIONS[self.current_character]:
            button = tk.Button(
                self.choices_frame,
                text=f"{story['title']}\n{story['description']}",
                font=self.button_font,
                command=lambda story_id=story["id"]: self.start_story(self.current_character, story_id),
                bg="#88d498",
                fg="#17351f",
                activebackground="#6cc57e",
                relief="flat",
                padx=14,
                pady=10,
                wraplength=460,
                justify="left",
            )
            button.pack(fill="x", pady=6)

        self.back_button.config(state="normal")
        self.draw_story_select()

    def start_story(self, character_id, story_id):
        self.current_character = character_id
        story = self.find_story_option(character_id, story_id)
        self.current_story_id = story_id
        self.current_story_scenes = story["scenes"]
        self.history = []
        self.show_scene("start", remember=False)

    def show_scene(self, scene_id, remember=True):
        if scene_id == "character_select":
            self.show_character_select()
            return
        if scene_id == "story_select":
            if remember:
                self.history.append(self.current_scene)
            self.show_story_select()
            return
        if self.current_story_scenes is None:
            self.show_story_select(self.current_character, reset_history=True)
            return
        self.hide_release_notes()

        if not self.canvas.winfo_ismapped():
            self.story_panel.pack_forget()
            self.canvas.pack(side="left", fill="both", expand=False, padx=(0, 18))
            self.story_panel.pack(side="left", fill="both", expand=True)
            self.scene_title.config(justify="left")
            self.scene_title.pack_configure(anchor="w")
            self.story_text.config(justify="left", width=430)
            self.story_text.pack_configure(anchor="w")

        if remember:
            self.history.append(self.current_scene)

        self.current_scene = scene_id
        scene = self.current_story_scenes[scene_id]
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
        self.draw_scene(scene)

    def go_back(self):
        if not self.history:
            return
        previous = self.history.pop()
        self.show_scene(previous, remember=False)

    def find_story_option(self, character_id, story_id):
        for story in STORY_OPTIONS[character_id]:
            if story["id"] == story_id:
                return story
        return STORY_OPTIONS[character_id][0]

    def show_release_notes(self, anchor="w"):
        self.release_notes.config(text=release_notes_text())
        self.release_notes.pack(anchor=anchor, fill="x", pady=(12, 0))

    def hide_release_notes(self):
        self.release_notes.pack_forget()

    def draw_character_select(self):
        self.canvas.delete("all")
        if self.character_select_art:
            self.canvas.create_rectangle(0, 0, 360, 300, fill="#fffaf0", outline="")
            self.canvas.create_image(180, 150, image=self.character_select_art)
            return

        self.canvas.create_rectangle(0, 0, 360, 300, fill="#fff1a8", outline="")
        self.canvas.create_oval(-70, -70, 150, 112, fill="#ffffff", outline="")
        self.canvas.create_oval(220, 185, 460, 370, fill="#ffffff", outline="")
        self.draw_stars("#f4a261", "#ff70a6")
        lineup = [
            ("melody", 70, 82, 0.38),
            ("callum", 180, 82, 0.38),
            ("ledger", 290, 82, 0.36),
            ("millie", 70, 168, 0.42),
            ("lily", 180, 168, 0.38),
            ("mason", 290, 168, 0.38),
            ("oliver", 70, 252, 0.38),
            ("gemma", 180, 252, 0.38),
            ("nora", 290, 252, 0.38),
        ]
        for character_id, x, y, scale in lineup:
            self.draw_character(character_id, x, y, scale)

    def draw_story_select(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, 360, 300, fill="#fff1a8", outline="")
        self.canvas.create_oval(-70, -70, 150, 112, fill="#ffffff", outline="")
        self.canvas.create_oval(220, 185, 460, 370, fill="#ffffff", outline="")
        self.draw_stars("#f4a261", "#ff70a6")
        if self.current_character:
            self.draw_character(self.current_character, 180, 170, 0.72)
        self.canvas.create_text(
            180,
            42,
            text="Which story today?",
            font=("Georgia", 18, "bold"),
            fill="#4a3b2a",
        )

    def draw_scene(self, scene):
        self.canvas.delete("all")
        image_key = scene["image"]
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

        self.draw_adventurers(scene)

        if image_key == "queen":
            self.canvas.create_arc(135, 63, 222, 122, start=0, extent=180, style="arc", width=4, outline="#f9c74f")
            for x, y in [(147, 81), (178, 66), (209, 81)]:
                self.canvas.create_oval(x - 8, y - 8, x + 8, y + 8, fill="#f9c74f", outline="#c08700")

    def draw_adventurers(self, scene):
        hero = self.current_character if self.current_character in PLAYABLE_CHARACTER_ORDER else "melody"
        side_characters = [character_id for character_id in self.active_scene_characters(scene) if character_id != hero]
        left_side = side_characters[:4]
        right_side = side_characters[4:]

        for index, character_id in enumerate(left_side):
            self.draw_character(character_id, 58, self.side_row_y(index, len(left_side)), 0.33)

        for index, character_id in enumerate(right_side):
            self.draw_character(character_id, 302, self.side_row_y(index, len(right_side)), 0.33)

        hero_scale = 0.78
        if hero == "millie":
            hero_scale = 0.9
        elif hero == "ledger":
            hero_scale = 0.74
        elif hero in COUSIN_HEROES:
            hero_scale = 0.82

        self.draw_character(hero, 180, 198, hero_scale)

    def active_scene_characters(self, scene):
        scene_text = " ".join(
            [
                scene["title"],
                scene["text"],
                " ".join(label for label, _ in scene["choices"]),
            ]
        ).lower()
        active = [self.current_character] if self.current_character else []
        for character_id in PLAYABLE_CHARACTER_ORDER:
            info = CHARACTERS[character_id]
            names = {info["name"].lower(), info["description"].lower()}
            if character_id in COUSIN_HEROES:
                names.add(COUSIN_HEROES[character_id]["full_name"].lower())
            if any(name in scene_text for name in names):
                active.append(character_id)
        return [character_id for character_id in PLAYABLE_CHARACTER_ORDER if character_id in set(active)]

    def side_row_y(self, index, total):
        if total <= 1:
            return 116
        if total == 2:
            return [88, 162][index]
        if total == 3:
            return [66, 126, 186][index]
        return [54, 104, 154, 204][index]

    def draw_character(self, character_id, x, y, scale):
        if self.draw_sprite_character(character_id, x, y, scale):
            return

        if character_id == "melody":
            self.draw_cat(x, y, scale=scale, body="#f4a261", stripes="#bc6c25", name="Melody")
        elif character_id == "callum":
            self.draw_dog(x, y, scale=scale, name="Callum")
        elif character_id == "ledger":
            self.draw_dino(x, y, scale=scale, name="Ledger")
        elif character_id == "millie":
            self.draw_bunny(x, y, scale=scale, name="Millie")
        elif character_id in COUSIN_HEROES:
            self.draw_cousin(character_id, x, y, scale)

    def draw_sprite_character(self, character_id, x, y, scale):
        variants = self.sprite_images.get(character_id)
        if not variants:
            return False
        if scale <= 0.45:
            size = "small"
        elif scale <= 0.65:
            size = "medium"
        else:
            size = "large"
        image = variants.get(size) or variants.get("large") or next(iter(variants.values()))
        bottom = y + 90 * scale
        self.canvas.create_image(x, bottom, image=image, anchor="s")
        self.canvas.create_text(
            x,
            bottom + 12,
            text=CHARACTERS[character_id]["name"],
            fill="#3f3428",
            font=("Segoe UI", max(8, int(11 * scale)), "bold"),
        )
        return True

    def draw_cousin(self, character_id, x, y, scale):
        hero = COUSIN_HEROES[character_id]
        name = hero["name"]
        body = hero["color"]
        outline = "#5c4033"
        s = scale
        self.canvas.create_oval(x - 48 * s, y - 4 * s, x + 48 * s, y + 74 * s, fill=body, outline=outline, width=2)
        self.canvas.create_oval(x - 36 * s, y - 62 * s, x + 36 * s, y + 6 * s, fill=body, outline=outline, width=2)

        if character_id == "lily":
            self.canvas.create_oval(x - 47 * s, y - 45 * s, x - 25 * s, y - 19 * s, fill=body, outline=outline, width=2)
            self.canvas.create_oval(x + 25 * s, y - 45 * s, x + 47 * s, y - 19 * s, fill=body, outline=outline, width=2)
            self.canvas.create_oval(x - 16 * s, y - 30 * s, x + 16 * s, y - 10 * s, fill="#d7b38c", outline=outline)
            self.canvas.create_arc(x + 36 * s, y + 22 * s, x + 88 * s, y + 72 * s, start=95, extent=225, style="arc", outline="#6f4d2f", width=max(5, int(10 * s)))
        elif character_id == "mason":
            self.canvas.create_polygon(x - 34 * s, y - 40 * s, x - 18 * s, y - 86 * s, x - 5 * s, y - 43 * s, fill=body, outline=outline)
            self.canvas.create_polygon(x + 34 * s, y - 40 * s, x + 18 * s, y - 86 * s, x + 5 * s, y - 43 * s, fill=body, outline=outline)
            for offset in [-24, 0, 24]:
                self.canvas.create_polygon(x + offset * s, y - 70 * s, x + (offset + 8) * s, y - 88 * s, x + (offset + 16) * s, y - 70 * s, fill="#f7c948", outline=outline)
            self.canvas.create_arc(x + 32 * s, y + 12 * s, x + 92 * s, y + 76 * s, start=90, extent=220, style="arc", outline=body, width=max(5, int(10 * s)))
        elif character_id == "oliver":
            self.canvas.create_polygon(x - 33 * s, y - 42 * s, x - 20 * s, y - 82 * s, x - 4 * s, y - 44 * s, fill="#f7f7f7", outline=outline)
            self.canvas.create_polygon(x + 33 * s, y - 42 * s, x + 20 * s, y - 82 * s, x + 4 * s, y - 44 * s, fill="#f7f7f7", outline=outline)
            self.canvas.create_oval(x - 24 * s, y - 48 * s, x + 24 * s, y - 8 * s, fill="#f7f7f7", outline="")
            self.canvas.create_line(x - 28 * s, y + 6 * s, x + 28 * s, y + 6 * s, fill="#457b9d", width=max(4, int(7 * s)))
        elif character_id == "gemma":
            for offset in [-28, -14, 0, 14, 28]:
                self.canvas.create_line(x + offset * s, y - 74 * s, x + (offset - 8) * s, y - 55 * s, fill="#3f3428", width=max(1, int(2 * s)))
            self.canvas.create_oval(x - 20 * s, y - 32 * s, x + 20 * s, y - 12 * s, fill="#f4d1ae", outline=outline)
        elif character_id == "nora":
            self.canvas.create_oval(x - 35 * s, y - 94 * s, x - 18 * s, y - 40 * s, fill=body, outline=outline, width=2)
            self.canvas.create_oval(x + 18 * s, y - 94 * s, x + 35 * s, y - 40 * s, fill=body, outline=outline, width=2)
            self.canvas.create_oval(x - 20 * s, y + 26 * s, x + 20 * s, y + 62 * s, fill="#f6d7b0", outline=outline)
            self.canvas.create_line(x + 38 * s, y + 26 * s, x + 78 * s, y + 65 * s, fill=outline, width=max(3, int(5 * s)))

        self.canvas.create_oval(x - 15 * s, y - 36 * s, x - 5 * s, y - 26 * s, fill="#243b53", outline="")
        self.canvas.create_oval(x + 5 * s, y - 36 * s, x + 15 * s, y - 26 * s, fill="#243b53", outline="")
        self.canvas.create_oval(x - 4 * s, y - 20 * s, x + 4 * s, y - 12 * s, fill=outline, outline="")
        self.canvas.create_arc(x - 12 * s, y - 18 * s, x + 12 * s, y - 2 * s, start=200, extent=140, style="arc", outline=outline, width=2)
        self.canvas.create_text(x, y + 92 * s, text=name, fill="#3f3428", font=("Segoe UI", max(8, int(11 * s)), "bold"))

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

    def draw_bunny(self, x, y, scale, name):
        s = scale
        body = "#d7d0c8"
        outline = "#5c514b"
        ear = "#f4bfc2"
        self.canvas.create_oval(x - 40 * s, y - 2 * s, x + 42 * s, y + 58 * s, fill=body, outline=outline, width=2)
        self.canvas.create_oval(x - 32 * s, y - 58 * s, x + 32 * s, y + 6 * s, fill=body, outline=outline, width=2)
        self.canvas.create_oval(x - 32 * s, y - 118 * s, x - 10 * s, y - 50 * s, fill=body, outline=outline, width=2)
        self.canvas.create_oval(x + 10 * s, y - 118 * s, x + 32 * s, y - 50 * s, fill=body, outline=outline, width=2)
        self.canvas.create_oval(x - 27 * s, y - 106 * s, x - 15 * s, y - 60 * s, fill=ear, outline="")
        self.canvas.create_oval(x + 15 * s, y - 106 * s, x + 27 * s, y - 60 * s, fill=ear, outline="")
        self.canvas.create_oval(x - 13 * s, y - 34 * s, x - 5 * s, y - 26 * s, fill="#1f2933", outline="")
        self.canvas.create_oval(x + 5 * s, y - 34 * s, x + 13 * s, y - 26 * s, fill="#1f2933", outline="")
        self.canvas.create_oval(x - 4 * s, y - 20 * s, x + 4 * s, y - 12 * s, fill="#7d4f50", outline="")
        for side in [-1, 1]:
            self.canvas.create_line(x + side * 3 * s, y - 16 * s, x + side * 32 * s, y - 23 * s, fill=outline)
            self.canvas.create_line(x + side * 3 * s, y - 13 * s, x + side * 34 * s, y - 12 * s, fill=outline)
        self.canvas.create_oval(x + 24 * s, y + 34 * s, x + 48 * s, y + 58 * s, fill="#ffffff", outline=outline, width=1)
        self.canvas.create_line(x - 22 * s, y + 12 * s, x + 20 * s, y + 12 * s, fill="#7aa7c7", width=max(3, int(5 * s)))
        self.canvas.create_text(x, y + 78 * s, text=name, fill="#3f3428", font=("Segoe UI", max(9, int(11 * s)), "bold"))

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
