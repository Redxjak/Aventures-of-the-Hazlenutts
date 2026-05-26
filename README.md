# Aventures of the Hazlenutts

A kid-friendly, mostly text-based Python adventure game starring Melody the cat, Callum the dog, Ledger the dinosaur, Millie the bunny cousin, and the wider Hazlenutts family.

## How to Play

Run:

```powershell
python app.py
```

Choose Melody, Callum, Ledger, or Millie as the hero. Then read each scene together and click one of the choice buttons to decide where the adventure goes next.

## What Is Included

- A gentle branching story with multiple endings
- A hero selection screen
- Separate story arcs for Melody, Callum, Ledger, and Millie
- Funny, safe adventures around the house and garden
- Melody as the main cat hero
- Callum as a friendly German shepherd-style dog
- Ledger as a tiny T. rex-style dinosaur
- Millie as their curious bunny cousin
- Mama Bear as the kids' caring mom
- Daddy Monkey as their silly dad
- Grandma GiGi and Papa Troy as Mama Bear's parents, featured in some Melody, Callum, and Ledger adventures
- Grandma Mimi and Papa Dave as Daddy Monkey's parents, featured in some Millie and Melody adventures
- Auntie Croc as Daddy Monkey's sister and Millie's mom
- Uncle Zebra as Millie's dad
- Built-in character illustrations drawn directly in the Python GUI
- No internet connection or extra packages required

## Future Browser Version

The story is stored separately from the GUI in the `STORY` dictionary inside `app.py`. That makes it easier to move later into a browser version, where the same scenes and choices could become JSON and be displayed with HTML, CSS, and JavaScript.

Good next steps for a tablet-friendly browser version:

- Move the `STORY` data into `story.json`
- Recreate the screen with HTML buttons and a large readable story panel
- Draw the cats with HTML canvas or use image files
- Add large touch targets for tablet play
