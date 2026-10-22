motdang business plan

Every version of motdang's business plan as one site, a page each. Live: https://motdang.github.io/business-plan/
Her ask 2026-10-14: "take all the business plan documents and put it in the motdang github as websites" — "one website many pages".

docs/plan/        the full plan, from src/business-plan.md (the Claude Docs plan, exported 14 Oct, rev 40)
docs/red-ant/     The Red Ant Plan      ← ../red-ant-plan-motdang/docs
docs/wheels/      The Wheels deck       ← ../motdang-roadmap/wheels/deck/project
docs/the-plan/    The Plan (27 Sep)     ← ../the-plan/docs
docs/brief/       the brief (13 Aug)    ← ../motdang-deck/dist

Rebuild: python3 tools/build.py   (re-copies every source, re-renders plan, wheels and the index)
Public copy of the plan leaves out the itemised running-cost table and the internal note on how the terms were set.
Share card: tools/card.html → docs/card.jpg (bump CARD_V in build.py when it changes).
Publish: ~/.claude/bin/pr-push "<this folder>" "<title>"
Check the card: python3 ~/Developer/claude\ code\ projects/site-kit/sharecard.py https://motdang.github.io/business-plan/
