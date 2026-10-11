# Changelog

## v1.3.1

### Fixes

- Restart the app automatically after a theme change in both source and packaged builds.

## v1.3

### Highlights

- Added an in-app **Update yt-dlp** action in the header. It checks for the latest official yt-dlp release, downloads and verifies it in the background, and prepares it for use after restart.
- Added a current yt-dlp version label below the update button. It refreshes after each update check and indicates when a restart is needed.
- Added seven visual themes, available from **Settings -> Themes**:
  - Emerald & Gold
  - Midnight Onyx & Champagne
  - Halloween
  - Christmas
  - Cyberpunk
  - Dark and Light themes remain available
- Added festive header decorations for the Halloween and Christmas themes.
- Updated the application and release version to **1.3**.

### Reliability

- yt-dlp updates are downloaded from the official PyPI release metadata, validated with the published SHA-256 digest, and installed without overwriting the running application.
- The updater prevents changes while a download is active and reports update status or errors clearly.

### Build and release

- GitHub Actions builds Windows and Linux packages for the `v1.3` release tag and publishes the resulting archives to GitHub Releases.
