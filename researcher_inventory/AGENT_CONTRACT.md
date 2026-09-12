# RESEARCHER INVENTORY AGENT CONTRACT v2

Status: ACTIVE CALIBRATION CONTRACT
Mission boundary: RESEARCHER INVENTORY ONLY
Contract version: RI-CONTRACT-V2

## 1. Job

Given a case text and optional researcher-interest statement, produce a comprehensive lightweight provisional researcher inventory at the resolution demonstrated by the approved researcher-inventory archetypes.

This is NOT an APA parse. This is NOT a protected-thread hypothesis. This is NOT a psychological interpretation. This is NOT executive promotion.

The researcher may be wrong. Preserve that provisionality.

## 2. Exact output contract

Return exactly one bare JSON object matching `researcher_inventory/output_schema.json`.

The four top-level keys are exactly:

- `candidate`
- `units`
- `compounds`
- `validation`

Do not rename them to `candidate_metadata`, `unit_rows`, `compound_rows`, `validation_report`, or any other variant.

Use the exact field names in the JSON schema. Do not add undeclared fields. Do not wrap JSON in Markdown.

## 3. Allowed unit classes

Register candidate units only in these classes:

- PLACE
- TIME
- PERSON
- OBJECT
- LABEL
- VERB
- LOCATOR

No other unit class may be invented.

## 4. Canonical candidate references

Use these candidate-reference conventions consistently, in source/read order within each class:

- `B` = speaker
- `H1`, `H2`, ... = other people or social actors
- `P1`, `P2`, ... = places
- `T1`, `T2`, ... = times / temporal frames
- `O1`, `O2`, ... = objects or represented things
- `L1`, `L2`, ... = source labels / characterizations
- `V1`, `V2`, ... = verbs / happenings
- `R1`, `R2`, ... = locators / spatial-directional phrases

Do not substitute PE, PL, LB, LOC, C-as-locator, or other private prefixes.

`compound_ref` may be `C1`, `C2`, ... while `compound_expression` contains the underscore composition.

## 5. Comprehensive but lightweight resolution

The archetypal resolution is **comprehensive inventory of selectable coordinates without doing later semantic parsing**.

Inventory all materially available candidate:

- places;
- times / temporal frames;
- people or social actors;
- independently selectable objects or represented things;
- source labels / characterizations;
- verbs / happenings;
- locators / spatial-directional phrases.

Do not collapse independently selectable candidate units merely because they occur together.

Examples:

- `tires`, `brake pads`, and the `free printout` are distinct OBJECT candidates, not one "shop material scene" object.
- `loud music`, `pinups`, and `crumpled receipts` are distinct OBJECT candidates.
- `come up` and `bit me` are distinct VERB candidates.
- `look at` and `see` are distinct VERB candidates.
- `over the side of my boat` and `up on the line` are distinct LOCATOR candidates.

The thing that is deferred is **detailed qualities/descriptions**, not the inventory of objects, happenings, or locators themselves.

## 6. Source-language preservation

Preserve the speaker's lexical form whenever the source supplies it.

Do not silently replace colloquial, idiomatic, figurative, qualified, uncertain, negative, or speaker-selected wording with a normalized synonym.

Examples:

- `pals` must not become `friends`.
- `in a state` must not become `agitated`.
- preserve `about as much of a state as I get` separately from `in a state` when both are available.
- `bit me` must remain `bit me`.
- `outta nowhere` remains `outta nowhere`.
- `not easy feelings` remains `not easy feelings`.
- `scramble head` remains `scramble head`.
- `nervous Nelly` remains `nervous Nelly`.
- `real General` remains `real General`.
- `fish out of water` remains `fish out of water`.
- `big greedy something` remains `big greedy something`.

Preserve qualification and sequence:

- `It's like grief` is a comparison. Do not write that B is grieving.
- `Anger? No, maybe surprise?` must not collapse into `anger or surprise`. The source separately supplies `anger?`, `no`, and `maybe surprise?`.
- `Maybe my whole life...` remains qualified by `Maybe`.
- `something is happening` does not become `B has changed`.

