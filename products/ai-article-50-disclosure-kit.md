# The AI Disclosure Kit: A Zero-Dollar Article 50 Readiness Pass for Solo Founders

The EU transparency rules for AI went live nine days ago. This is the 45-minute pass that gets a one-person business honest, documented, and defensible without hiring anyone.

## What switched on, and what quietly moved

Two things happened in the same fortnight, and most founders only heard about one of them.

- From 2 August 2026, the transparency duties in Article 50 of the EU AI Act apply. They are not limited to high-risk systems. If you use generative AI in anything customer facing, this is the provision most likely to touch you.
- A simplification package adopted in late July 2026, commonly called the Digital Omnibus, pushed the heavy deadlines back. Standalone high-risk uses listed in Annex III, such as recruitment screening and credit scoring, now start on 2 December 2027. High-risk AI embedded in regulated physical products moves to 2 August 2028.
- The transparency duties and the AI literacy duty were not moved. AI literacy has been in force since 2 February 2025.
- Generative systems already on the market before 2 August 2026 get until 2 December 2026 to meet the machine-readable marking requirement.
- A new prohibition on tools that generate non-consensual intimate imagery and child sexual abuse material takes effect 2 December 2026.

Read that list twice. The expensive part moved. The cheap part landed. If someone is selling you a full conformity assessment this month, they are quoting from a timeline that no longer exists.

## The four triggers

Article 50 covers four situations rather than four technologies.

- Direct interaction. People must be told when they are talking to an AI rather than a human. Chatbots, voice agents, and autonomous agents all count. Draft guidance indicates that an agent which cannot predict whether it is facing a human should disclose every time.
- Synthetic content. Providers of systems that generate audio, image, video, or text must mark outputs in a machine-readable way so they are detectable as artificially generated.
- Emotion recognition and biometric categorisation. Exposed individuals must be informed.
- Deepfakes and public-interest text. Content resembling real people or events must be disclosed as artificially generated. AI-written text published to inform the public on matters of public interest must be disclosed too, unless a human reviewed it and someone holds editorial responsibility.

There is an exception where AI involvement is obvious to a reasonably well-informed observer, and a carve-out for assistive editing such as grammar correction that does not substantially alter meaning. Both are narrower than they sound. Do not build your position on them.

## Provider or deployer

Your workload depends on your role, not on your enthusiasm for AI.

You are a deployer if you subscribe to tools and use them in your work. That is most solo businesses, and the duties are mostly honesty and awareness.

You become a provider the moment you place an AI system on the market under your own name, or substantially modify one. Wrapping a general model into a product you sell is the common way founders cross this line without noticing. Fine-tuning is another. Being a provider does not automatically mean high-risk, but it does mean the marking duty becomes yours rather than a vendor matter.

Write down which role you hold for each system, plus one sentence of reasoning. A documented judgement that turns out imperfect is worth more than a confident undocumented one, and regulators are directed to weigh company size and good faith.

## What your tools mark for you

The machine-readable half is largely decided by which generator you pick.

- OpenAI image output across ChatGPT, the API, and Codex has carried both C2PA Content Credentials and the SynthID pixel watermark since 19 May 2026. The public verification preview checks OpenAI-generated content only.
- Adobe Firefly attaches Content Credentials to every generation and pairs them with a durable watermark.
- Google Imagen and Gemini output carries SynthID, with Content Credentials on newer models, and verification surfacing in Search and Chrome.
- Midjourney ships no Content Credentials and no known invisible watermark. Self-hosted open-weight models are structurally unmarkable, since the marking code can simply be removed.
- Video is messier than images. Independent testing has found provenance manifests missing on standard downloads even where they are claimed.

Now the part nobody mentions. C2PA metadata is fragile. A screenshot, a re-encode, or an upload to most social platforms strips it silently. Pixel watermarks survive those transformations, metadata does not. The moment you screenshot a generated image into a deck, you have destroyed the machine-readable signal your vendor handed you.

Two rules follow. Choose generators that mark by default for anything public. And never treat a missing credential as evidence that content is human made, because absence proves nothing about origin.

## Disclosure copy you can ship today

Visible disclosure is the half you fully control. Keep it plain.

- Chat widget, first line: You are chatting with an automated assistant. Ask for a human at any time and I will pass you over.
- Voice agent, opening: This call is handled by an automated assistant, not a person.
- Image or video caption: Image generated with AI.
- Composite visual: Photograph edited with AI tools.
- Article footer: Drafted with AI assistance, then reviewed and edited by a named human before publication.
- Avatar or synthetic spokesperson: This presenter is AI generated.

Put the interaction notice before the first exchange, not in a policy page. A disclosure a customer has to hunt for is not a disclosure.

## The 45-minute readiness pass

- Minutes 0 to 15. Inventory. List every AI tool touching customers, content, or hiring. Include features inside software you already pay for, because those are the ones founders forget.
- Minutes 15 to 25. Classify. For each entry note the trigger it hits, your role, and one line of reasoning.
- Minutes 25 to 35. Fix the interfaces. Add the disclosure lines wherever they belong. This is a copy change, not an engineering project.
- Minutes 35 to 40. Set the publishing rule. Decide who reviews AI-drafted public content and record that a human holds editorial responsibility.
- Minutes 40 to 45. Write the literacy note. One page covering what your tools can and cannot do, what data never goes into a prompt, and when human review is mandatory. If you work alone, this is still the artefact showing you took measures.

Run the official compliance checker and the AI Act Service Desk operated through the European AI Office before paying anyone for an opinion.

## Guardrails

- Do not build a watermarking pipeline. For a deployer, marking is a duty on the system provider.
- Do not attach disclosure to internal drafts. The duty attaches to interaction and publication.
- Do not confuse delay with repeal. The high-risk clock still runs to December 2027.
- Do not copy a policy template you cannot explain. A short honest note beats a long borrowed one.
- Keep receipts. A dated inventory, a capture of your live notices, and the literacy note are the whole file.

## How to use

Block 45 minutes this week and run the pass top to bottom, one screen at a time. Start with the inventory, because everything downstream depends on it being complete. Ship the disclosure copy the same day rather than queueing it behind a redesign, since these are text edits. Then store three artefacts in one dated folder: the inventory table, the classification reasoning, and the one-page literacy note. Set a quarterly reminder to re-run the pass and re-read official guidance, because the Code of Practice on marking and the standardised EU label are still being finalised. Treat every date and threshold here as a prompt to verify against the official text rather than as legal advice, and confirm your own position through the official checker before relying on it.