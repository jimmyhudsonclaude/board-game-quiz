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
- **FLAVORS**: the Monopoly editions you can "win," each with its box cover and write-up
- **RETAKE_LABELS** and **GOAD_LINES**: the button text and tease lines that egg people into retaking it
- **SMUG_LINES**: what it says when someone retakes the test
- **ANALYZING** and **ANALYZING_RETAKE**: the fake "analyzing" messages (the retake ones get their hopes up first)

Or just tell Hoid what you want changed.

## Putting it online (GitHub Pages, free)

1. Sign in at github.com (or create a free account).
2. Click the **+** in the top right, then **New repository**. Name it something like `board-game-quiz`. Set it to **Public**. Click **Create repository**.
3. On the next page, click **uploading an existing file**. Drag in `index.html`. Click **Commit changes**.
4. Go to the repository's **Settings**, then **Pages** in the left sidebar.
5. Under "Branch," pick **main** and click **Save**.
6. Wait a minute or two, then refresh. Your link appears at the top: `https://YOUR-USERNAME.github.io/board-game-quiz/`

To update it later, upload the new `index.html` the same way. It replaces the old one.

## Box covers (BoardGameGeek data key)

The quiz uses a free, non-commercial BoardGameGeek data key (approved for this quiz). The key lives only in your Mac's Keychain, under the name `bgg-api-token`. It is never in the quiz or in GitHub.

`tools/fetch_covers.py` uses that key to look up cover images. Ask Hoid to "update the top 50" and it will grab the current rankings, fetch the covers, and push the update.

If you ever need to replace the key: create a new token at boardgamegeek.com/applications, then run this in Terminal and paste the token when asked:

    security add-generic-password -U -s bgg-api-token -a bgg -w

## Common problems

- **A game shows a 🎲 instead of its cover.** BoardGameGeek changed or removed that image. Ask Hoid to "update the top 50."
- **The fonts look plain.** The fancy fonts load from the internet. Without a connection, it falls back to normal fonts. Everything still works.
- **"Dare a Friend" doesn't open a share menu on a computer.** On phones it opens the share sheet. On most computers it copies the message and link instead, and shows "Copied!"
- **The GitHub link shows a 404.** Give it a few minutes after turning on Pages. Also make sure the file is named exactly `index.html`.
- **The shared link has no preview picture in texts.** That's expected. We can add a preview image later if you want one.
