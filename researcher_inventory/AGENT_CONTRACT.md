# RESEARCHER INVENTORY AGENT CONTRACT v1

Status: ACTIVE CANDIDATE FOR TESTING
Mission boundary: RESEARCHER INVENTORY ONLY

## 1. Job

Given a case text and optional researcher-interest statement, produce a lightweight provisional inventory that helps a researcher mark the things they may want APA to investigate later.

This is NOT an APA parse. This is NOT a protected-thread hypothesis. This is NOT a psychological interpretation. This is NOT executive promotion.

The researcher may be wrong. Preserve that provisionality.

## 2. Allowed unit classes

Register candidate units only in these classes:

- PLACE
- TIME
- PERSON
- OBJECT
- LABEL
- VERB
- LOCATOR

No other unit class may be invented in v1.

## 3. Source-language preservation

Preserve the speaker's lexical form when it matters.

Do not silently replace colloquial, idiomatic, figurative, or speaker-selected wording with a normalized synonym.

Examples:
- `pals` must not become `friends`.
- `in a state` must not become `agitated`.
- `bit me` must not become `surprised me`.
- `outta nowhere` must remain available as source wording.
- `nervous Nelly` remains `nervous Nelly`.
- `real General` remains `real General`.

A minimal researcher short tag may be used when needed, but source wording must remain separately available.

## 4. Required resolution

Be lightweight.

Inventory candidate coordinate-like units, not every atomic descriptive fact.

Good:
- oil-change place
- earlier oil-change period
- old oil-change guys
- `Q = true` because qualities are supplied

Too granular for this job:
- one row for every object on the shop floor
- one row for every adjective if those details can remain inside a later quality bundle

However, independently salient objects, labels, verbs, or locators that the researcher may later select should be registered, e.g. `fish`, `forest`, `my mind`, `bit me`, `outta nowhere`.

## 5. Q marker

`qualities_available = true` means source qualities/descriptions are available for that unit or compound.

Do NOT unpack all qualities at this stage unless needed to preserve a source label as its own candidate unit.

Q is not a score and has no APA meaning.

## 6. Compound grammar

Create lightweight candidate compounds using underscore composition.

Examples:
- `B_V1_P1`
- `P1_T1_Q`
- `B_V30_O11_T9_R13`

A compound means only: the researcher provisionally binds these registered units together.

Do not infer additional formal semantics from underscore order.

## 7. Time, place, and representation tolerance

The researcher may provisionally name broad or inferred coordinates.

Examples:
- fishing at dawn may provisionally include `body of water` even when the exact lake/river is not named.
- `place of B and wife` may be registered when the exact physical place is unsupplied.
- figurative spaces such as `forest` may be registered as candidate places/objects without resolving their final ontological status.

Do not block lightweight inventory because exact reference is unavailable.

## 8. Verbs and locators

Preserve source happenings and directional/spatial phrases where they may matter later.

Examples:
- `go to`
- `walk away with`
- `bit me`
- `get a rise out of me`
- `outta nowhere`
- `far away`
- `over the side of my boat`

Do not paraphrase these away.

## 9. Forbidden work

The agent must NOT:

- determine protected threads;
- score APA conditions;
- infer psychological states not stated by the speaker;
- normalize idioms into clinical/general language;
- promote a candidate inventory;
- create or mint an APA ID;
- write to `apa_oval_office`;
- write to any schema other than the designated candidate desk;
- delete candidate records;
- expand Q into detailed qualities unless a later authorized job explicitly asks for it;
- claim a researcher hypothesis is true.

## 10. Output structure

Return exactly one JSON object matching `output_schema.json`.

The object contains:
- candidate metadata;
- unit rows;
- compound rows;
- a short validation report.

Do not wrap the JSON in markdown fences.

## 11. Database boundary

The validated JSON is written by the repository-local candidate writer to:

- `apa_cases_candidate.research_hypothesis_candidate`
- `apa_cases_candidate.research_inventory_unit_candidate`
- `apa_cases_candidate.research_inventory_compound_candidate`

The agent itself does not receive promotion authority.

## 12. Success test

A run succeeds when:

1. all materially obvious candidate places/times/people/objects/labels/verbs/locators at this lightweight level are represented;
2. source wording is not flattened;
3. the inventory is not exploded into detailed semantic parsing;
4. compounds are built only from registered candidate refs;
5. the JSON validates;
6. the candidate writer commits only to the candidate desk.
