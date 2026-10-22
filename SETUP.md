# Setting up your new GitHub profile (no terminal needed)

Everything happens on github.com in your browser. Allow about 20 minutes.

## 1. Upload the files
1. Go to **github.com/fredkamm/fredkamm** (your profile repo).
2. **Back up your old README first.** Open `README.md`, click the copy-raw-file button, and paste it into a note somewhere safe.
3. Click **Add file → Upload files**.
4. Unzip `fredkamm-profile.zip` on your computer. Drag in **everything inside the folder**: `README.md`, `assets`, `scripts`, `.github`, and this `SETUP.md` if you want it. You can skip `preview.png`.
   - **Hidden folder warning:** `.github` starts with a dot, so Mac and Windows may hide it. On a Mac, press **Cmd + Shift + .** in Finder to show it. On Windows, turn on **View → Hidden items**.
   - If dragging the `.github` folder doesn't work, add each workflow by hand. Click **Add file → Create new file** and type the name `.github/workflows/metrics.yml` (the slashes create the folders), then paste in that file's contents. Do the same for `3d-contrib.yml`, `snake.yml`, `activity-graph.yml` and `.github/3d-contrib-settings.json`.
5. **Delete the old snake workflow.** Open `.github/workflows/main.yml` in the repo → **⋯ → Delete file** → commit. It publishes to the same `output` branch and would wipe the new snake images. Its schedule is also broken: it runs every minute for an hour, twice a day.
6. Choose **Commit directly to the main branch** and click **Commit changes**. Your old README is replaced at this point.

## 2. Create the METRICS_TOKEN secret
The Metrics workflow needs a personal access token so it can read your stats.
1. Go to **github.com/settings/tokens** and choose **Generate new token → Generate new token (classic)**.
2. Note: `profile metrics`. Expiration: **No expiration**, or 1 year if you set a reminder to renew it.
3. Tick only these scopes:
   - `public_repo` (under *repo*)
   - `read:user` (under *user*)
   - `read:org` (under *admin:org*)
4. Click **Generate token** and copy it. You only see it once.
5. Go to **github.com/fredkamm/fredkamm → Settings → Secrets and variables → Actions → New repository secret**.
6. Name: `METRICS_TOKEN`. Secret: paste the token. Click **Add secret**.

(The other three workflows use GitHub's built-in token, so they don't need a secret.)

## 3. Let the workflows save files
1. In the repo go to **Settings → Actions → General**.
2. Under **Actions permissions**, choose **Allow all actions and reusable workflows**.
3. Under **Workflow permissions**, choose **Read and write permissions** and click **Save**.

## 4. Run each workflow once by hand
Open the **Actions** tab. If GitHub asks, click **I understand my workflows, go ahead and enable them**. Then, for each one:
click its name on the left → **Run workflow** → **Run workflow**.

| Workflow | What it makes | Takes |
|---|---|---|
| **Metrics** | `metrics/languages.svg`, `metrics/habits.svg` | 3–6 min |
| **3D contribution graph** | `profile-3d-contrib/profile-blue-dark.svg` and `-light.svg` | ~1 min |
| **Contribution snake** | snake images on a new `output` branch | ~1 min |
| **Activity graph** | `generated/activity-dark.svg` and `-light.svg` | <1 min |

**Run them one at a time.** Wait for each green check before starting the next, because they all save files to the same branch.

## 5. What to expect
- Visit **github.com/fredkamm**. Sections show "broken image" icons until their workflow has run once; after that they fill in.
- From then on, all four workflows refresh every day on their own, early morning US Eastern time.
- **Delays:** GitHub caches images, so a change can take a few minutes, sometimes an hour or two, to appear. A hard refresh helps.
- **Light and dark mode:** the banner, terminal, tiles and contribution graphs switch automatically to match the visitor's theme.
- **Animations:** they play when the page loads. This is normal: the terminal types once, while the banner keeps moving gently.
- **If something fails:** a workflow with a red ✗ in the Actions tab usually means one of these:
  - the `METRICS_TOKEN` secret is missing or has expired (step 2);
  - "Read and write permissions" is still off (step 3).

## Make the graphs look full (recommended)
Your public contribution calendar currently shows very few contributions (about 1 in the last 31 days when checked). If much of your work happens in private repos, you can count it (as anonymous squares, nothing private is revealed):
**github.com/fredkamm → Contribution settings (above the green squares) → turn on "Private contributions"**.
The 3D graph, activity graph, and snake all read from that calendar.

## Things to review
- **Skills:** the list comes from your old README plus what we discussed. Remove anything you don't want listed.
- **Email badge:** it uses the address from your old README. Delete that line if you'd rather not show it.
