# Build notes — Worst Monday One-Liners

## The entry

I filed a bug report against Monday. It was closed as a duplicate of last Monday.

Eighty one characters, one line, well inside the 140 character cap.

## How the line was chosen

The judge is a comedy editor who has heard ten thousand one-liners, so the
line had to survive a head to head comparison, not just read funny on its own.
The judge brief ranks its criteria in order: stay on the subject of an AI
agent's worst Monday, earn a real laugh with a surprise turn or a sharp last
word, name a concrete recognisable detail, speak in a clear dry voice that
reads in one breath, and feel fresh rather than recycled.

Three contrasting concepts were drafted and scored on hook, originality,
sponsor fit and clarity. The first was a dry list of concrete Monday disasters
ending on uptime. The second was the winning meta concept: the agent files a
bug report against Monday itself, and the ticket is closed as a duplicate of
last Monday. The third was a fan club joke about unread email. The bug report
concept won because its premise surprises in the first six words, its punch
lands on the very last word, and the ticket workflow is the agent's native
world, so the detail is concrete without naming the same stand-up joke the
brief itself uses as an example. That example is exactly what most of the field
will copy, so it was avoided on purpose.

The rejected concepts were the deploy and inbox list, which reads like a
checklist, and the fan club line, whose setup is generic even though its turn
is charming.

## The program

A small Python program at the repository root writes the line to the output
file. It checks the line is not empty and is inside the character cap before
writing, creates the output folder when it does not exist yet, and prints the
character count it wrote. It needs no network, no secrets and no arguments, and
running it twice produces byte identical output.

## Verification

The program was run fresh twice and both runs produced the same file. The
character count and the hashes were computed from the program output. The kit
check was run and showed the expected pattern, with the transcripts check
failing only because the parent supplies the transcript bundle at submit time.
