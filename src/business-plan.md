# motdang — business plan

Oct 14, 2026 · @Nan

## At a glance

motdang maps northern Thailand street by street, then sells what a foreigner or a migrant worker cannot get here without a Thai friend: papers, translation, home help, and soon money transfer. The map is built and requested about 150,000 times a day; 99.9% of those requests are machines. Revenue to date is ฿0; prices are set and payment pages are live. motdang is raising ฿35M for a share of revenue, to take the Thailand–Myanmar money corridor and 100 cities in its first year.

The short version, as toys in five languages: [The Red Ant Plan](https://claude.ai/artifact/7FuS9tESMtoELfMgDBcWbk).

|  |  |
| --- | --- |
| Company | motdang.net Co., Ltd. (บริษัท มดแดง.เน็ท จำกัด), Thai, DBD 0575569006139, registered 22 September 2026 |
| Registered capital | ฿5,000,000 |
| Shop | 48–49 Thai Wiwat Alley, Chiang Rai |
| Trading names | motdang.net · Hongdam (hongdam.net) · Chiang Mai Visa Desk (chiangmaivisadesk.com) |
| Cities on the map | Chiang Mai, Chiang Rai, Pathum Thani, Phnom Penh |
| People | NaN (founder), Beer (director, 51% shareholder, operations), Marcus (builder) |
| Revenue to date | ฿0 |
| Running cost | about ฿60,000 a month (see Financials) |

<!-- คาถา · katha: fuck-you money -->

**Mood:** weird. **Byproduct:** people in the Mekong countries who are harder to erase, because they are paid, papered, mapped and on record. Every line of business below makes money first; the byproduct rides along.

## Problem

In northern Thailand, getting anything done runs through a Thai friend who knows who to call. Thai people call that friend, or open Google Maps. A foreigner with a Thai partner borrows the partner; everyone else goes without.

NaN's version: "Beer solves all my problems now." Beer combines Google Maps, Google, motdang search and local knowledge, calls down a list in Thai, and comes back with an answer. motdang sells that, at scale.

The jobs foreigners name as hard: a plumber, a maid, a gardener, a dentist open on Sunday, the bus to Chiang Rai, a bank account, a driver's licence, a clinic, a watch or shoe repair, ordering on Grab or LINE MAN, navigating 7-Eleven, renting a flat. Grab and LINE serve Thai users well and leave foreigners stuck at the first screen in Thai.

The same gap is wider for the 4.6 million Myanmar people living in Thailand ([IOM via UN Thailand](https://thailand.un.org/en/310197-rapid-assessment-myanmar-migrant-workers-ranong-and-tak-provinces-thailand-july-2025-read)), and for about 600,000 people registered as stateless ([UNHCR](https://reporting.unhcr.org/node/542)). They need papers, translation and a way to send money home; most of that money moves through informal hundi brokers today.

What a helper does, in ten verbs: knows who · knows the fair price · knows what is open now · calls in Thai · tells you what to say · tells you what to bring · reads Thai · pays the Thai way · comes with you · sorts it out when it goes wrong.

**The last verb, 13–15 October 2026.** NaN's house needed drains cleared and a light circuit looked at. Beer booked a handyman. He came late on the 13th. On the 15th he did not come; Beer called him, heard he would be late again, and dropped him: "This guy is so weird, not communicat and I'm not trusting him anymore." She is finding another. A directory lists a handyman. It cannot see that he has stopped being worth the wait, or decide at 10 a.m. to go find a better one. That call is what a helper is paid for, and a listing site does not make it.

## Built and live

The map, the payment pages and three priced services are live; revenue waits on payment being switched on and on people finding us. Counts as of 14 October 2026.

| Asset | Count or state |
| --- | --- |
| Places on the live map (Chiang Mai + Chiang Rai) | 88,943 |
| Pages across 20 sites | 110,263 |
| Records held, all corpora | 304,123 in 18 corpora |
| Requests to motdang.net, one week | 1,069,281 requests, 7–13 Oct 2026; 64% from AI crawlers (Meta's alone 421,516) |
| People, same week | people opened 1,258 pages that week (1,127 from Thailand), counted by the browser beacon: about 1 page per 850 machine requests |
| Cities | Chiang Mai, Chiang Rai live; Pathum Thani and Phnom Penh live as growing |
| Languages | Thai, English, Burmese, Shan; Khmer on Phnom Penh |
| Own pages (sites.motdang.net) | live: anyone makes a page with map, LINE and Grab tools; Gold tier ฿3,000 a year |
| Home help board | live; agreements, wage page, 250 shops |
| Translation desks | live on hongdam.net and chiangmaivisadesk.com, with a PromptPay payment box |
| Parking and walk-back app | live at motdang.net/parking (5,024 places); Android app 0.4 |
| Open data | 88,161-row dataset and four more repositories public on Hugging Face |
| Payment kit | PromptPay QR with automatic slip check, built; switched off until the SlipOK account is set up |
| Infrastructure | own build server and 5 TB store in Germany, Cloudflare at the edge, world map tiles self-hosted |

The stack is the moat and the cost base at once: NaN and AI agents built it, with Beer in the field, since the first commit on 27 July 2026, for under ฿2,000 a month in servers.

## Customers

NaN: "Right now I have millions of customers, problem is none of them pays." Six groups read or use motdang; four of them can pay now.

| Group | What they need | What they pay for | Paying now? |
| --- | --- | --- | --- |
| Foreigners living in the north (long-stay, retirees, remote workers) | the Thai friend: who, price, open now, what to say | visas, translation, home help, help in person | prices live |
| Myanmar, Shan, Lao and Cambodian workers in Thailand | papers, translation, money home | translation, document reminders (฿100 a year), remittance | prices live; remittance planned |
| Thai small businesses | to be found by foreigners and machines | Gold pages, employer subscriptions, referrals | prices live |
| Thai residents | parking, toilets, open now, events | nothing; they make the map worth reading | free |
| Machines: AI agents and crawlers | ground truth on places, prices, hours, Thai names in Latin letters | data licences now; per-call billing later | offers sent 6 October 2026 |
| Other businesses | payment, hosting, company formation | the motdang stack as a service | planned |

Among people, NaN finds motdang does best with three groups: vibe coders, computer engineers, and displaced Burmese people. The machines are the largest readership by far, and they arrive without marketing.

## Revenue

Sixteen lines, each a toll at a crossing people already make. Three are open to the public now; the first baht waits on the slip-check account and on traffic from people rather than machines.

| Line | Sells | Price | Status |
| --- | --- | --- | --- |
| Translation | new and checked translations, stamped, EN/TH/Burmese | new ฿1,500 up to 5 pages, then ฿500 a page; checked ฿500 up to 5 pages, then ฿150; stamp ฿100 a page | Live |
| Visa desk | visa work in Chiang Mai, migrant routes included (MOU, pink card, border pass) | quoted in writing | Live |
| Own pages | a page of one's own with map, LINE and Grab tools | basic free; Gold ฿3,000 a year | Live |
| Document reminders | LINE reminders before a worker's papers expire | ฿100 a year per document | Built |
| Home help | employment agreements, employer subscriptions, building packs, referrals | agreement ฿100; employer ฿1,000 a month; building ฿2,000 a month; 15% of each booking | Built |
| Data licences | 89,000 places with weekly changes, field photos, Thai names read in Latin letters | per licence | Offered to GrabMaps, LINE MAN Wongnai, Perplexity, AI Singapore |
| Lead research | named decision-makers for businesses abroad (Hongdam) | US$1 a line | Offered |
| Currency exchange | a counter run with Laila Luxe Co., Ltd., next door | share of net | In setup |
| Remittance | money home to Myanmar for workers in Thailand | fee plus exchange spread | Planned |
| Company formation | Thai companies for foreigners, US treaty companies for Thais, both ways | to be set | Planned |
| Payment system | motdang's own payment rail, offered to other businesses | to be set | Planned |
| Hosting and storage | servers in more than one country, sold to businesses that want their records out of one country's reach | to be set | Planned |
| Business factory | virtual businesses built on the motdang stack, run, then sold | sale price per business | Planned |
| Bot billing | answers and bookings for the AI agents that already read motdang | per call | Planned |
| Merch | motdang clothing and goods | to be set | Planned |
| Import | goods brought into Thailand to order; a margin on each shipment | to be set | Planned |

Live: open to the public with a price. Built: made, not yet charging. In setup: being arranged. Planned: not built.

Payment is automatic by design: a PromptPay QR carries the exact amount, the payer uploads the bank slip, SlipOK confirms it, and the service opens without a person checking.

## Why it can win

motdang costs almost nothing to run, holds data joined across Thai and Latin scripts, and sits where three borders meet with a Thai-majority company that can enter trades foreigners cannot.

- **Cost.** AI agents build and rebuild the whole map every round on one rented server. Servers cost under ฿2,000 a month; the largest cost is one salary. A rival doing this by hand needs a team.
- **Data joined across two scripts.** State registers (temples, schools, pharmacies, condominiums) are Thai-only; most open map records are Latin-only. Only 24% of the catalogue held both scripts of its own name when measured in September 2026. motdang reads Thai names into Latin letters and joins the halves, so a foreigner can find a Thai-only pharmacy and a machine can match it.
- **Ground truth from the street.** Ride-camera footage, NaN's own photos and Beer's calls feed place records: signs read, prices seen, parking spots found by stopping in them.
- **Machines already come.** In the week of 7–13 October 2026, 64% of 1,069,281 requests came from AI crawlers. Answer engines read us every night at no marketing cost; the open datasets on Hugging Face carry the name further.
- **Place.** The shop is in Chiang Rai, an hour from the Golden Triangle. Laila's money exchange is next door. Burmese and Shan speakers are on the team.
- **Structure.** The company is Thai-majority, so it can hold licences and run trades (exchange, transport, agriculture, land-adjacent work) that a foreign-owned firm needs special permission for.

## Competition

Each rival is strong at one crossing; motdang puts all of them on one map, in four languages, with a person behind it.

| Rival | Strong at | Gap motdang fills |
| --- | --- | --- |
| Google Maps | coverage, directions, reviews | Thai-only businesses unreadable in English; no help placing the call; little Burmese or Shan |
| Grab, LINE MAN Wongnai | rides, food, payments for Thai users | foreigners stall at Thai-language steps; no papers, translation or home help |
| Facebook expat groups | fast answers from neighbours | answers scroll away; nothing stays findable |
| Visa agents | one service, in person | single trade; no map, no follow-on services |
| Hundi brokers | cheap, trusted money home | cash only, no record; nothing else on offer |
| City guides and magazines | editorial, events | static lists; no booking, payment or help |

Grab and LINE MAN Wongnai are also prospective customers: both were offered a data licence on 6 October 2026.

## Team and company

Four people and a fleet of AI agents run the map, two service desks and a shop.

| Person | Role | Brings |
| --- | --- | --- |
| NaN | founder | built motdang; taxonomy work at Quora; US treaty-investor (E-1/E-2) visa work, then business plans and company formation for visa applicants |
| Beer | director of record, 51% shareholder, operations lead | Thai; full-time since August 2026; holds a tourism licence; does what motdang will do at scale |
| Marcus | intern, tech overhaul | intern; oversees the tech overhaul; sees the vision and brings a large circle of talented friends |
| Michael | advisor | NaN: "Nobody knows what he does, but he helps me make good decisions." |

- **Ownership.** Beer holds 51%, the Thai majority the Foreign Business Act requires for many of these trades. Investors in this round take a share of revenue, not shares, so ownership stays as it is; counsel writes the paper per investor.
- **Partners.** Laila Luxe Co., Ltd. (money exchange, next door, Chiang Rai).
- **Where the team works.** A GitHub organisation where a merge to main publishes the site, and a Discord server by project.

## Road map

With ฿35M, the first year takes the Thailand–Myanmar money corridor and 100 cities; five years puts motdang on a stage at Davos.

&#91;embedded content: road map · three horizons from 14 October 2026\]

The shaded goals are NaN's cards on the team road map; the steps above them are this plan's placement, for the team to move.

## Financials

With ฿35M, year one aims at ฿28.8M a month in revenue by month 12: about ฿345M a year, ten times the raise. Today motdang spends about ฿61,000 a month and earns nothing. Amounts in baht; US$1 ≈ ฿33, assumed.

**Year one on ฿35M: world domination, itemised.** Targets, not forecasts; each volume is a stated assumption.

| Line | Target by month 12 | Unit | ฿ a month at month 12 |
| --- | --- | --- | --- |
| Remittance, Thailand to Myanmar, then Cambodia and Laos | 100,000 senders, 2 transfers a month | ฿60 margin a transfer, assumed | 12,000,000 |
| Papers: translation, visas, companies both ways, reminders | 500 translations, 200 visa or company cases, 200,000 documents watched | ฿1,800 · ฿15,000, assumed · ฿100 a year | 5,570,000 |
| Own pages, worldwide | 20,000 Gold pages | ฿250 a month | 5,000,000 |
| Payment rail for other businesses | 2,000 businesses | ฿1,000 a month, assumed | 2,000,000 |
| Data licences and bot billing | 10 licences; 10 million paid calls | ฿100,000 a month · ฿0.10 a call, assumed | 2,000,000 |
| Home help | 1,000 employers, 100 buildings | ฿1,000 · ฿2,000 a month | 1,200,000 |
| Business factory | 12 businesses sold | ฿1M each, assumed | 1,000,000 |
| **Total** |  |  | **about 28,800,000** |

The remittance target moves about ฿1.6 billion a month at an assumed ฿8,000 a transfer: roughly a tenth of the US$5.6 billion Myanmar's finance ministry counted in worker remittances for 2025 ([Mekong Migration Network, citing Bloomberg](https://mekongmigration.org/?p=24805)). Most of that money still moves through hundi brokers; an ILO survey found 85% of migrants' transfers going through informal agents, at about ฿300 a transfer ([ILO 2010, via Susan Cunningham](https://susanjcunningham.com/2025/05/29/myanmar-fintech-migrant-workers-stick-to-underground/)). Chiang Mai took 11,485,568 visits in 2024 and visitors spent ฿103.8 billion: about ฿9,039 a visit (Thai ฿7,821, foreign ฿11,833). Rooms take 36% of a foreign visitor's spend, food and drink 23%, shopping 18%, the rest 23% (Ministry of Tourism and Sports survey, 2023). motdang is paid nothing of that today; rooms, through booking links, come first. Chiang Mai drew up to 12 million visitors in 2025 ([TAT, via Le Petit Journal](https://lepetitjournal.com/thailande/chiang-mai-destination-touristique-pleine-mutation-435044)).

**Where the ฿35M goes, over 12 months**

| Use | ฿ | Buys |
| --- | --- | --- |
| People | 12M | helpers paid per job in every city, translators, visa and company staff, Marcus's tech overhaul |
| Money rail and licences | 8M | counsel, licence applications, settlement float with a licensed partner, slip checking at volume |
| Reaching people | 6M | Burmese and Shan community agents, launch nights, the LINE official account, merch as marketing |
| Cities and servers | 3M | 100 city builds across Thailand, Myanmar, Laos, Cambodia and Vietnam; servers in three countries |
| Shops and border counters | 3M | a Chiang Mai storefront; counters in Mae Sot and Mae Sai, where workers cross |
| Reserve | 3M |  |
| **Total** | **35M** |  |

Spending runs near ฿2.9M a month. On a straight ramp to the month-12 rate, revenue passes spending within the first quarter.

**Running cost today, monthly, October 2026**

| Item | ฿ a month | Basis |
| --- | --- | --- |
| Beer, salary | 40,000 | agreed term |
| AI subscriptions (Claude, Gemini) | about 20,000 | approximate |
| Servers, storage, edge | about 1,000 | build server US$7.09, 5 TB store US$13, Cloudflare and R2 |
| Shop rent, Marcus's pay | not on this disk | to add |
| **Total known** | **about 61,000** |  |

**What investors get back.** Term: 10% of monthly revenue until investors hold 3× the money drawn (฿105M if all three draws). On the year-one ramp they receive about ฿19M in the first 12 months and about ฿2.9M a month after; 3× lands around month 42 at the month-12 rate, sooner if revenue keeps climbing.

## Risks

The largest risk is plain: nobody has paid yet. The rest are known and each has an answer under way.

| Risk | What could happen | Answer |
| --- | --- | --- |
| No revenue | readers stay mostly machines; people never pay | automatic payment on every service; data licences offered to four buyers; bot billing charges the machines directly |
| Pace | 100 cities and 100,000 senders in a year outruns the team | the city kit stood up Pathum Thani and Phnom Penh in days; helpers are paid per job, so people scale with work |
| Licences | exchange and remittance need Bank of Thailand licences; some trades need permits | a licensed partner's rail carries money while ours is applied for; Thai-majority company; Laila's exchange licence path; counsel before launch |
| Key person | NaN directs the build | the team holds admin on every repository; agents and open-weights models can run the stack; a merge publishes without her |
| Platforms | a provider changes terms or a social account is suspended (it has happened) | own servers, self-hosted map tiles, open-weights fallback; owned channels: LINE official account, Discord, events |
| Builds | a site build fails | the live site keeps its last good version; a failing page is held back while the rest publishes |
| Politics | border closures, Myanmar's remittance rules, attention from serving stateless people | records kept in more than one country; the same need is the market |
| Employment law | matching workers to employers carries licensing duties | home help runs as a notice board; no offers handled |

## The ask

motdang asks for ฿35M (about US$1.06M) in three draws, for 10% of monthly revenue until investors hold 3× what they put in. Beer keeps 51%. Contact: nan@motdang.net.

| Draw | Released when | Buys |
| --- | --- | --- |
| ฿5M | at signing | payment switched on, money home through a licensed partner, 20 cities, the first data and bot buyers |
| ฿10M | first ฿1M revenue month, or 10,000 senders | border counters, helpers in every city, Burmese and Shan community agents |
| ฿20M | 50,000 senders and a licence route set with counsel | float for transfers at volume, the Chiang Mai shop, the run to 100 cities |

**Terms**

| Term | Setting |
| --- | --- |
| Share | 10% of monthly revenue |
| Stops at | 3× the money drawn (฿105M if all three draws) |
| Revenue means | fees, spreads and sales motdang keeps; money carried for senders is not revenue |
| Paid | monthly, automatically, with a statement of revenue and each investor's share |
| Smallest cheque | ฿100,000 (about US$3,000), on a ladder ฿100,000 · ฿200,000 · ฿500,000 · ฿1,000,000; on the 1st, while a draw is open, 80% or more of it promised moves it up a rung, under 60% down a rung |
| Smaller | a founding membership at sites.motdang.net/founders: prepaid Gold, two Gold years and a number on the wall, ฿2,000–5,000 on its own ladder; not a share |
| Later draws | each investor joins draws 2 and 3 when the target is met, or may step out if a target is not met within 12 months of signing |
| Ownership | unchanged: Beer 51%; investors hold a revenue right, not shares |
| Paper | counsel drafts one agreement for every investor |

**Where to start reading, by kind of investor**

| Investor | Buys into | Read first |
| --- | --- | --- |
| Venture | a stack that builds cities for almost nothing, and machines as customers | Built and live, Why it can win |
| Impact and refugee funds | papers, money and records for people who lack them | Problem, Customers |
| Thai angels and family offices | a Thai company at the Golden Triangle with trades foreigners cannot enter | Team and company, Revenue |
| Strategic: maps, ride and delivery apps | ground-truth data in Thai and Latin letters, weekly | Revenue (data licences) |
| AI labs and answer engines | the places, prices and names their agents already read | Customers (machines) |
| Fintech | a remittance and payment rail on the Thailand–Myanmar corridor | Financials (remittance) |

**16 October 2026.** NaN: the smallest cheque ฿100,000 on a Shoup ladder, and the founding membership beside it.

**Settled, 14 October 2026.** NaN: ฿35M, a share of revenue, Beer's 51% shown, three draws. The terms above, one copy of this plan with the mission on page one, and sharing by link with named investors only (no public posting of the offer) were set on NaN's word to decide them.

*Be not afraid.*