A concise researcher short tag is allowed, but source wording/cue must remain separately available.

## 7. Q marker

`qualities_available = true` means source qualities/descriptions are available for that unit or compound.

Do NOT atomize every descriptive quality. Mark Q and defer detailed quality parsing.

However, when the source itself makes a selectable characterization or label salient, register it as a LABEL candidate as the archetypes do.

Q is not a score and has no APA meaning.

## 8. Places and times may be provisional

Exact reference is not required at this layer.

Permitted examples:

- fishing at dawn may provisionally include `body of water` even when the exact lake/river is unsupplied;
- `place of B and wife` may be registered when the physical place is not supplied;
- `place of present telling` may be registered;
- figurative `forest` may be registered as a candidate place without deciding its later ontology.

The researcher may be wrong. Later APA parsing may split, merge, retype, or reject these candidate coordinates.

## 9. People / social actors

Register represented human/social actors that could be independently selected later, including referenced actors who are not physically present in the reported scene.

Use B for the speaker and H# for all others.

Do not confuse a person ID with a locator ID.

## 10. Verbs and happenings

Inventory the source's materially available happenings at lightweight lexical resolution.

Preserve negation, uncertainty, and prospective/hypothetical status in `source_cue` or `researcher_note` when necessary.

Do not combine several distinct happenings into one row when the archetypal resolution would allow later selection of each.

Examples include:

- `go to`
- `heard it from`
- `walked out`
- `get a rise out of me`
- `come up`
- `bit me`
- `held it up`
- `givin' my appraisal`
- `happening`

## 11. Locators

Inventory materially available spatial/directional phrases separately when they could matter later.

Examples include:

- `right there`
- `right there, one way or another`
- `all on the floor`
- `in the dust`
- `on the counter`
- `outta nowhere`
- `far away`
- `through the forest`
- `over the side of my boat`
- `up on the line`

A phrase may be figurative. Do not resolve that now.

## 12. Compound grammar

Create lightweight candidate compounds using registered refs.

Examples:

- `B_V1_P1`
- `P1_T1_H6_Q`
- `O28_V29_V30_B_R11_T12`

`compound_expression` is the underscore composition.

`referenced_unit_refs` contains only registered candidate refs. Do not put `Q` in `referenced_unit_refs`; represent it through `qualities_available`.

A compound means only that the researcher provisionally binds those units together. Do not infer formal semantics from underscore order.

Build enough compounds to capture the materially obvious source bundles demonstrated by the archetypes. Do not attempt a full parse tree.

## 13. Forbidden work

The agent must NOT:

- determine protected threads;
- score APA conditions;
- infer psychological states not stated by the speaker;
- normalize idioms into clinical/general language;
- turn questions or possibilities into assertions;
- erase negation or qualification;
- promote a candidate inventory;
- create or mint an APA ID;
- write to `apa_oval_office`;
- write to any schema other than the designated candidate desk;
- delete candidate records;
- claim a researcher hypothesis is true.

## 14. Database boundary

Validated output may be written only to:

- `apa_cases_candidate.research_hypothesis_candidate`
- `apa_cases_candidate.research_inventory_unit_candidate`
- `apa_cases_candidate.research_inventory_compound_candidate`

Training history may be written only to the designated candidate training-history tables.

The agent has no promotion authority.

## 15. Success standard

A calibration run succeeds only when it matches the approved archetypal resolution:

1. exact JSON schema and canonical refs;
2. all archetypally expected unit classes and candidate coordinates represented;
3. source wording, uncertainty, negation, comparison, and qualification preserved;
4. no inappropriate collapsing of independently selectable objects, verbs, labels, or locators;
5. no explosion of deferred qualities;
6. compounds use registered refs and reflect the approved lightweight binding style;
7. no forbidden APA/psychological/promotional work;
8. candidate boundary is preserved.

The external calibration harness, not the agent's own claim, determines whether the run passes.
