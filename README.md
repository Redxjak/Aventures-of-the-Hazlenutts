# Aventures of the Hazlenutts

A kid-friendly, mostly text-based Python adventure game starring Melody the cat, with Callum the dog and Ledger the dinosaur as side characters.

## How to Play

Run:

```powershell
python app.py
```

Choose Melody, Callum, or Ledger as the hero. Then read each scene together and click one of the choice buttons to decide where the adventure goes next.

## What Is Included

- A gentle branching story with multiple endings
- A hero selection screen
- Separate story arcs for Melody, Callum, and Ledger
- Funny, safe adventures around the house and garden
- Melody as the main cat hero
- Callum as a friendly German shepherd-style dog
- Ledger as a tiny T. rex-style dinosaur
- Built-in character illustrations drawn directly in the Python GUI
- No internet connection or extra packages required

## Future Browser Version

The story is stored separately from the GUI in the `STORY` dictionary inside `app.py`. That makes it easier to move later into a browser version, where the same scenes and choices could become JSON and be displayed with HTML, CSS, and JavaScript.

Good next steps for a tablet-friendly browser version:

- Move the `STORY` data into `story.json`
- Recreate the screen with HTML buttons and a large readable story panel
- Draw the cats with HTML canvas or use image files
- Add large touch targets for tablet play
