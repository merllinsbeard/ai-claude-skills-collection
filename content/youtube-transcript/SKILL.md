---
name: youtube-transcript
description: Download YouTube video transcripts using Playwright browser automation. Use when user provides a YouTube URL and wants the transcript, asks to download/get/fetch captions or subtitles from a YouTube video.
allowed-tools: Bash,Read,Write
---

# YouTube Transcript Downloader (Playwright)

This skill downloads transcripts from YouTube videos using **Playwright browser automation**. It opens a headless browser, navigates to the video, clicks "Show transcript", and extracts the text.

## When to Use This Skill

Activate this skill when the user:
- Provides a YouTube URL and wants the transcript
- Asks to "download transcript from YouTube"
- Wants to "get captions" or "get subtitles" from a video
- Needs text content from a YouTube video

## Prerequisites

This skill requires the **Playwright skill** to be installed at:
```
/Users/merlin/.claude/plugins/marketplaces/playwright-skill/skills/playwright-skill
```

## How It Works

1. Extract VIDEO_ID from the YouTube URL
2. Write a Playwright script to `/tmp/yt-transcript-VIDEO_ID.js`
3. Execute the script via Playwright skill's runner
4. Return the path to the saved transcript

## Step-by-Step Process

### Step 1: Extract Video ID

From a YouTube URL like:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://youtube.com/watch?v=VIDEO_ID&...`

Extract the VIDEO_ID (11 characters, alphanumeric with `-` and `_`).

### Step 2: Write the Playwright Script

Create a file at `/tmp/yt-transcript-VIDEO_ID.js` with this content:

```javascript
const { chromium } = require('playwright');
const fs = require('fs');

const VIDEO_URL = 'https://www.youtube.com/watch?v=VIDEO_ID_HERE';
const OUTPUT_FILE = '/tmp/youtube_transcript_VIDEO_ID_HERE.txt';

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    viewport: { width: 1920, height: 1080 }
  });
  const page = await context.newPage();

  try {
    console.log('Opening YouTube video...');
    await page.goto(VIDEO_URL, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.waitForTimeout(4000);

    // Dismiss cookie consent if present
    try {
      const acceptBtn = page.locator('button:has-text("Accept all"), button:has-text("Accept")');
      if (await acceptBtn.isVisible({ timeout: 2000 })) {
        await acceptBtn.click();
        await page.waitForTimeout(1000);
      }
    } catch (e) {}

    // Scroll to make description visible
    await page.evaluate(() => window.scrollTo(0, 400));
    await page.waitForTimeout(1000);

    // Try multiple expand button selectors
    console.log('Expanding description...');
    const expandSelectors = [
      'ytd-text-inline-expander #expand',
      '#description-inline-expander #expand',
      'tp-yt-paper-button#expand',
      '#expand',
      '[id="expand"]',
      'ytd-expander[collapsed] #more'
    ];

    for (const selector of expandSelectors) {
      try {
        const expandBtn = page.locator(selector).first();
        if (await expandBtn.isVisible({ timeout: 1000 })) {
          await expandBtn.click();
          console.log('Expanded description with: ' + selector);
          await page.waitForTimeout(1500);
          break;
        }
      } catch (e) {}
    }

    // Try multiple methods to find transcript button
    console.log('Looking for Show transcript button...');

    // Method 1: Direct transcript button in description
    const transcriptSelectors = [
      'button:has-text("Show transcript")',
      'ytd-button-renderer:has-text("Show transcript") button',
      '[aria-label*="transcript" i]',
      'ytd-video-description-transcript-section-renderer button'
    ];

    let foundTranscript = false;

    for (const selector of transcriptSelectors) {
      try {
        const btn = page.locator(selector).first();
        if (await btn.isVisible({ timeout: 2000 })) {
          await btn.click();
          console.log('Clicked transcript button: ' + selector);
          await page.waitForTimeout(2000);
          foundTranscript = true;
          break;
        }
      } catch (e) {}
    }

    // Method 2: Three-dot menu fallback
    if (!foundTranscript) {
      console.log('Trying three-dot menu...');
      const menuSelectors = [
        'ytd-menu-renderer button[aria-label="More actions"]',
        '#button-shape button[aria-label="More actions"]',
        'button[aria-label="More actions"]',
        'yt-icon-button#button'
      ];

      for (const selector of menuSelectors) {
        try {
          const menuBtn = page.locator(selector).first();
          if (await menuBtn.isVisible({ timeout: 2000 })) {
            await menuBtn.click();
            await page.waitForTimeout(1000);

            const transcriptMenuItem = page.locator('ytd-menu-service-item-renderer:has-text("Show transcript"), tp-yt-paper-item:has-text("Show transcript")').first();
            if (await transcriptMenuItem.isVisible({ timeout: 2000 })) {
              await transcriptMenuItem.click();
              await page.waitForTimeout(2000);
              foundTranscript = true;
              break;
            }
          }
        } catch (e) {}
      }
    }

    if (!foundTranscript) {
      console.log('ERROR: Could not find transcript button');
      process.exit(1);
    }

    // Extract transcript segments with multiple selectors
    const segmentSelectors = [
      'ytd-transcript-segment-renderer yt-formatted-string.segment-text',
      '.ytd-transcript-segment-renderer .segment-text',
      'ytd-transcript-segment-list-renderer yt-formatted-string',
      '[class*="segment-text"]'
    ];

    let segments = [];
    for (const selector of segmentSelectors) {
      segments = await page.locator(selector).allTextContents();
      if (segments.length > 0) {
        console.log('Found segments with: ' + selector);
        break;
      }
    }

    if (segments.length > 0) {
      const transcript = segments.join('\n');
      fs.writeFileSync(OUTPUT_FILE, transcript);
      console.log('');
      console.log('=== TRANSCRIPT SAVED ===');
      console.log('File: ' + OUTPUT_FILE);
      console.log('Lines: ' + segments.length);
    } else {
      console.log('ERROR: No transcript segments found');
      process.exit(1);
    }
  } catch (error) {
    console.error('ERROR:', error.message);
    process.exit(1);
  } finally {
    await browser.close();
  }
})();
```

