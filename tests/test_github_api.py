import unittest

from backend.github_api import GitHubReleaseClient


class GitHubReleaseClientTests(unittest.TestCase):
    def test_accepts_github_canonical_repository_asset_url(self):
        # GitHub canonicalizes this repository's underscore to a hyphen in
        # browser_download_url values returned by its Releases API.
        self.assertTrue(
            GitHubReleaseClient._is_repository_asset_url(
                "https://github.com/biswaspratyay/universal-video-downloader/"
                "releases/download/v1.3/UniversalVideoDownloader-v1.3-Windows-x64.zip"
            )
        )

    def test_parses_release_with_github_canonical_asset_url(self):
        release = GitHubReleaseClient._parse_release(
            {
                "tag_name": "v1.3",
                "published_at": "2026-10-11T19:53:37Z",
                "assets": [
                    {
                        "name": "UniversalVideoDownloader-v1.3-Windows-x64.zip",
                        "browser_download_url": (
                            "https://github.com/biswaspratyay/"
                            "universal-video-downloader/releases/download/v1.3/"
                            "UniversalVideoDownloader-v1.3-Windows-x64.zip"
                        ),
                        "size": 202021286,
                    }
                ],
            }
        )

        self.assertEqual(len(release.assets), 1)

    def test_rejects_asset_url_from_another_repository(self):
        self.assertFalse(
            GitHubReleaseClient._is_repository_asset_url(
                "https://github.com/biswaspratyay/another-repository/"
                "releases/download/v1.3/update.zip"
            )
        )


if __name__ == "__main__":
    unittest.main()
