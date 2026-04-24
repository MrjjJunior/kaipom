# kaipom

Made from joining the two words, Kaizen (Japanese philosophy of continous improvement) & Pomdoro, is command‑line study t that uses the Pomodoro Technique to help you focus, track your learning, and revisit what you’ve studied.

## Features

- **Pomodoro timer** – Start a 25 or 50 minute focus session, optionally set a total study duration (1–6 hours) with automatic breaks.
- **Study notes** – Add notes after each session. View all notes (latest first) or filter by date.
<!-- - **Quiz** – Generate a simple quiz from your own notes (local only, no external APIs). -->

## Commands

```bash
# Start a Pomodoro
study-cli study 25 --hour 2

# Add a note
study-cli notes --add "Learned about list comprehensions"

# View notes
study-cli notes


