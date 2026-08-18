# Evidence-ledger supplement — Batch 009

Date: 2026-08-18  
Scope: support for treating referral completion and access barriers as distinct from merely naming a resource.

| Claim | Status | Evidence | Runtime consequence |
|---|---|---|---|
| A referral should be tracked to determine whether connection occurred | **DIRECT PROCESS SUPPORT** | AHRQ `Attend to Social Needs: Tool 18` says practices should follow up to ensure connections are actually made and document referral outcomes | `suggested` is not `connected`; preserve handoff state |
| Referral systems should not keep sending patients to clinicians who do not provide timely appointments or feedback | **DIRECT PROCESS SUPPORT** | AHRQ `Make Referrals Easy: Tool 21` advises against continuing such referrals and recommends investigating barriers when referrals are incomplete | Do not recycle an unavailable route; revise the plan |
| Cost, waiting time, transport, and distance create genuine unmet care | **DIRECT ACCESS EVIDENCE** | WHO analyses identify long waits, cost, and transportation/distance as major barriers to needed care | Access failure is current reality, not noncompliance |
| Affordability and structural barriers commonly prevent needed mental-health care | **DIRECT ACCESS EVIDENCE** | SAMHSA NSDUH reports identify cost/insurance and structural barriers among reasons needed services are not received | Record financial/structural barrier separately from goal endorsement |
| A smaller action plan should be collaboratively achievable | **ADJACENT SUPPORT** | AHRQ action-planning guidance emphasizes patient-owned achievable steps and follow-up | Choose the smallest reachable substitute while preserving the full unmet need |

## Sources

- AHRQ, `Attend to Social Needs: Tool 18` — https://www.ahrq.gov/health-literacy/improve/precautions/tool18.html
- AHRQ, `Make Referrals Easy: Tool 21` — https://www.ahrq.gov/health-literacy/improve/precautions/tool21.html
- AHRQ, `Make Action Plans: Tool 15` — https://www.ahrq.gov/health-literacy/improve/precautions/tool15.html
- WHO Kobe Centre, `Inequality in unmet healthcare and social care needs in Europe` — https://wkc.who.int/resources/news/item/27-12-2023-inequality-in-unmet-healthcare-and-social-care-needs-in-europe
- WHO European Observatory, `Gaps in access undermine universal health coverage across the EU` — https://eurohealthobservatory.who.int/news-room/news/item/29-11-2019-gaps-in-access-undermine-universal-health-coverage-across-the-eu
- SAMHSA, `1.5 Million Young Adults Do Not Receive Needed Mental Health Services` — https://www.samhsa.gov/data/sites/default/files/report_1975/Spotlight-1975.html
- SAMHSA, `Affordability Most Frequent Reason for Not Receiving Mental Health Services` — https://www.samhsa.gov/data/report/affordability-most-frequent-reason-not-receiving-mental-health-services-2009-2011-nsduh

## Limits

These sources support access/handoff architecture. They do not prove that the complete therapy protocol or a future bot is clinically safe.
