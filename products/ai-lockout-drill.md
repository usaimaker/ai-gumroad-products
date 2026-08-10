# The Lockout Drill: A Zero-Dollar Continuity Plan for the Account That Runs Your Business

One account is the master key to everything you run, and this is the free drill that makes losing it survivable.

## Why this is the one risk you cannot outsource

For a solo operator, the primary email account is not one account among many. It is the reset channel for every other account you own. It is often the login itself, through Sign in with Google or Sign in with Microsoft. It frequently holds the domain, the invoices, the contracts, and the client files.

Now the uncomfortable part. Consumer accounts at the large providers do not come with a phone number or an email address that reaches a human. Recovery is an automated process that scores how much you look like the real owner. Paid escalation exists, such as support bundled with a consumer subscription tier or an administrator inside a business workspace, but neither helps at 2am if you never set it up.

A business workspace lockout is worse. With no reachable administrator, staff cannot get password resets, a compromised account cannot be suspended, and billing cannot be fixed. Recovery then means proving domain ownership through a DNS record and waiting days or weeks.

The entire leverage is in preparation, and preparation costs nothing.

## Step 1: Name the single point of failure

Spend ten minutes answering five questions on paper:

- Which inbox receives password resets for your bank, payment processor, domain registrar, and ad accounts
- Which services you access with Sign in with Google or Sign in with Microsoft instead of an independent email and password
- Where the domain is registered, and who controls the DNS records
- Where client files and signed contracts actually live
- Which account owns the payout method

If one row appears in every answer, you have found the account to harden first. Most solo businesses have exactly one.

## Step 2: Build a break-glass kit

Everything here is free and takes about thirty minutes.

- **A second way in.** On a business workspace, create an administrator account that belongs to no individual, such as emergency-admin at your own domain. Standard guidance is to keep more than one super administrator, commonly two to six depending on size. For a solo business, two is the minimum that works.
- **Printed backup codes.** Generate them, print them, store the paper physically. They are single use, so regenerate after you spend one.
- **A recovery address on a different provider.** Never route recovery for an account back into that same account.
- **A recovery phone that is not your only factor.** Number transfer fraud is growing, so treat SMS as a fallback, never as the primary lock.
- **A one page paper card.** Record the month and year the account was created, the last password you are confident about, and the exact spelling of your recovery contacts. Recovery forms reward approximate answers and punish blanks.
- **Registrar hardening.** Turn on transfer lock, point registrar notifications at the recovery address, and set auto renewal with a card that is not about to expire. An expired card has taken more small businesses offline than any attacker.

## Step 3: Preserve the signals that make recovery possible

Consumer recovery is scored on behavior, not on identity documents. Four habits move that score more than anything else.

- **Keep one device permanently signed in.** An old phone that stays at home, signed in and untouched, is the strongest single recovery signal available.
- **Never wipe that device during an incident.** Factory resetting it destroys the session that would have proven you are the owner.
- **Run recovery from your usual device, browser profile, and network.** Private browsing strips the cookies and history the system reads as identity, so it makes you look like a stranger.
- **Fill in every field, once.** Approximate answers beat empty ones, and a burst of random guesses looks like an attack.

## Step 4: Close the doors a new password leaves open

Changing a password ends active sessions. It does not touch the four things intruders rely on to stay inside.

- Mail rules and forwarding that quietly copy, archive, or delete incoming mail, including the reset emails you are about to trigger
- Third party applications holding a standing authorization grant
- Application specific passwords and legacy mail client access
- Delegated mailbox access granted to another address

Work in this order, on a device you trust:

1. Screenshot the current state before deleting anything, because you will need to know what was there
2. Change the password from the official settings page, never from a link inside a message
3. Sign out all other sessions and devices
4. Revoke third party grants and application specific passwords
5. Delete unknown rules, filters, and forwarding addresses
6. Reset the recovery address and phone to your own
7. Rotate credentials for anything that inbox could have reset

Stolen session cookies are the reason multi factor authentication alone is not the finish line, so pair phishing resistant factors, meaning passkeys or hardware keys, with the habit of revoking sessions. The Google Advanced Protection Program is free, enforces hardware keys, and blocks most third party application access. The tradeoff is deliberate: recovery becomes slower for you as well.

## Step 5: What the free tools actually give you

Free tiers move, so confirm on the vendor pricing page before committing. As commonly documented in 2026:

- Bitwarden free stores unlimited items on unlimited devices, but built in one time codes are not included and hardware key sign in sits in the paid tier at around ten dollars a year
- Proton Pass free includes unlimited logins, built in one time codes, passkey support, and ten masked email aliases
- Apple Passwords is fully free on recent operating systems with passkeys and verification codes, but only inside that ecosystem
- KeePassXC is free, local, and supports one time codes, but you own the sync problem
- LastPass free is limited to one device type, mobile or desktop, not both
- NordPass free allows one active device at a time
- Dashlane free caps the vault at roughly twenty five items, which makes it evaluation only

One judgment call is worth making deliberately. Keeping the password and the second factor in the same vault is convenient and puts both keys in one basket. A reasonable middle ground is a vault for passwords, plus a separate authenticator app or hardware key for the three accounts that would end the business: email, registrar, payment processor. Masked aliases matter too, because credential reuse harvested from unrelated breaches is widely reported as the largest single source of takeover attempts, and a unique address per signup breaks that chain.

## Step 6: The first sixty minutes

If it happens today, containment comes before cleanup:

1. Move to a device you believe is clean
2. Capture evidence with screenshots and timestamps
3. Start the official recovery flow by typing the address yourself
4. Change the password, then end all sessions
5. Revoke grants, application passwords, and delegation
6. Remove hostile rules and restore recovery contacts
7. Protect the blast radius in order: registrar, payment processor, file sharing links, then every service using that account as its login
8. Send contacts a two line warning that recent messages may be hostile
9. Only then start cleaning up

## The quarterly fifteen minute drill

Put it on the calendar four times a year:

- Open the security review page and read the device list
- Revoke every third party application you have not used this quarter
- Confirm the recovery address and phone are still yours and still reachable
- Regenerate and reprint backup codes
- Confirm the always signed in device still opens the account
- Confirm the registrar lock and the billing card expiry date
- Attempt one recovery step so you learn the flow while calm

## What this does not cover

This is continuity planning, not compliance. It does not replace a written incident response policy, cyber insurance, or legal advice on breach notification duties. Vendor limits and support paths change without notice, so treat every number here as a prompt to check the official page, including the numbers in this document.

## How to use

Run it as a three week schedule rather than a single read.

Week one: complete Step 1 and Step 2. Write the single point of failure page, create the second administrator, print backup codes, fix the recovery address, lock the domain.

Week two: complete Step 3 and Step 5. Set up the always signed in device, choose your password and authenticator split, and move the three critical accounts to phishing resistant sign in.

Week three: run Step 4 as an audit even though nothing is wrong. Delete stale grants, unknown rules, and unused application passwords. Print Step 6, put it in the same envelope as the backup codes, and add the quarterly drill to your calendar.

If you only ever do one thing, do this: print the backup codes today and set a recovery address on a different provider. That single pair converts most lockouts from a business ending event into a bad afternoon.