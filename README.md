# Which Board Game Are You?

A goof personality quiz. People answer 10 questions about board games (plus a few random ones like green or blue, Apple or Android) and get a very official-looking result. The result is always Monopoly, with a random "flavor" (The Top Hat, The Banker, Free Parking House Rules, and so on). Retaking it gets a smug "Still Monopoly" message.

**Live link:** https://jimmyhudsonclaude.github.io/board-game-quiz/

To update the live site, ask Hoid to "push the quiz changes." It goes live a minute or two later.

## How to open it

Double-click `index.html`. It opens in your web browser. That's the whole app, one file.

## How to change things

Open `index.html` in any text editor (TextEdit works). Near the bottom are clearly labeled lists:

- **GAMES**: a snapshot of BoardGameGeek's top 50, with cover images. The first question and the desert island question pick random games from it every time. To refresh it, ask Hoid to "update the top 50."
- **QUESTIONS**: the 10 questions and their answers
- **FLAVORS**: the Monopoly results and their write-ups
- **STAT_POOL**: the joke stat bars on the result card
- **RUNNERS**: the "runners-up" (all Monopoly versions)
- **SMUG_LINES**: what it says when someone retakes the test
- **ANALYZING**: the fake "analyzing" messages

Or just tell Hoid what you want changed.

## Putting it online (GitHub Pages, free)

1. Sign in at github.com (or create a free account).
2. Click the **+** in the top right, then **New repository**. Name it something like `board-game-quiz`. Set it to **Public**. Click **Create repository**.
3. On the next page, click **uploading an existing file**. Drag in `index.html`. Click **Commit changes**.
4. Go to the repository's **Settings**, then **Pages** in the left sidebar.
5. Under "Branch," pick **main** and click **Save**.
6. Wait a minute or two, then refresh. Your link appears at the top: `https://YOUR-USERNAME.github.io/board-game-quiz/`

To update it later, upload the new `index.html` the same way. It replaces the old one.

## Common problems

- **A game shows a 🎲 instead of its cover.** BoardGameGeek changed or removed that image. Ask Hoid to "update the top 50."
- **The fonts look plain.** The fancy fonts load from the internet. Without a connection, it falls back to normal fonts. Everything still works.
- **"Dare a Friend" doesn't open a share menu on a computer.** On phones it opens the share sheet. On most computers it copies the message and link instead, and shows "Copied!"
- **The GitHub link shows a 404.** Give it a few minutes after turning on Pages. Also make sure the file is named exactly `index.html`.
- **The shared link has no preview picture in texts.** That's expected. We can add a preview image later if you want one.