**Replace `VIDEO_ID_HERE` with the actual video ID in both places.**

### Step 3: Execute the Script

Run the script using the Playwright skill:

```bash
cd /Users/merlin/.claude/plugins/marketplaces/playwright-skill/skills/playwright-skill && node run.js /tmp/yt-transcript-VIDEO_ID.js
```

### Step 4: Report Results

After successful execution, inform the user:
- Path to the transcript file: `/tmp/youtube_transcript_VIDEO_ID.txt`
- Number of lines extracted
- Optionally show a preview of the content

## Complete Example

For URL `https://youtu.be/Qe_LiVZ308w`:

1. VIDEO_ID = `Qe_LiVZ308w`
2. Script file = `/tmp/yt-transcript-Qe_LiVZ308w.js`
3. Output file = `/tmp/youtube_transcript_Qe_LiVZ308w.txt`

Execute:
```bash
cd /Users/merlin/.claude/plugins/marketplaces/playwright-skill/skills/playwright-skill && node run.js /tmp/yt-transcript-Qe_LiVZ308w.js
```

## Error Handling

### Playwright Method Fails
If the Playwright script outputs any ERROR, **automatically switch to the yt-dlp fallback method** (see below).

Common Playwright errors:
- `ERROR: Could not find transcript button` - YouTube UI changed, selectors outdated
- `ERROR: No transcript segments found` - Transcript panel opened but couldn't extract text
- Timeout errors - Page didn't load properly

### Transcript Not Available
Some videos don't have transcripts. Both methods will fail. Inform the user that this video doesn't have subtitles/captions available.

### Video Not Found / Private
If the video is private or doesn't exist, both methods will fail with authentication errors.

### Network Issues
If there are network problems, the Playwright script will timeout after 30 seconds. Try yt-dlp as fallback.

## Tips

- The transcript is saved as plain text, one line per caption segment
- Works with both manual and auto-generated subtitles
- Headless mode means no browser window will appear
- Files in `/tmp/` are automatically cleaned by the system

---

## Fallback Method: yt-dlp

**If the Playwright method fails**, use yt-dlp as a fallback. This method is more reliable because it uses YouTube's API directly and authenticates via browser cookies.

### Prerequisites

- `yt-dlp` must be installed (`brew install yt-dlp` or `pip install yt-dlp`)
- Chrome/Firefox browser with YouTube cookies

### Step 1: Download Subtitles

```bash
yt-dlp --cookies-from-browser chrome \
       --write-auto-sub --sub-lang en \
       --skip-download \
       -o "/tmp/youtube_transcript_VIDEO_ID" \
       "https://www.youtube.com/watch?v=VIDEO_ID"
```

This downloads subtitles to `/tmp/youtube_transcript_VIDEO_ID.en.vtt`

**Options:**
- `--cookies-from-browser chrome` - Use Chrome cookies for authentication (also supports `firefox`, `safari`, `edge`)
- `--write-auto-sub` - Download auto-generated subtitles if manual not available
- `--sub-lang en` - Language preference (change to `ru`, `es`, etc. as needed)
- `--skip-download` - Don't download the video, only subtitles

### Step 2: Convert VTT to Plain Text

```bash
cat /tmp/youtube_transcript_VIDEO_ID.en.vtt | \
  grep -v "^WEBVTT" | \
  grep -v "^Kind:" | \
  grep -v "^Language:" | \
  grep -v "^$" | \
  grep -v "^[0-9][0-9]:[0-9][0-9]:[0-9][0-9]" | \
  grep -v "align:start position:" | \
  sed 's/<[^>]*>//g' | \
  uniq > /tmp/youtube_transcript_VIDEO_ID.txt
```

This removes:
- VTT headers (WEBVTT, Kind, Language)
- Timestamps (00:00:00.000 format)
- Position/alignment tags
- HTML tags like `<c>` and `</c>`
- Duplicate lines

### Complete yt-dlp Example

For URL `https://www.youtube.com/watch?v=DcrXHTOxi3I`:

```bash
# Download subtitles
yt-dlp --cookies-from-browser chrome \
       --write-auto-sub --sub-lang en \
       --skip-download \
       -o "/tmp/youtube_transcript_DcrXHTOxi3I" \
       "https://www.youtube.com/watch?v=DcrXHTOxi3I"

# Convert to plain text
cat /tmp/youtube_transcript_DcrXHTOxi3I.en.vtt | \
  grep -v "^WEBVTT" | \
  grep -v "^Kind:" | \
  grep -v "^Language:" | \
  grep -v "^$" | \
  grep -v "^[0-9][0-9]:[0-9][0-9]:[0-9][0-9]" | \
  grep -v "align:start position:" | \
  sed 's/<[^>]*>//g' | \
  uniq > /tmp/youtube_transcript_DcrXHTOxi3I.txt
```

### yt-dlp Troubleshooting

**"Sign in to confirm you're not a bot"**
- Use `--cookies-from-browser chrome` to authenticate via browser cookies
- Make sure you're logged into YouTube in the browser

**No subtitles found**
- Try `--sub-lang en,auto` to accept any language
- Some videos simply don't have captions available

**Permission denied for cookies**
- Close the browser before running yt-dlp
- Or use `--cookies /path/to/cookies.txt` with exported cookies
